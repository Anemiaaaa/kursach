from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from tkinter import Frame, Label

class GUI:
    def __init__(self, root, assets_path):
        self.root = root
        self.assets_path = assets_path
        self.setup_window()
        self.setup_canvas()
        self.setup_widgets()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def setup_window(self):
        self.root.geometry("762x637")
        self.root.configure(bg="#C4E0A6")

    def setup_canvas(self):
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
        self.canvas.create_rectangle(
            -2.0,
            123.0,
            761.9999901050287,
            125.99999999027409,
            fill="#000000",
            outline=""
        )
        self.canvas.create_rectangle(
            1.0,
            375.0,
            764.9999901050287,
            377.9999999902741,
            fill="#000000",
            outline=""
        )

    def setup_widgets(self):
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(231.0, 71.0, image=self.image_image_1)

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(631.5, 70, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#74C38C", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=581.0, y=49.0, width=101.0, height=43.0)

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.canvas.create_image(608.0, 32.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.canvas.create_image(152.0, 500.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.canvas.create_image(154.0, 256.0, image=self.image_image_4)

        self.create_buttons()

    def create_buttons(self):
        button_images = [
            "button_1.png", "button_2.png", "button_3.png", "button_4.png",
            "button_5.png", "button_6.png", "button_7.png", "button_8.png",
            "button_9.png", "button_10.png", "button_11.png", "button_12.png"
        ]
        button_positions = [
            (629.0, 516.0), (489.0, 516.0), (349.0, 516.0), (629.0, 408.0),
            (489.0, 408.0), (349.0, 408.0), (629.0, 253.0), (489.0, 253.0),
            (349.0, 253.0), (629.0, 145.0), (489.0, 145.0), (349.0, 145.0)
        ]

        for image, position in zip(button_images, button_positions):
            button_image = PhotoImage(file=self.relative_to_assets(image))
            button = Button(
                image=button_image,
                borderwidth=0,
                highlightthickness=0,
                command=lambda img=image: self.button_clicked(img),
                relief="flat"
            )
            button.image = button_image  # Сохраняем ссылку на изображение
            button.place(x=position[0], y=position[1], width=86.0, height=89.0)

    def button_clicked(self, image):
        print(f"{image} clicked")

if __name__ == "__main__":
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\amiri\PycharmProjects\kursach\frames\frame categories")

    root = Tk()
    gui = GUI(root, ASSETS_PATH)
    root.resizable(False, False)
    root.mainloop()
