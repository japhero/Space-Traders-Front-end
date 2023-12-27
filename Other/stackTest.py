import tkinter as tk
from tkinter import ttk
# Default imports 

root = tk.Tk()
root.geometry("720x550")
root.overrideredirect(True)


root.grid_rowconfigure(1, weight=10)
root.grid_columnconfigure(1, weight=1)


titleFrame = tk.Frame(root,bd=3, relief=tk.RAISED)
titleFrame.grid(row=0, column=0, sticky="nsew",columnspan=2)
titleFrame.grid_columnconfigure(3, weight=1)

appTitle = ttk.Label(titleFrame, text="Sample Tkinter Structuring", font=('Times', '20'))
appTitle.grid(row=0, column=0, sticky="w")

appClose = tk.Button(titleFrame, text=" X ", command=root.destroy,anchor="e")
appClose.grid(row=0, column=3, sticky="e")

tabs = ttk.Notebook(root)
tabs.grid(row=1, column=1, sticky="nsew")

tab1 = ttk.Frame(tabs)
tabs.add(tab1, text="Tab 1")
tab1.grid_rowconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

buttonFrame = tk.Frame(tab1,bd=3, relief=tk.RAISED)
buttonFrame.grid(row=0, column=1, sticky="nsew")

shipInfoFrame = ttk.Scrollbar(tab1,orient="horizontal")
shipInfoFrame.grid(row=1, column=1, sticky="nsew")

for x in range(5):
    button = ttk.Button(buttonFrame, text="Button")
    button.grid(row=x, column=0, sticky="nsew")

root.mainloop()