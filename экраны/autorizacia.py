import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import sqlite3

logged_in_user = None

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\amiri\PycharmProjects\kursach\frames\frame autorizacia")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def check_credentials(event=None):
    global logged_in_user
    username = entry_1.get()
    password = entry_2.get()

    # Подключение к базе данных
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Запрос к базе данных для проверки логина и пароля
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    result = cursor.fetchone()

    # Закрытие соединения
    conn.close()

    if result:
        logged_in_user = username
        open_main()
    else:
        messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль")

def open_main():
    if logged_in_user:
        window.destroy()
        subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\main.py", logged_in_user])
    else:
        messagebox.showerror("Ошибка", "Вы не вошли в систему")

def open_registration():
    subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\register.py"])

window = Tk()
window.geometry("1093x637")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 637,
    width = 1093,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    721.0,
    637.0,
    fill="#C4E0A6",
    outline="")

canvas.create_rectangle(
    711.0,
    286.0,
    721.0,
    1189.000045418732,
    fill="#63BD03",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    910.0,
    212.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#74C38C",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 16)  # Увеличиваем шрифт
)
entry_1.place(
    x=779.5,
    y=195.0,
    width=261.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    910.5,
    361.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#73C38B",
    fg="#000716",
    highlightthickness=0,
    show="*",
    font=("Arial", 16)  # Увеличиваем шрифт
)
entry_2.place(
    x=780.0,
    y=340.0,
    width=261.0,
    height=43.0
)

canvas.create_text(
    782.0,
    308.0,
    anchor="nw",
    text="Password\n",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=check_credentials,
    relief="flat"
)
button_1.place(
    x=819.0,
    y=451.0,
    width=182.0863037109375,
    height=51.0
)

canvas.create_rectangle(
    710.7630004882812,
    -9.999913215637207,
    720.9999999884599,
    636.9999647140503,
    fill="#63BD03",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    320.0,
    296.0,
    image=image_image_1
)

canvas.create_text(
    782.0,
    160.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    909.0,
    114.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    150,
    485.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    599.0,
    520.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    591.0,
    123.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    397.0,
    477.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    125.0000011920929,
    140.99999856948853,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    638.0,
    357.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    339.0,
    113.0,
    image=image_image_9
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_registration,
    relief="flat"
)
button_2.place(
    x=917.0,
    y=583.0,
    width=160.0,
    height=35.0
)

# Bind the Enter key to the check_credentials function
window.bind('<Return>', check_credentials)

window.resizable(False, False)
window.mainloop()