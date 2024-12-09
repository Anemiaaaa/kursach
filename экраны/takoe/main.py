import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Frame, Button, PhotoImage
import sys


class App:
    def __init__(self, root, assets_path, logged_in_user):
        self.root = root
        self.assets_path = assets_path
        self.logged_in_user = logged_in_user
        self.setup_window()
        self.setup_canvas()
        self.setup_frame()
        self.setup_buttons()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def setup_window(self):
        self.root.geometry("1093x637")
        self.root.configure(bg="#C4E0A6")

    def setup_canvas(self):
        self.canvas = Canvas(
            self.root,
            bg="#C4E0A6",
            height=637,
            width=1093,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            -1.0,
            121.0,
            314.9999960580535,
            123.99999995112421,
            fill="#000000",
            outline=""
        )
        self.canvas.create_rectangle(
            307.0,
            -10.0,
            317.9999999884383,
            637.0000110260298,
            fill="#63BD03",
            outline=""
        )

    def setup_frame(self):
        self.frame = Frame(self.root, bg="#000000", width=775, height=637)
        self.frame.place(x=318.0, y=0.0)

    def setup_buttons(self):
        button_images = [
            ("button_1.png", self.open_settings_window, 25.0, 568.0, 50.0, 51.0),
            ("button_2.png", self.open_categories_window, 27.0, 445.0, 269.0, 62.0),
            ("button_3.png", lambda: print("button_3 clicked"), 25.0, 356.0, 266.0, 68.0),
            ("button_4.png", self.open_istoria_window, 27.0, 265.0, 264.0, 73.0),
            ("button_5.png", self.open_glavnaya_window, 24.0, 181.0, 268.0, 64.0),
            ("button_6.png", lambda: print("button_6 clicked"), 0.0, 0.0, 302.0, 116.0)
        ]

        for image, command, x, y, width, height in button_images:
            button_image = PhotoImage(file=self.relative_to_assets(image))
            button = Button(
                image=button_image,
                borderwidth=0,
                highlightthickness=0,
                command=command,
                relief="flat"
            )
            button.image = button_image  # Сохраняем ссылку на изображение
            button.place(x=x, y=y, width=width, height=height)

    def open_glavnaya_window(self):
        subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\glavnaya.py", self.logged_in_user])

    def open_settings_window(self):
        subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\settings.py"])

    def open_istoria_window(self):
        subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\istoria.py", self.logged_in_user])

    def open_categories_window(self):
        subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\categories.py"])


if __name__ == "__main__":
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\amiri\PycharmProjects\kursach\frames\frame main")

    logged_in_user = sys.argv[1] if len(sys.argv) > 1 else None

    root = Tk()
    app = App(root, ASSETS_PATH, logged_in_user)
    root.resizable(False, False)
    root.mainloop()
