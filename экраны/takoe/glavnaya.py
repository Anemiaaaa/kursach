import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from datetime import datetime
import sys
from tkinter import Frame, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\amiri\PycharmProjects\kursach\frames\frame glavnaya")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def glavnaya():
    Application()


class Application(Frame):
    def __init__(self, root, user_id):
        self.root = root
        self.user_id = user_id
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path(r"C:\Users\amiri\PycharmProjects\kursach\frames\frame glavnaya")
        self.setup_ui()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def add_transaction_rashod(self):
        try:
            amount = self.entry_1.get()
            category = self.entry_4.get()

            if not self.user_id:
                messagebox.showerror("Ошибка", "Пользователь не найден")
                return

            if not amount or not category:
                messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля")
                return

            try:
                amount = float(amount)
            except ValueError:
                messagebox.showerror("Ошибка", "Сумма должна быть числом")
                return

            conn = sqlite3.connect(r'C:\Users\amiri\PycharmProjects\kursach\экраны\users.db')
            cursor = conn.cursor()

            cursor.execute('SELECT name FROM Categories')
            existing_categories = [row[0] for row in cursor.fetchall()]

            if category not in existing_categories:
                messagebox.showerror("Ошибка", "Категория не найдена")
                conn.close()
                return

            cursor.execute('''
                INSERT INTO Transactions (user_id, type, amount, date, description)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.user_id, 'expense', amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), category))

            conn.commit()
            conn.close()

            messagebox.showinfo("Успех", "Транзакция добавлена")
        except Exception as e:
            print(f"An error occurred: {e}")
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

    def setup_ui(self):
        self.root.geometry("762x637")
        self.root.configure(bg="#C4E0A6")

        self.canvas = Canvas(
            self.root,
            bg="#C4E0A6",
            height=637,
            width=762,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_transaction_rashod,
            relief="flat"
        )
        self.button_1.place(x=39.0, y=440.0, width=302.0, height=85.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(x=381.0, y=440.0, width=302.0, height=85.0)

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(131.5, 234.5, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#74C38C", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=56.0, y=213.0, width=151.0, height=43.0)

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(481.5, 234.5, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#74C38C", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=406.0, y=213.0, width=151.0, height=43.0)

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(481.5, 348.5, image=self.entry_image_3)
        self.entry_3 = Entry(bd=0, bg="#74C38C", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=406.0, y=327.0, width=151.0, height=43.0)

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(131.5, 348.5, image=self.entry_image_4)
        self.entry_4 = Entry(bd=0, bg="#74C38C", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=56.0, y=327.0, width=151.0, height=43.0)

        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(193.0, 70.0, image=self.image_image_1)

        self.canvas.create_rectangle(-2.0, 123.0, 761.9999901050287, 125.99999999027409, fill="#000000", outline="")

        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(629.5, 70.5, image=self.entry_image_5)
        self.entry_5 = Entry(bd=0, bg="#74C38C", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=579.0, y=50.0, width=101.0, height=43.0)

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(432.0, 192.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(80.0, 192.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(94.0, 308.0, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(446.0, 308.0, image=self.image_image_5)

        self.image_image_6 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(606.0, 28.0, image=self.image_image_6)

        self.root.resizable(False, False)


if __name__ == "__main__":
    logged_in_user = sys.argv[1] if len(sys.argv) > 1 else None
    root = Tk()
    app = Application(root, logged_in_user)
    root.mainloop()
