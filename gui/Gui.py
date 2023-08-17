import tkinter as tk
from tkinter import *
from tkinter import ttk


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        transForm = (700, 500)
        self.geometry(f"{transForm[0]}{transForm[1]}")
        self.resizable(True, True)
