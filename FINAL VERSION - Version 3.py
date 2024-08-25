########################################################################
###Welcome to Julies Party Hire!. ###
########################################################################

#import the tkinter library so a GUI can be made. 
import random #import random module
from tkinter import *
from tkinter import messagebox, ttk #import messagebox and ttk (tkinter tool kit) modules. 



#create the buttons and labels
def button_setup():
    Label(main_window,text="Customer Name",font=("Bahnschrift", 12, "bold"),bg='#b4c8e4').grid(column=0, row=0, padx=12, ipadx=10, pady=10, sticky=E) #Create a label for Customer Name
    Label(main_window,text="Item Hired",font=("Bahnschrift", 12, "bold"),bg='#b4c8e4').grid(column=0, row=1, padx=12, pady=10, sticky=E,) #Create a label for Item Hired
    Label(main_window,text="Amount Hired",font=("Bahnschrift", 12, "bold"),bg='#b4c8e4').grid(column=0, row=2, padx=5, pady=10, sticky=E) #Create a label for Amount Hired
    Button(main_window,text="Print",font=("Bahnschrift", 12, "bold"),command=print_customer_details,width=12).grid(column=2,row=0, pady=10,sticky=E) #Create Print Details button
    Button(main_window,text="Submit",font=("Bahnschrift", 12, "bold"),command=append_entry,width=12).grid(column=2,row=1,pady=10,sticky=E) #Create Submit Details button
    Button(main_window,text="Quit",font=("Bahnschrift", 12, "bold"), command=quit, bg="#ba2106", fg="#FFFFFF",width=12).grid(column=3,row=0,pady=10,sticky=E) #Create Quit button
    Button(main_window,text="Delete Receipt",font=("Bahnschrift", 12, "bold"),command=delete_customer_receipt,width=12).grid(column=3, row=1,pady=10,sticky=E) #Create button for Deleting Receipt. 

#create combobox for items
def combo(event):
    myLabel = Label(main_window, text="")

#Function used to define the quit button command. 
def quit(): 
    response = messagebox.askyesno("Quit","Do you want to quit the program?")
    if response == 1: #If response variable is true then program will be terminated if the user selects "Yes" on the messagebox. 
        main_window.destroy()#Program is terminated/exited. 

#print all customer details 
def print_customer_details ():
    for widget in main_window.grid_slaves():
        if int(widget.grid_info()["row"]) > 3 :
            widget.grid_forget()
        else:            
            #Create column headings
            if counters['total_entries'] > 0:
                Label(main_window, font=("Bahnschrift", 10, "bold"),text="Entry No.",bg='#b4c8e4').grid(column=0,row=7,pady=25) #Create a column heading for Entry No. when the Print button is clicked
                Label(main_window, font=("Bahnschrift", 10, "bold"),text="Receipt Number",bg='#b4c8e4').grid(column=1,row=7,pady=25) #Create a column heading for Receipt Number when the Print button is clicked
                Label(main_window, font=("Bahnschrift", 10, "bold"),text="Customer Name",bg='#b4c8e4').grid(column=2,row=7) #Create a column heading for the Customers Name when the Print button is clicked
                Label(main_window, font=("Bahnschrift", 10, "bold"),text="Item Hired ",bg='#b4c8e4').grid(column=3,row=7) #Create a column heading for the Item Hired when the Print button is clicked
                Label(main_window, font=("Bahnschrift", 10, "bold"),text="Amount Hired",bg='#b4c8e4').grid(column=3,columnspan=3,padx=20,row=7)#Create a column heading for Amount Hired when the Print button is clicked
        
    #add each item in the list into its own row
    name_count = 0
    while name_count < counters['total_entries'] :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        Label(main_window, text=(name_count+1),font=("Bahnschrift", 11)).grid(column=0,row=name_count+8) #Entry Number value
        Label(main_window, text=(customer_details[name_count][1]),font=("Bahnschrift", 10)).grid(column=1,row=name_count+8) # Randomly generated receipt number value
        Label(main_window, text=(customer_details[name_count][2]),font=("Bahnschrift", 10)).grid(column=2,row=name_count+8) # Customer Name value 
        Label(main_window, text=(customer_details[name_count][3]),font=("Bahnschrift", 10)).grid(column=3,row=name_count+8) # Item which the customer has hired value. 
        Label(main_window, text=(customer_details[name_count][4]),font=("Bahnschrift", 10)).grid(column=3,columnspan=3,padx=20,row=name_count+8) #The Quantity of the Item the customer has hired value.
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
        customer_details.append([ str(counters['total_entries']+1) ,int(receipt_num),customer_name.get(),item.get(),entry_amount.get()]) 
        #call the saving_details() function so that the details can be written to a file.
        saving_details(customer_details)        
        #clear the boxes
        customer_name.delete(0,'end')
        item.set('')
        #item.delete(0,'end')
        entry_amount.delete(0,'end')
        #increase the number of entries
        counters['total_entries'] += 1        
    else:
        return 0 #If check_inputs is not == to 1 program will not proceed.

