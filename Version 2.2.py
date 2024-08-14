########################################################################
###This program is used to store each customers details. ###
########################################################################

#import tkinter so we can make a GUI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random


#start the program running
def main():
    #Start the GUI
    button_setup()
    main_window.mainloop()


main_window = Tk()
main_window.title('Julies Store')
main_window.geometry('640x340')

#bgtest = PhotoImage(file = "partyimg.png")


#Show image using label
#mybg = Label(main_window, image=bgtest)
#mybg.place(x=0, y=0)
#quit subroutine
def quit():
    response = messagebox.askyesno("Quit", "Are you sure you want to quit?")
    if response == 1:
        main_window.destroy()


#print all customer details
def print_customer_details():
    name_count = 0
    #Create column headings
    Label(main_window, font=("Helvetica 10 bold"),
          text="Reciept Number").grid(column=0, row=7, pady=25)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Full Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Item Hired ").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Amount Hired").grid(column=3, row=7)
    #add each item in the list into its own row
    while name_count < counters['total_entries']:
        Label(main_window, text=name_count).grid(column=0, row=name_count + 8)
        Label(main_window,
              text=(customer_details[name_count][0])).grid(column=1,
                                                           row=name_count + 8)
        Label(main_window,
              text=(customer_details[name_count][1])).grid(column=2,
                                                           row=name_count + 8)
        Label(main_window,
              text=(customer_details[name_count][2])).grid(column=3,
                                                           row=name_count + 8)
        name_count += 1
        counters['name_count'] = name_count


#Check the inputs are all valid
def check_inputs():
    input_check = 0
    #Program checks if name is not blank, if blank then it outputs a error
    if (entry_customer_name.get().isalpha()) == False:
        messagebox.showerror("Error", "Please enter a valid name")
    else:
        input_check = 1
    if len(entry_customer_name.get()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=0)
        input_check = 1
    #Program checks if item is not blank, if blank then it outputs a error
    if (item.get().isalpha()):
        if len(item.get()) == 0:
            Label(main_window, fg="red", text="Required").grid(column=2, row=1)
            input_check = 1
    #Program checks if the item amount is not blank and that the amount enetered is between 1-500
    if (entry_amount.get().isdigit()):
        if int(entry_amount.get()) < 1 or int(entry_amount.get()) > 500:
            Label(main_window, fg="red", text="1-500 only").grid(column=2,
                                                                 row=2)
            input_check = 1
    else:
        Label(main_window, fg="red", text="1-500 only").grid(column=2, row=2)
        input_check = 1
    if (entry_receipt.get().isdigit()):
        if len(entry_receipt.get()) == 0:
            Label(main_window, fg="red", text="Required").grid(column=2, row=3)
            input_check = 1
    
    if input_check == 0: append_name()


#add more customers to the list.
def append_name():
    #append each item to its own area of the list
    customer_details.append(
        [entry_customer_name.get(),
         item.get(),
         entry_amount.get()])
    #clear the boxes
    entry_customer_name.delete(0, 'end')
    item.delete(0, 'end')
    entry_amount.delete(0, 'end')
    counters['total_entries'] += 1


#Function for deleting a row from the list
def delete_row():
    #find which row is to be deleted and delete it
    del customer_details[int(delete_item.get())]
    counters['total_entries'] -= 1
    name_count = counters['name_count']
    delete_item.delete(0, 'end')
    #clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0, row=name_count + 7)
    Label(main_window, text="       ").grid(column=1, row=name_count + 7)
    Label(main_window, text="       ").grid(column=2, row=name_count + 7)
    Label(main_window, text="       ").grid(column=3, row=name_count + 7)
    Label(main_window, text="       ").grid(column=4, row=name_count + 7)
    #print all the items in the list
    print_customer_details()


#create the buttons and labels


#create combobox for items
def combo(event):

    myLabel = Label(main_window, text="")


items = [
    "Spoon",
    "Forks",
    "Party Plates",
    "Serviettes",
]

clicked = StringVar()
clicked.set(items[0])


def button_setup():
    #create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location
    Label(main_window,
          text="Customer Full Name",
          font=("Bahnschrift", 12, "bold"),
          bg='#b4c8e4').grid(column=0, row=0, sticky=E)
    Label(main_window,
          text="Item Hired",
          font=("Bahnschrift", 12, "bold"),
          bg='#b4c8e4').grid(column=0, row=1, sticky=E)
    Button(main_window,
           text="Quit",
           font=("Bahnschrift", 12, "bold"),
           command=quit,
           bg="#ba2106",
           fg="#FFFFFF",
           width=12).grid(column=9, row=0, sticky=E)
    Label(main_window,
          text="Receipt",
          font=("Bahnschrift", 12, "bold"),
          bg='#b4c8e4').grid(column=0, row=5, sticky=E)
    Label(main_window,
          text="Hired Item Quantity",
          font=("Bahnschrift", 12, "bold"),
          bg='#b4c8e4').grid(column=0, row=2, sticky=E)
    Button(main_window,
           text="Submit",
           font=("Bahnschrift", 12, "bold"),
           command=check_inputs).grid(column=9, row=1, pady=10)
    Button(main_window,
           text="Print Details",
           font=("Bahnschrift", 12, "bold"),
           command=print_customer_details,
           width=12).grid(column=9,
                          row=1,
                          columnspan=9,
                          rowspan=9,
                          pady=6,
                          sticky=E)
    Button(main_window,
           text="Delete Receipt",
           font=("Bahnschrift", 12, "bold"),
           command=delete_row,
           width=12).grid(column=8, row=7, rowspan=8, columnspan=8, sticky=E)


#create empty list for customer details and empty variable for entries in the list
counters = {'total_entries': 0, 'name_count': 0}
customer_details = []
entry_customer_name = Entry(main_window)
entry_customer_name.grid(column=1, row=0)
#item = Entry(main_window)
#item.grid(column=1, row=1)
item = ttk.Combobox(main_window, value=items)
item.current(0)
item.bind("<<ComboboxSelected>>", combo)
item.grid(column=1,row=1)
entry_amount = Entry(main_window)
entry_amount.grid(column=1, row=2)
entry_receipt = Entry(main_window)
entry_receipt.grid(column=1, row=5, pady=25)
delete_item = Entry(main_window)
delete_item.grid(column=3, row=7)
main()
