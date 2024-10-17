import tkinter as tk
from tkinter import messagebox, ttk
from threading import Thread
from pathlib import Path
import shutil

# Dictionary for translations into different languages
translations = {
    "en": {
        "title": "File Sorting",
        "enter_source": "Enter the folder path for sorting",
        "enter_dest": "Enter the destination folder",
        "enter_doc_type": "Enter the document type (extension)",
        "sort_button": "Sort",
        "sorted": "{} files sorted",
        "error": "Error",
        "file_not_found": "Directory {} not found",
        "permission_error": "Permission denied: {}",
        "other_error": "Other error: {}"
    },
    "de": {
        "title": "Dateisortierung",
        "enter_source": "Geben Sie den Pfad zum Ordner ein",
        "enter_dest": "Geben Sie den Zielordner ein",
        "enter_doc_type": "Geben Sie den Dokumenttyp (Erweiterung) ein",
        "sort_button": "Sortieren",
        "sorted": "{} Dateien sortiert",
        "error": "Fehler",
        "file_not_found": "Verzeichnis {} nicht gefunden",
        "permission_error": "Zugriff verweigert: {}",
        "other_error": "Anderer Fehler: {}"
    },
    "uk": {
        "title": "Сортування файлів",
        "enter_source": "Введіть шлях до папки для сортування",
        "enter_dest": "Введіть папку у яку буде завантажено результат",
        "enter_doc_type": "Введіть тип документу (розширення)",
        "sort_button": "Відсортувати",
        "sorted": "{} файли відсортовано",
        "error": "Помилка",
        "file_not_found": "Директорія {} не існує",
        "permission_error": "Немає дозволу на доступ: {}",
        "other_error": "Інша помилка: {}"
    }
}

# Function to change the interface language
def change_language(language):
    global current_language
    current_language = language
    update_texts()

# Update interface texts according to the selected language
def update_texts():
    root.title(translations[current_language]["title"])
    label_source.config(text=translations[current_language]["enter_source"])
    label_dest.config(text=translations[current_language]["enter_dest"])
    label_doc_type.config(text=translations[current_language]["enter_doc_type"])
    button_sort.config(text=translations[current_language]["sort_button"])

# Function to sort files
def verzeichnisse(schlax_p, schlax_k, doc_type, status_label):
    try:
        directory = Path(schlax_k)
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)

        directory_1 = Path(schlax_p)

        if not directory_1.exists():
            raise FileNotFoundError(translations[current_language]["file_not_found"].format(schlax_p))

        for path in directory_1.iterdir():
            if path.is_file() and path.suffix.lower() == f'.{doc_type.lower()}':
                source = path
                destination = directory / path.name
                shutil.copy(source, destination)

            if path.is_dir():
                verzeichnisse(path, directory, doc_type, status_label)

        status_label.config(text=translations[current_language]["sorted"].format(doc_type.upper()), bg="green")

    except FileNotFoundError as e:
        status_label.config(text=translations[current_language]["error"], bg="red")
        messagebox.showerror(translations[current_language]["error"], str(e))
    except PermissionError as e:
        status_label.config(text=translations[current_language]["error"], bg="red")
        messagebox.showerror(translations[current_language]["error"], translations[current_language]["permission_error"].format(e))
    except Exception as e:
        status_label.config(text=translations[current_language]["error"], bg="red")
        messagebox.showerror(translations[current_language]["error"], translations[current_language]["other_error"].format(e))

def start_sorting():
    schlax_p = entry_source.get()
    schlax_k = entry_dest.get()
    doc_type = entry_doc_type.get()
    status_label.config(text="", bg="light yellow")
    thread = Thread(target=verzeichnisse, args=(schlax_p, schlax_k, doc_type, status_label))
    thread.start()

# Create the main window
root = tk.Tk()
current_language = "en"  # Default language is English
root.title(translations[current_language]["title"])
root.geometry("400x400")
root.config(bg="light yellow")

# Add a menu for language selection
menu_bar = tk.Menu(root)
language_menu = tk.Menu(menu_bar, tearoff=0)
for lang, lang_name in [("en", "English"), ("de", "Deutsch"), ("uk", "Українська")]:
    language_menu.add_command(label=lang_name, command=lambda l=lang: change_language(l))
menu_bar.add_cascade(label="Language", menu=language_menu)
root.config(menu=menu_bar)

# Field for entering the path to the files
label_source = tk.Label(root, text=translations[current_language]["enter_source"], bg="light yellow")
label_source.pack(pady=5)

entry_source = tk.Entry(root, width=50)
entry_source.pack(pady=5)

# Field for entering the destination directory
label_dest = tk.Label(root, text=translations[current_language]["enter_dest"], bg="light yellow")
label_dest.pack(pady=5)

entry_dest = tk.Entry(root, width=50)
entry_dest.pack(pady=5)

# Field for entering document types
label_doc_type = tk.Label(root, text=translations[current_language]["enter_doc_type"], bg="light yellow")
label_doc_type.pack(pady=5)

entry_doc_type = tk.Entry(root, width=20)
entry_doc_type.pack(pady=5)

# Button to start sorting
button_sort = tk.Button(root, text=translations[current_language]["sort_button"], command=start_sorting)
button_sort.pack(pady=20)

# Status label
status_label = tk.Label(root, text="", bg="light yellow")
status_label.pack(pady=20)

root.mainloop()


