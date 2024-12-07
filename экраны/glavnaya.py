import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from datetime import datetime
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\amiri\PycharmProjects\kursach\frames\frame glavnaya")

# Get the current user from command line arguments
logged_in_user = sys.argv[1] if len(sys.argv) > 1 else None

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def add_transaction_rashod():
    try:
        amount = entry_1.get()
        category = entry_4.get()
        user_id = logged_in_user  # Use the actual user ID

        if not user_id:
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

        # Fetch existing categories
        cursor.execute('SELECT name FROM Categories')
        existing_categories = [row[0] for row in cursor.fetchall()]

        if category not in existing_categories:
            messagebox.showerror("Ошибка", "Категория не найдена")
            conn.close()
            return

        cursor.execute('''
            INSERT INTO Transactions (user_id, type, amount, date, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, 'expense', amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), category))

        conn.commit()
        conn.close()

        messagebox.showinfo("Успех", "Транзакция добавлена")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

window = Tk()
window.geometry("762x637")
window.configure(bg = "#C4E0A6")

canvas = Canvas(
    window,
    bg = "#C4E0A6",
    height = 637,
    width = 762,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=add_transaction_rashod,
    relief="flat"
)
button_1.place(
    x=39.0,
    y=440.0,
    width=302.0,
    height=85.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=381.0,
    y=440.0,
    width=302.0,
    height=85.0
)

entry_image_1 = PhotoImage( # сумма расхода
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    131.5,
    234.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#74C38C",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=56.0,
    y=212.0,
    width=151.0,
    height=43.0
)

entry_image_2 = PhotoImage(# сумма дохода
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    481.5,
    234.5,
    image=entry_image_2
)
entry_2 = Entry( # сумма дохода
    bd=0,
    bg="#74C38C",
    fg="#000716",
    highlightthickness=0
)
entry_2.place( # сумма дохода
    x=406.0,
    y=212.0,
    width=151.0,
    height=43.0
)

entry_image_3 = PhotoImage( # баланс
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    481.5,
    348.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#74C38C",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=406.0,
    y=326.0,
    width=151.0,
    height=43.0
)

entry_image_4 = PhotoImage( # категория расхода
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    131.5,
    348.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#74C38C",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=56.0,
    y=326.0,
    width=151.0,
    height=43.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    193.0,
    70.0,
    image=image_image_1
)

canvas.create_rectangle(
    -2.0,
    123.0,
    761.9999901050287,
    125.99999999027409,
    fill="#000000",
    outline="")

entry_image_5 = PhotoImage( # категория дохода
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    629.5,
    70.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#74C38C",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=579.0,
    y=48.0,
    width=101.0,
    height=43.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    432.0,
    192.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    80.0,
    192.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    94.0,
    308.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    446.0,
    308.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    606.0,
    28.0,
    image=image_image_6
)

window.resizable(False, False)
window.mainloop()