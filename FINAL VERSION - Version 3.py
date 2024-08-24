########################################################################
###This program is used to store each customers details. ###
########################################################################

#import tkinter so we can make a GUI
import random
from tkinter import *
from tkinter import messagebox, ttk
import os


#start the program running
def main():
    #Start the GUI
    button_setup()
    main_window.mainloop()

main_window =Tk() 
main_window.title('Julies Party Hire')
main_window.geometry('692x390')
bgtest = PhotoImage(file = "purplepartybg2.png")

#Show image using label
mybg = Label(main_window, image=bgtest)
mybg.place(x=0, y=0)

#setup columnsizes

main_window.columnconfigure(0, weight=0, minsize=150)
main_window.columnconfigure(1, weight=0, minsize=150)
main_window.columnconfigure(2, weight=0, minsize=120)
main_window.columnconfigure(3, weight=0,pad=40,minsize=0)
main_window.columnconfigure(4, weight=0, minsize=100)
main_window.columnconfigure(5, weight=0, minsize=150)

#quit subroutine



def quit(): 
    response = messagebox.askyesno("Quit","Do you want to quit the program?")
    if response == 1:
        main_window.destroy()

#print all customer details 
def print_customer_details ():
    for widget in main_window.grid_slaves():
        if int(widget.grid_info()["row"]) > 3 :
            widget.grid_forget()
        else:            
            #Create column headings
            if counters['total_entries'] > 0:
                Label(main_window, font=("Bahnschrift", 10, "bold"),text="Entry No.",bg='#b4c8e4').grid(column=0,row=7,pady=25)
                Label(main_window, font=("Bahnschrift", 10, "bold"),text="Reciept Number",bg='#b4c8e4').grid(column=1,row=7,pady=25)
                Label(main_window, font=("Bahnschrift", 10, "bold"),text="Full Name",bg='#b4c8e4').grid(column=2,row=7)
                Label(main_window, font=("Bahnschrift", 10, "bold"),text="Item Hired ",bg='#b4c8e4').grid(column=3,row=7)
                Label(main_window, font=("Bahnschrift", 10, "bold"),text="Amount Hired",bg='#b4c8e4').grid(column=3,columnspan=3,padx=20,row=7)
        
    #add each item in the list into its own row
    name_count = 0
    while name_count < counters['total_entries'] :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        Label(main_window, text=(name_count+1),font=("Bahnschrift", 11)).grid(column=0,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][1]),font=("Bahnschrift", 10)).grid(column=1,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][2]),font=("Bahnschrift", 10)).grid(column=2,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][3]),font=("Bahnschrift", 10)).grid(column=3,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][4]),font=("Bahnschrift", 10)).grid(column=3,columnspan=3,padx=20,row=name_count+8)
        name_count +=  1
        counters['name_count'] = name_count 

#Check the inputs are all valid
def check_inputs ():
    #Program checks if name is not blank, if blank then it outputs a error
    if len(customer_name.get()) == 0:
        messagebox.showwarning("Warning","Customer Name field must not be left blank.")
        return 0 # entered details were incorrect.
    elif (customer_name.get().isalpha()) == False:
        messagebox.showerror("Error","No numbers, blank symbols or symbols for name. Alphabet only and no spaces.")
        return 0 # entered details were incorrect.
    if len(item.get()) == 0:
        messagebox.showwarning("Warning","You cannot procced without selecting a item.")
        return 0
    elif (item.get().isdigit()) == True:
        messagebox.showwarning("Error","Not a valid item.")
        return 0
    #Program checks if the item amount is not blank and that the amount enetered is between 1-500 
    if len(entry_amount.get()) == 0:
        messagebox.showwarning("Warning","You must not leave the Amount Hired Field Blank.")
        return 0 # entered details were incorrect.
    elif (entry_amount.get().isdigit()) == False: 
        messagebox.showerror("Error","No symbols, negative numbersor letters in the amount hired field.")
        return 0
    elif int(entry_amount.get()) < 1 or  int(entry_amount.get()) > 500:
        messagebox.showerror("Error","You can only have a quanitiy of an item between the range of 1-500.") 
        return 0 # entered details were incorrect.     
    return 1 # all the details are correct.