#Function for deleting a row from the list
def delete_customer_receipt():
    #find which receipt is to be deleted and delete it
    #If the Delete Receipt entry box is left blank program will output an error
    if (delete_receipt.get()) == "":
        messagebox.showerror("Error","Enter a receipt number to delete.")
    else:
        deletedreceipt_num = int(delete_receipt.get().strip().replace("","")) #Create a variable for the deleted receipt number which stores the input that has been entered in delete_receipt entry box. 
        customer_detected = False #customer is detected as 'not found'
        for i, myOrder in enumerate(customer_details): 
            if myOrder[1] == deletedreceipt_num: #Program checks to see if the receipt number for the myOrder variable matches the receipt number entered in the Delete Receipt entry box.
                del customer_details[i] #Program will delete a row if a match has been found between the myOrder variable and Delete Receipt entry box.
                customer_detected = True #If everything above is correct then the customer is detected as 'found'.
         #commands to execute if the customer_detected value is true. 
        if customer_detected: 
            counters['total_entries'] -= 1 #Program will remove a row if the customer_detected vairbale is True. 
            name_count = counters['name_count']
            delete_receipt.delete(0,'end') #Clear the delete_receipt entry box.
            print_customer_details() #Call the print_customer_details function
        else: 
            messagebox.showerror("Error","Receipt Number not found.") #If the user inputs a receipt number which is not found, program will output an error. 

#Create function for writing the entries to a text file.
def saving_details(myOrder):
    with open("customerdetails.txt","a") as file:
        for i in myOrder[len(myOrder)-1]:
            file.write(str(i)+ ",")  
        file.write("\n")
        file.close()


#start the program running
def main():
    #Start the GUI
    button_setup() #Call the button_setup function so the buttons and labels can be displayed on the GUI
    main_window.mainloop()# Loop which keeps the program running unless the window is closed. 

#main_window.mainloop()--- starts
main_window =Tk() 
main_window.title('Julies Party Hire')
main_window.geometry('692x390')

#Show image using label
bgtest = PhotoImage(file = "programbg.png")
mybg = Label(main_window, image=bgtest)
mybg.place(x=0, y=0)

#setup columnsizes
main_window.columnconfigure(0, weight=0, minsize=150) #Setup columnsize for column 0
main_window.columnconfigure(1, weight=0, minsize=150) #Setup columnsize for column 1
main_window.columnconfigure(2, weight=0, minsize=120) #Setup columnsize for column 2
main_window.columnconfigure(3, weight=0,pad=40,minsize=0) #Setup columnsize for column 3
main_window.columnconfigure(4, weight=0, minsize=100)#Setup columnsize for column 4
main_window.columnconfigure(5, weight=0, minsize=150) #Setup columnsize for column 5

#create empty list for customer details and empty variable for entries in the list
counters = {'total_entries': 0, 'name_count': 0}
customer_details = []
#create blank entry box for the customers name 
customer_name = Entry(main_window)
customer_name.grid(column=1, row=0)

#List of items available to hire 
items = ["Spoon","Forks","Party Plates","Serviettes","Drinking Cups","Paper Bowls","Candles"]

var= StringVar() 
item = ttk.Combobox(main_window, textvariable= var, value=items)
item['state'] = 'readonly' #User cannot write anything in the Item Hired combobox. They can only select an item. 
item.bind("<<ComboboxSelected>>", combo)
item.grid(column=1, row=1)

#create blank entry box so that the customer can enter the quantity of an item 
entry_amount = Entry(main_window)
entry_amount.grid(column=1, row=2)

#create blank entry box for the receipt number for deletion purposes  
delete_receipt = Entry(main_window)
delete_receipt.grid(column=3,row=2,sticky=E)

main()    
