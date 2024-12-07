import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, Entry
from tkinter import ttk  # Для создания таблицы (Treeview)
from tkinter import font
from datetime import datetime
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\amiri\PycharmProjects\kursach\frames\frame istoria")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def fetch_transactions_by_user(username):
    """
    Получает список транзакций для текущего пользователя.
    """
    conn = sqlite3.connect(r'C:\Users\amiri\PycharmProjects\kursach\экраны\users.db')
    cursor = conn.cursor()

    # Получить ID пользователя по имени
    cursor.execute('SELECT id FROM Users WHERE username = ?', (username,))
    user_id = cursor.fetchone()

    if user_id:
        user_id = user_id[0]
        # Извлекаем транзакции только текущего пользователя, сортируя по дате в обратном порядке
        cursor.execute('''SELECT Transactions.id, Transactions.type, Transactions.amount, Transactions.date, Transactions.description
                          FROM Transactions
                          WHERE Transactions.user_id = ?
                          ORDER BY Transactions.date DESC''', (user_id,))
        transactions = cursor.fetchall()
    else:
        transactions = []

    conn.close()
    return transactions

def calculate_balance(transactions):
    """
    Вычисляет текущий баланс пользователя.
    """
    balance = 0
    for transaction in transactions:
        amount = transaction[2]
        if transaction[1] == 'expense':
            amount = -amount
        balance += amount
    return balance

def on_hover(event):
    """
    Показывает описание транзакции и баланс при наведении мыши на строку.
    """
    item = transactions_table.identify_row(event.y)
    if item:
        # Получаем данные строки
        values = transactions_table.item(item, "values")
        description = values[5]  # Индекс 5 - описание
        # ID транзакции из строки
        transaction_id = int(values[0])

        # Находим индекс транзакции в исходных данных
        for index, transaction in enumerate(transactions):
            if transaction[0] == transaction_id:  # Сравниваем ID
                # Вычисляем баланс до текущей транзакции
                balance = calculate_balance(transactions[:index + 1])
                tooltip_label.config(text=f"Описание: {description}\nБаланс: {balance}")
                break
    else:
        tooltip_label.config(text="")


def on_leave(event):
    """
    Скрывает описание при уходе мыши с строки.
    """
    tooltip_label.config(text="")

def format_datetime(datetime_str):
    """
    Форматирует строку даты и времени.
    Разделяет дату и время для отображения.
    """
    dt_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    date = dt_obj.strftime("%d.%m.%Y")
    time = dt_obj.strftime("%H:%M:%S")
    return date, time

def translate_type(transaction_type):
    """
    Переводит тип транзакции на русский язык.
    """
    if transaction_type == 'income':
        return 'Доход'
    elif transaction_type == 'expense':
        return 'Расход'
    return transaction_type

# Получаем текущего пользователя из аргументов командной строки
logged_in_user = sys.argv[1] if len(sys.argv) > 1 else None

# Инициализация окна
window = Tk()
window.geometry("762x637")
window.configure(bg="#C4E0A6")

# Добавляем название интерфейса и интерфейс баланса
canvas = Canvas(
    window,
    bg="#C4E0A6",
    height=637,
    width=762,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(-2.0, 123.0, 761.9999901050287, 125.99999999027409, fill="#000000", outline="")

# Заголовок "История"
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(196.0, 70.0, image=image_image_1)

# Поле для баланса
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(656.5, 69.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#74C38C", fg="#000716", highlightthickness=0, font=("Arial", 14))
entry_1.place(x=606.0, y=47.0, width=101.0, height=43.0)
entry_1.config(state='readonly', readonlybackground="#74C38C")  # Устанавливаем поле только для чтения и цвет фона

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(633.0, 28.0, image=image_image_2)

# Создаем таблицу для отображения транзакций
columns = ("ID", "Тип", "Сумма", "Дата", "Время", "Описание")
transactions_table = ttk.Treeview(window, columns=columns, show="headings", height=20)

# Настройка заголовков таблицы
transactions_table.heading("ID", text="ID")
transactions_table.heading("Тип", text="Тип")
transactions_table.heading("Сумма", text="Сумма")
transactions_table.heading("Дата", text="Дата")
transactions_table.heading("Время", text="Время")

# Настройка ширины колонок
transactions_table.column("ID", width=0, stretch=False)  # Скрываем колонку "ID"
transactions_table.column("Тип", width=150, anchor="center")
transactions_table.column("Сумма", width=150, anchor="center")
transactions_table.column("Дата", width=100, anchor="center")
transactions_table.column("Время", width=100, anchor="center")
transactions_table.column("Описание", width=0, stretch=False)  # Скрываем колонку "Описание"

# Увеличиваем шрифт таблицы
style = ttk.Style()
style.configure("Treeview", font=("Arial", 14), rowheight=28)
style.configure("Treeview.Heading", font=("Arial", 16, "bold"))

# Фильтруем транзакции по текущему пользователю
transactions = fetch_transactions_by_user(logged_in_user)
for transaction in transactions:
    transaction_id = transaction[0]
    transaction_type = translate_type(transaction[1])  # Переводим тип транзакции на русский
    amount = transaction[2]
    if transaction_type == 'Расход':
        amount = -amount  # Add minus sign for expenses
    date, time = format_datetime(transaction[3])  # Разделяем дату и время
    description = transaction[4]

    # Вставляем транзакцию в таблицу в начало
    transactions_table.insert("", 0, values=(transaction_id, transaction_type, amount, date, time, description))

# Вычисляем текущий баланс и выводим его в поле для баланса
current_balance = calculate_balance(transactions)
entry_1.config(state='normal')  # Разрешаем запись в поле
entry_1.insert(0, str(current_balance))
entry_1.config(state='readonly', readonlybackground="#74C38C")  # Устанавливаем поле только для чтения и цвет фона

# Размещение таблицы на интерфейсе
transactions_table.place(x=10, y=130, width=740, height=450)

# Добавляем метку для отображения описания при наведении
tooltip_label = ttk.Label(window, text="", background="#C4E0A6", font=("Arial", 12))
tooltip_label.place(x=10, y=590)

# Добавляем обработчики событий для показа и скрытия описания
transactions_table.bind("<Motion>", on_hover)
transactions_table.bind("<Leave>", on_leave)

window.resizable(False, False)
window.mainloop()