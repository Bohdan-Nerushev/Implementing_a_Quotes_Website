

import tkinter as tk
from tkinter import messagebox
from threading import Thread
from pathlib import Path
import shutil

def verzeichnisse(schlax_p, schlax_k, doc_type, status_label):
    try:
        # Створення об'єкту Path для цільової директорії
        directory = Path(schlax_k)
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)

        # Створення об'єкту Path для початкової директорії
        directory_1 = Path(schlax_p)

        if not directory_1.exists():
            raise FileNotFoundError(f"Директорія {schlax_p} не існує")

        # Виведення переліку всіх файлів та піддиректорій
        for path in directory_1.iterdir():
            if path.is_file() and path.suffix.lower() == f'.{doc_type.lower()}':
                # Вихідний і цільовий файли для копіювання
                source = path
                destination = directory / path.name

                # Копіювання файлу
                shutil.copy(source, destination)

            # Запускаємо рекурсію для глибокого пошуку
            if path.is_dir():
                verzeichnisse(path, directory, doc_type, status_label)

        status_label.config(text=f"{doc_type.upper()} файли відсортовано", bg="green")

    except FileNotFoundError as e:
        status_label.config(text="Виникла помилка", bg="red")
        messagebox.showerror("Помилка", f"Помилка: {e}")
    except PermissionError as e:
        status_label.config(text="Виникла помилка", bg="red")
        messagebox.showerror("Помилка", f"Помилка: Немає дозволу на доступ: {e}")
    except Exception as e:
        status_label.config(text="Виникла помилка", bg="red")
        messagebox.showerror("Помилка", f"Інша помилка: {e}")

def start_sorting():
    schlax_p = entry_source.get()
    schlax_k = entry_dest.get()
    doc_type = entry_doc_type.get()
    status_label.config(text="", bg="light yellow")
    thread = Thread(target=verzeichnisse, args=(schlax_p, schlax_k, doc_type, status_label))
    thread.start()

root = tk.Tk()
root.title("Сортування файлів")
root.geometry("400x400")
root.config(bg="light yellow")

# Поле для введення шляху до файлів
label_source = tk.Label(root, text="Введіть шлях до папки для сортування", bg="light yellow")
label_source.pack(pady=5)

entry_source = tk.Entry(root, width=50)
entry_source.pack(pady=5)

# Поле для введення шляху до цільової директорії
label_dest = tk.Label(root, text="Введіть папку у яку буде завантажено результат", bg="light yellow")
label_dest.pack(pady=5)

entry_dest = tk.Entry(root, width=50)
entry_dest.pack(pady=5)

# Поле для введення типу документів
label_doc_type = tk.Label(root, text="Введіть тип документу (розширення)", bg="light yellow")
label_doc_type.pack(pady=5)

entry_doc_type = tk.Entry(root, width=20)
entry_doc_type.pack(pady=5)

# Кнопка для запуску сортування
button_sort = tk.Button(root, text="Відсортувати", command=start_sorting)
button_sort.pack(pady=20)

# Статус
status_label = tk.Label(root, text="", bg="light yellow")
status_label.pack(pady=20)

root.mainloop()
