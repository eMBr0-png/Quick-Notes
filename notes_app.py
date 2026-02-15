import tkinter as tk
from tkinter import messagebox
class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Командний менеджер нотаток")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
# --- Інтерфейс ---
        self.label = tk.Label(root, text="Напишіть нотатку нижче:", bg="#f0f0f0", font=("Arial", 10, "bold"))
        self.label.pack(pady=(20, 5))

        # Поле введення
        self.entry = tk.Entry(root, width=35, font=("Arial", 12), bd=2)
        self.entry.pack(pady=5, padx=20)
        # Дозволяємо додавати нотатку натисканням Enter
        self.entry.bind('<Return>', lambda event: self.add_note())

        # Кнопка додавання
        self.add_button = tk.Button(root, text="➕ Додати нотатку", command=self.add_note, 
                                   bg="#0f073f", fg="white", font=("Arial", 10, "bold"), width=20)
        self.add_button.pack(pady=10)

        # Список нотаток
        self.listbox = tk.Listbox(root, width=40, height=12, font=("Arial", 11), selectmode=tk.SINGLE)
        self.listbox.pack(pady=10, padx=20)

        # Кнопка видалення (Завдання 2)
        self.delete_button = tk.Button(root, text="🗑 Видалити обране", command=self.delete_note, 
                                      bg="#3bbec7", fg="white", width=20)
        self.delete_button.pack(pady=5)

        # Кнопка очищення (Завдання 3)
        self.clear_button = tk.Button(root, text="🧹 Очистити все", command=self.clear_all, 
                                     bg="#2196f3", fg="white", width=20)
        self.clear_button.pack(pady=5)