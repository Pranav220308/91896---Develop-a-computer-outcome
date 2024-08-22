from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
#start the program running
def main():
    #Start the GUI
    button_setup()
    main_window.mainloop()



main_window =Tk() 
main_window.title('Julies Party Hire')
main_window.geometry('640x340')













def saving_details():
    try:
        with open("customerdetails.txt", "w") as party_details:
            # Assuming customer_name, item, and entry_amount are Tkinter Entry widgets
            # Use .get() method to retrieve the input values
            
            # Format the data to be written to the file
            data = f"Customer Name: {customer_name.get()}\n"
            data += f"Item: {item.get()}\n"
            data += f"Amount: {entry_amount.get()}\n"
            
            # Write the formatted data to the file
            party_details.write(data)
            
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")



def combo(event):

    myLabel = Label(main_window, text="")

customer_name = Entry(main_window)
customer_name.grid(column=1, row=0)
items = [
    "Spoon",
    "Forks",
    "Party Plates",
    "Serviettes",
]
item = ttk.Combobox(main_window, value=items)
item.current(0)
item.bind("<<ComboboxSelected>>", combo)
item.grid(column=1, row=1)
entry_amount = Entry(main_window)
entry_amount.grid(column=1, row=2)
delete_item = Entry(main_window)
delete_item.grid(column=3,row=2,sticky=E)
main()