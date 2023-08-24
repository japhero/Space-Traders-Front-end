import tkinter as tk
from tkinter import ttk


class GUI(tk.Tk):
    def __init__(self, transform):
        super().__init__()

        ## Setup
        self.overrideredirect(True)
        self.transform = transform
        self.geometry(f"{transform[0]}x{transform[1]}")
        self.resizable(True, True)

        ## Creating a container
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        ## Frames for the GUI
        self.frames = {}
        self.tabs = Tabs
        self.shipInfoTab = ShipInfoTab


class ShipInfoTab(ttk.Notebook):

    def __int__(self, parent, container):
        super().__init__(master=container)

        self.infoFrame = ttk.Frame(self)
        self.add(self.infoFrame, text="Ships")  # Add the frame to the tab

        self.infoFrame.grid_rowconfigure(0, weight=1)  # Make first info fill the whole frame vertically
        self.ships = []  # List of ship items to later update the info in the frame.

        self.infoFrame.grid(row=0, column=1, sticky="nsew")  # place the frame in the right corner of the tab


app = GUI((720, 550))
app.mainloop()
