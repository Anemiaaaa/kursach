import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, Entry
from tkinter import ttk  # Для создания таблицы (Treeview)
from datetime import datetime
import sys

from tkinter import Frame, Label


class TransactionManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def fetch_transactions_by_user(self, username):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM Users WHERE username = ?', (username,))
        user_id = cursor.fetchone()

        if user_id:
            user_id = user_id[0]
            cursor.execute('''SELECT Transactions.id, Transactions.type, Transactions.amount, Transactions.date, Transactions.description
                              FROM Transactions
                              WHERE Transactions.user_id = ?
                              ORDER BY Transactions.date DESC''', (user_id,))
            transactions = cursor.fetchall()
        else:
            transactions = []

        conn.close()
        return transactions

    def calculate_balance(self, transactions):
        balance = 0
        for transaction in transactions:
            amount = transaction[2]
            if transaction[1] == 'expense':
                amount = -amount
            balance += amount
        return balance


class GUI:
    def __init__(self, transaction_manager, user):
        self.transaction_manager = transaction_manager
        self.user = user
        self.transactions = self.transaction_manager.fetch_transactions_by_user(self.user)
        self.current_balance = self.transaction_manager.calculate_balance(self.transactions)

        self.window = Tk()
        self.window.geometry("762x637")
        self.window.configure(bg="#C4E0A6")

        self.canvas = Canvas(
            self.window,
            bg="#C4E0A6",
            height=637,
            width=762,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(-2.0, 123.0, 761.9999901050287, 125.99999999027409, fill="#000000", outline="")

        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(196.0, 70.0, image=self.image_image_1)

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(656.5, 68, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#74C38C", fg="#000716", highlightthickness=0, font=("Arial", 14))
        self.entry_1.place(x=606.0, y=47.0, width=101.0, height=43.0)
        self.entry_1.config(state='readonly', readonlybackground="#74C38C")
        self.update_balance()

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(633.0, 28.0, image=self.image_image_2)

        self.columns = ("ID", "Тип", "Сумма", "Дата", "Время", "Описание")
        self.transactions_table = ttk.Treeview(self.window, columns=self.columns, show="headings", height=20)

        self.transactions_table.heading("ID", text="ID")
        self.transactions_table.heading("Тип", text="Тип")
        self.transactions_table.heading("Сумма", text="Сумма")
        self.transactions_table.heading("Дата", text="Дата")
        self.transactions_table.heading("Время", text="Время")

        self.transactions_table.column("ID", width=0, stretch=False)
        self.transactions_table.column("Тип", width=150, anchor="center")
        self.transactions_table.column("Сумма", width=150, anchor="center")
        self.transactions_table.column("Дата", width=100, anchor="center")
        self.transactions_table.column("Время", width=100, anchor="center")
        self.transactions_table.column("Описание", width=0, stretch=False)

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14), rowheight=28)
        style.configure("Treeview.Heading", font=("Arial", 16, "bold"))

        for transaction in self.transactions:
            transaction_id = transaction[0]
            transaction_type = self.translate_type(transaction[1])
            amount = transaction[2]
            if transaction_type == 'Расход':
                amount = -amount
            date, time = self.format_datetime(transaction[3])
            description = transaction[4]

            self.transactions_table.insert("", 0, values=(transaction_id, transaction_type, amount, date, time, description))

        self.transactions_table.place(x=10, y=130, width=740, height=450)

        self.tooltip_label = ttk.Label(self.window, text="", background="#C4E0A6", font=("Arial", 12))
        self.tooltip_label.place(x=10, y=590)

        self.transactions_table.bind("<Motion>", self.on_hover)
        self.transactions_table.bind("<Leave>", self.on_leave)

        self.window.resizable(False, False)
        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\amiri\PycharmProjects\kursach\frames\frame istoria")
        return ASSETS_PATH / Path(path)

    def on_hover(self, event):
        item = self.transactions_table.identify_row(event.y)
        if item:
            values = self.transactions_table.item(item, "values")
            description = values[5]
            transaction_id = int(values[0])

            for index, transaction in enumerate(self.transactions):
                if transaction[0] == transaction_id:
                    balance = self.transaction_manager.calculate_balance(self.transactions[:index + 1])
                    self.tooltip_label.config(text=f"Описание: {description}\nБаланс: {balance}")
                    break
        else:
            self.tooltip_label.config(text="")

    def on_leave(self, event):
        self.tooltip_label.config(text="")

    def format_datetime(self, datetime_str):
        dt_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        date = dt_obj.strftime("%d.%m.%Y")
        time = dt_obj.strftime("%H:%M:%S")
        return date, time

    def translate_type(self, transaction_type):
        if transaction_type == 'income':
            return 'Доход'
        elif transaction_type == 'expense':
            return 'Расход'
        return transaction_type

    def update_balance(self):
        self.entry_1.config(state='normal')
        self.entry_1.delete(0, 'end')
        self.entry_1.insert(0, str(self.current_balance))
        self.entry_1.config(state='readonly', readonlybackground="#74C38C")

if __name__ == "__main__":
    logged_in_user = sys.argv[1] if len(sys.argv) > 1 else None
    transaction_manager = TransactionManager(r'C:\Users\amiri\PycharmProjects\kursach\экраны\users.db')
    gui = GUI(transaction_manager, logged_in_user)