#add more customers to the list. 
def append_entry ():  
    if check_inputs() == 1:        
        #Create a variable for random receipt number. 
        receipt_num = random.randint(1,10000)
        #append each item to its own area of the list
        customer_details.append([ str(counters['total_entries']) ,int(receipt_num),customer_name.get(),item.get(),entry_amount.get()])
        #create a bulleted list for the valid entries messagebox.
        saving_details(customer_details)        
        #clear the boxes
        customer_name.delete(0,'end')
        item.set('')
        #item.delete(0,'end')
        entry_amount.delete(0,'end')
        counters['total_entries'] += 1        
    else:
        return 0

#Function for deleting a row from the list
def delete_row():
    #find which row is to be deleted and delete it
    if (delete_item.get()) == "":
        messagebox.showerror("Error","Enter a receipt number to delete.")
    

    else:
        deletedreceipt_num = int(delete_item.get().strip().replace("",""))
        customer_detected = False
        for i, myOrder in enumerate(customer_details):
            if myOrder[1] == deletedreceipt_num:
                del customer_details[i]
                customer_detected = True

         
        if customer_detected: 
            counters['total_entries'] -= 1
            name_count = counters['name_count']
            delete_item.delete(0,'end')
            print_customer_details()
        else:
            messagebox.showerror("Error","Receipt Number not found.")

#Create function for writing the entries to a text file.
def saving_details(myOrder):
    with open("customerdeats.txt","a") as file:
        for i in myOrder[len(myOrder)-1]:
            file.write(str(i)+ ",")  
        file.write("\n")
        file.close()

#create the buttons and labels

#testing window size
def button_setup():
    Label(main_window,text="Customer Name",font=("Bahnschrift", 12, "bold"),bg='#b4c8e4').grid(column=0, row=0, padx=12, ipadx=10, pady=10, sticky=E)
    Label(main_window,text="Item Hired",font=("Bahnschrift", 12, "bold"),bg='#b4c8e4').grid(column=0, row=1, padx=12, pady=10, sticky=E,)

    Label(main_window,text="Amount Hired",font=("Bahnschrift", 12, "bold"),bg='#b4c8e4').grid(column=0, row=2, padx=5, pady=10, sticky=E)

    Button(main_window,text="Print",font=("Bahnschrift", 12, "bold"),command=print_customer_details,width=12).grid(column=2,row=0, pady=10,sticky=E)
    Button(main_window,text="Submit",font=("Bahnschrift", 12, "bold"),command=append_entry,width=12).grid(column=2,row=1,pady=10,sticky=E)
    Button(main_window,text="Quit",font=("Bahnschrift", 12, "bold"), command=quit, bg="#ba2106", fg="#FFFFFF",width=12).grid(column=3,row=0,pady=10,sticky=E)
    Button(main_window,text="Delete Receipt",font=("Bahnschrift", 12, "bold"),command=delete_row,width=12).grid(column=3, row=1,pady=10,sticky=E)
    #create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location


#create empty list for customer details and empty variable for entries in the list
counters = {'total_entries': 0, 'name_count': 0}
customer_details = []
customer_name = Entry(main_window)
customer_name.grid(column=1, row=0)

#create combobox for items
def combo(event):

    myLabel = Label(main_window, text="")


items = ["Spoon","Forks","Party Plates","Serviettes","Drinking Cups","Paper Bowls","Candles"]
var= StringVar() 
item = ttk.Combobox(main_window, textvariable= var, value=items)
item['state'] = 'readonly'
item.bind("<<ComboboxSelected>>", combo)
item.grid(column=1, row=1)
entry_amount = Entry(main_window)
entry_amount.grid(column=1, row=2)
delete_item = Entry(main_window)
delete_item.grid(column=3,row=2,sticky=E)
main()    
