#button icon test 
import tkinter as tk
from tkinter import PhotoImage
root = tk.Tk()
root.title("test")


root.geometry('700x300')


def quit():
    root.destroy()

click_btn = PhotoImage(file='delbuttonicon.png')
img_label = tk.Label(root, image=click_btn)
img_label.pack()



root.mainloop()
