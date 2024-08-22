#custom image background in tkinter test

import tkinter as tk
from tkinter import PhotoImage
root = tk.Tk()
root.title("test")
root.geometry("800x500")
image = PhotoImage(file="partyimg.png")
image_label = tk.Label(root, image=image)
image_label.pack()
root.mainloop()
