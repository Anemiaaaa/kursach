import subprocess
from pathlib import Path
from tkinter import *
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\amiri\PycharmProjects\kursach\frames\frame main")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def open_glavnaya_window():
    subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\glavnaya.py", logged_in_user])

def open_settings_window():
    subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\settings.py"])

def open_istoria_window():
    subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\istoria.py", logged_in_user])

def open_categories_window():
    subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\categories.py"])

logged_in_user = sys.argv[1] if len(sys.argv) > 1 else None


window = Tk()
window.geometry("1093x637")
window.configure(bg="#C4E0A6")

canvas = Canvas(
    window,
    bg="#C4E0A6",
    height=637,
    width=1093,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    -1.0,
    121.0,
    314.9999960580535,
    123.99999995112421,
    fill="#000000",
    outline=""
)

# фрэйм куда будем добавлять все виджеты
frame = Frame(window, bg="#000000", width=775, height=637)
frame.place(x=318.0, y=0.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_settings_window,
    relief="flat"
)
button_1.place(
    x=25.0,
    y=568.0,
    width=50.0,
    height=51.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_categories_window,
    relief="flat"
)
button_2.place(
    x=27.0,
    y=445.000244140625,
    width=269.0,
    height=61.999725341796875
)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=25.0,
    y=356.0,
    width=266.1428527832031,
    height=68.0
)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_istoria_window,
    relief="flat"
)
button_4.place(
    x=27.0,
    y=265.0,
    width=264.0,
    height=72.99993896484375
)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=open_glavnaya_window,
    relief="flat"
)
button_5.place(
    x=24.0,
    y=181.0,
    width=267.9638671875,
    height=64.0
)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=0.0,
    y=0.0,
    width=302.0,
    height=116.0
)

canvas.create_rectangle(
    307.0,
    -10.0,
    317.9999999884383,
    637.0000110260298,
    fill="#63BD03",
    outline=""
)


window.resizable(False, False)
window.mainloop()