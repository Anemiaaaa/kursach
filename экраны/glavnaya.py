import subprocess
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from экраны.istoria import TransactionManager

class Application(Frame):
    def __init__(self, frame, assets_path, logged_in_user):
        super().__init__(frame)
        self.frame = frame
        self.assets_path = assets_path
        self.logged_in_user = logged_in_user
        self.transaction_manager = TransactionManager(r'C:\Users\amiri\PycharmProjects\kursach\экраны\users.db')  # Initialize TransactionManager
        self.current_balance = self.transaction_manager.calculate_balance(
            self.transaction_manager.fetch_transactions_by_user(self.logged_in_user)
        )
        self.setup_window()
        self.setup_canvas()
        self.setup_buttons()
        self.setup_entries()
        self.setup_images()
        self.update_balance_entry()  # Update the balance entry

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def setup_window(self):
        self.frame.configure(bg="#C4E0A6")

    def open_RashodCategory_window(self):
        subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\RashodCategory.py"])

    def open_DohodCategory_window(self):
        subprocess.Popen(["python", r"C:\Users\amiri\PycharmProjects\kursach\экраны\DohodCategory.py"])

    def setup_canvas(self):
        self.canvas = Canvas(
            self.frame,
            bg="#C4E0A6",
            height=637,
            width=762,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

    def setup_buttons(self):
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.frame,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_RashodCategory_window,
            relief="flat"
        )
        self.button_1.place(x=43.0, y=263.0, width=302.0, height=85.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.frame,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_DohodCategory_window,
            relief="flat"
        )
        self.button_2.place(x=419.0, y=263.0, width=302.0, height=85.0)

    def setup_entries(self):
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(388.0, 182.0, image=self.entry_image_1 )
        self.entry_1 = Entry(
            self.frame,
            bd=0,
            bg="#74C38C",
            fg="#000716",
            highlightthickness=0,
            font = ("Arial", 22),
            justify='center'
        )
        self.entry_1.config(state='readonly', readonlybackground="#74C38C")
        self.entry_1.place(x=298.0, y=158.0, width=180.0, height=46.0)

    def setup_images(self):
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(193.0, 70.0, image=self.image_image_1)

        self.canvas.create_rectangle(
            -2.0,
            123.0,
            761.9999901050287,
            125.99999999027409,
            fill="#000000",
            outline=""
        )

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.canvas.create_image(161.0, 180.0, image=self.image_image_2)

    def update_balance_entry(self):
        self.entry_1.config(state='normal')
        self.entry_1.delete(0, 'end')
        self.entry_1.insert(0, str(self.current_balance))
        self.entry_1.config(state='readonly', readonlybackground="#74C38C")