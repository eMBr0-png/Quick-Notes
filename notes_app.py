import tkinter as tk
from tkinter import messagebox

class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Командний менеджер нотаток")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
