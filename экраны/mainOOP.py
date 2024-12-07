import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage


class MainWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1093x637")
        self.window.configure(bg="#C4E0A6")
        self.window.resizable(False, False)

        self.assets_path = Path(r"C:\Users\amiri\PycharmProjects\kursach\frames\frame main")
        self.canvas = Canvas(
            self.window,
            bg="#C4E0A6",
            height=637,
            width=1093,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self._create_ui()

    def relative_to_assets(self, path: str) -> Path:
        """Возвращает полный путь к файлу в папке с ресурсами."""
        return self.assets_path / Path(path)

    def open_window(self, script_path: str):
        """Открывает новое окно через выполнение другого скрипта."""
        subprocess.Popen(["python", script_path])

    def _create_ui(self):
        """Создает пользовательский интерфейс."""
        # Разделяющая линия
        self.canvas.create_rectangle(
            -1.0, 121.0, 314.9999960580535, 123.99999995112421,
            fill="#000000", outline=""
        )

        # Кнопка настроек
        self._create_button(
            x=25.0, y=568.0, width=50.0, height=51.0,
            image="button_1.png",
            command=lambda: self.open_window(r"C:\Users\amiri\PycharmProjects\kursach\экраны\settings.py")
        )

        # Кнопка категорий
        self._create_button(
            x=27.0, y=445.000244140625, width=269.0, height=61.999725341796875,
            image="button_2.png",
            command=lambda: self.open_window(r"C:\Users\amiri\PycharmProjects\kursach\экраны\categories.py")
        )

        # Кнопка с неизвестным действием
        self._create_button(
            x=25.0, y=356.0, width=266.1428527832031, height=68.0,
            image="button_3.png",
            command=lambda: print("button_3 clicked")
        )

        # Кнопка истории
        self._create_button(
            x=27.0, y=265.0, width=264.0, height=72.99993896484375,
            image="button_4.png",
            command=lambda: self.open_window(r"C:\Users\amiri\PycharmProjects\kursach\экраны\istoria.py")
        )

        # Кнопка главного окна
        self._create_button(
            x=24.0, y=181.0, width=267.9638671875, height=64.0,
            image="button_5.png",
            command=lambda: self.open_window(r"C:\Users\amiri\PycharmProjects\kursach\экраны\glavnaya.py")
        )

        # Кнопка заголовка
        self._create_button(
            x=0.0, y=0.0, width=302.0, height=116.0,
            image="button_6.png",
            command=lambda: print("button_6 clicked")
        )

        # Разделительная линия справа
        self.canvas.create_rectangle(
            307.0, -10.0, 317.9999999884383, 637.0000110260298,
            fill="#63BD03", outline=""
        )

    def _create_button(self, x, y, width, height, image, command):
        """Создает кнопку с заданными параметрами."""
        button_image = PhotoImage(file=self.relative_to_assets(image))
        button = Button(
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat"
        )
        button.image = button_image  # Чтобы изображение не было удалено сборщиком мусора
        button.place(x=x, y=y, width=width, height=height)

    def run(self):
        """Запускает главное окно."""
        self.window.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.run()
