from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage

class Grafics(Frame):
    def __init__(self, parent, assets_path, logged_in_user):
        super().__init__(parent)  # Указываем родителя в базовом классе
        self.assets_path = assets_path
        self.logged_in_user = logged_in_user
        self.images = {}  # Словарь для хранения изображений
        self.create_widgets()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def create_widgets(self):
        self.canvas = Canvas(
            self,
            bg="#C4E0A6",
            height=637,
            width=762,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            -2.0,
            123.0,
            761.9999901050287,
            125.99999999027409,
            fill="#000000",
            outline=""
        )

        self.images["image_1"] = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(381.0, 188.0, image=self.images["image_1"])

        self.images["image_2"] = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.canvas.create_image(196.0, 68.0, image=self.images["image_2"])

        self.images["button_1"] = PhotoImage(file=self.relative_to_assets("button_1.png"))
        Button(
            self,
            image=self.images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        ).place(x=43.0, y=158.0, width=193.0, height=60.0)

        self.images["button_2"] = PhotoImage(file=self.relative_to_assets("button_2.png"))
        Button(
            self,
            image=self.images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        ).place(x=284.0, y=159.0, width=193.0, height=60.0)

        self.images["button_3"] = PhotoImage(file=self.relative_to_assets("button_3.png"))
        Button(
            self,
            image=self.images["button_3"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        ).place(x=526.0, y=158.0, width=191.0, height=60.0)

        self.canvas.create_rectangle(
            28.0,
            255.0,
            731.0,
            613.0,
            fill="#000000",
            outline=""
        )
