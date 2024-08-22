#combo box test
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Combobox Testing")
#Label(main_window, text="Item Hired",font=("Bahnschrift" ,12,"bold"),bg='#b4c8e4') .grid(column=0,row=1,sticky=E)
root.geometry("400x400")
#creates combo function
def combo(event):

  myLabel = Label(root, text="").pack()


items = [
    "Spoon",
    "Forks",
    "Party Plates",
    "Serviettes",
]

clicked = StringVar()
clicked.set(items[0])

myCombo = ttk.Combobox(root, value=items)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", combo)
myCombo.pack()
#Dropdown menu
#drop = OptionMenu(root, clicked, *items)
#drop.pack(pady=20)

root.mainloop()