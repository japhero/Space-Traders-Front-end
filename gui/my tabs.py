from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("720x550")
root.overrideredirect(True)

root.grid_rowconfigure(1, weight=10)
root.grid_columnconfigure(1, weight=1)

titleFrame = Frame(root, bd=3, relief=RAISED)
titleFrame.grid(row=0, column=0, sticky="nsew", columnspan=2)
titleFrame.grid_columnconfigure(3, weight=1)

appTitle = Label(titleFrame, text="Sample Tkinter Structuring", font=('Times', '20'))
appTitle.grid(row=0, column=0, sticky="w")

appClose = Button(titleFrame, text=" X ", command=root.destroy, anchor="e")
appClose.grid(row=0, column=3, sticky="e")

tabs = ttk.Notebook(root)
tabs.grid(row=1, column=1, sticky="nsew")

tab1 = Frame(tabs)
tabs.add(tab1, text="Tab 1")
tab1.grid_rowconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

buttonFrame = Frame(tab1, bd=3, relief=RAISED)
buttonFrame.grid(row=0, column=0, sticky="nsew")

infoScrollBar = Scrollbar(tab1, orient="vertical")
infoScrollBar.grid(row=0, column=2, sticky="nsew")

shipInfoFrame = Frame(tab1, bd=3, relief=RAISED)
shipInfoFrame.grid(row=0, column=1, sticky="nsew")
shipInfoFrame.grid_columnconfigure([0], weight=1)

for x in range(40):
    shipTestLabel = Label(shipInfoFrame, text="Ship Info", font=('Times', '20'), anchor="w")
    shipTestLabel.pack(side=TOP, fill="x")

for x in range(5):
    button = Button(buttonFrame, text="Button")
    button.grid(row=x, column=0, sticky="nsew")

root.mainloop()
