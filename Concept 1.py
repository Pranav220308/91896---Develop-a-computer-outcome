#Date: 17/06/2024
#AUthor: Pranav Kumar
#Purpose: To create a GUI which allows the user to enter details, append their details and allows them to quit the program. 

#Create the GUI
from tkinter import *
main_window = Tk()
main_window.geometry("600x120")

#Quit the program
def quit():
    main_window.destroy()

#Create the buttons and labels
    Button(main_window,command=quit, text="Quit",bg="#ba2106",fg = "#FFFFFF",width=12) .grid(column=12, row=4, sticky=E)




#Start the program running
def main():
    main_window.mainloop()
main()