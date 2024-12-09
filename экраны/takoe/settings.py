from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class Application:
    def __init__(self, root):
        self.root = root
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path(r"C:\Users\amiri\PycharmProjects\kursach\frames\frame settings")
        self.setup_ui()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

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
        self.canvas.create_rectangle(0.0, 125.0, 762.0, 445.0, fill="#74C38C", outline="")

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(229.5, 371.5, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#8FEAAB", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=154.0, y=350.0, width=151.0, height=43.0)

        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(225.0, 328.0, image=self.image_image_1)

        self.canvas.create_rectangle(-2.0, 123.0, 761.9999901050287, 125.99999999027409, fill="#000000", outline="")
        self.canvas.create_rectangle(-2.0, 443.0, 761.9999901050287, 445.9999999902741, fill="#000000", outline="")

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(229.5, 256.5, image=self.entry_image_3)
        self.entry_3 = Entry(bd=0, bg="#8FEAAB", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=154.0, y=235.0, width=151.0, height=43.0)

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(222.0, 213.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(181.0, 67.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(384.0, 163.0, image=self.image_image_4)

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(x=389.0, y=493.0, width=299.0, height=79.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(x=72.0, y=493.0, width=299.0, height=79.0)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(x=427.0, y=267.0, width=190.0, height=58.0)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(x=522.0, y=38.0, width=187.0, height=62.33333206176758)

        self.root.resizable(False, False)

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
