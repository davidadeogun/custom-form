#tkinter
#A custom form
#Where users can add data to a csv file

#Tutorial url : https://www.youtube.com/watch?v=7MQWCtTr0zA&t=2592s
from csv import DictWriter
import tkinter as tk
from tkinter import ttk
import os
import csv
from collections import namedtuple

win = tk.Tk()
win.title("Custom Form")

def main(): #Prints the data in the csv file to the terminal
   
   
   #An exception handling. 
   #FileNotFoundError 
   #Handled the exception incase the csv file (file.csv) is not found.
   #This reads the csv file and converts it into a list, printing on a new line to the terminal
    try:
        with open("file.csv", "rt") as data_file:
            f_csv = csv.reader(data_file)
            headers = next(f_csv)
            for row in f_csv:
                print(row)
            
    except FileNotFoundError as not_found_err:
        print(not_found_err)



    win.title("Custom Form")  #Title of the Custom Form
    win.mainloop()


#Create labels
#Widgets -- > labels, buttons, radio buttons
name_var = tk.StringVar()
name_label = ttk.Label(win, text='Enter your name: ')
name_label.grid(row=0, column=0, sticky=tk.W) #Adding sticky positions the label on the start of a new line
name_entrybox = ttk.Entry(win, width=25, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()  #Makes the cursor to start in name entry box, rather than allowing the user to manually 

email_var = tk.StringVar()
email_label = ttk.Label(win, text='Enter your email:')
email_label.grid(row=1, column=0, sticky=tk.W)
"""This creates an entry box and positions it besides the respective labels"""
email_entrybox = ttk.Entry(win, width=25, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

phone_var = tk.StringVar()
phone_label = ttk.Label(win, text='Phone Number')
phone_label.grid(row=2, column=0, sticky=tk.W)
phone_entrybox = ttk.Entry(win, width=25, textvariable=phone_var)
phone_entrybox.grid(row=2, column=1)


age_var = tk.StringVar()
age_label = ttk.Label(win, text='Enter your age: ')
age_label.grid(row=3, column=0, sticky=tk.W)
age_entrybox = ttk.Entry(win, width=25, textvariable=age_var)
age_entrybox.grid(row=3, column=1)


#Create Combobox
gender_var = tk.StringVar()
gender_label = ttk.Label(win, text='Select Gender')
gender_label.grid(row=4, column=0, sticky=tk.W)
"""The readonly state ensures that only the values supplied in the drop dowwn menu
are supplied as input"""
gender_comobobox = ttk.Combobox(win, width=22, textvariable=gender_var, state='readonly')
gender_comobobox['values'] = ('Male', 'Female', 'Other') #Drop down menu gender options
gender_comobobox.current(0) #Gives the first value in the drop down menu as the default value. Index (0) is male, (1) is female
gender_comobobox.grid(row=4,  column=1)


#Create radio buttons
#Two radio buttons, student and teacher
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='Student', value='Student', variable=usertype)
radiobtn1.grid(row=5, column=0)

radiobtn2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype)
radiobtn2.grid(row=5, column=1)


#Create checkbox
checkbox_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text='Check if you want to subscribe', variable=checkbox_var)
checkbtn.grid(row=6, columnspan=3)

#Create buttons
"""The action function gets the input value and returns it for respsective variables"""
def action():
    username = name_var.get()
    useremail = email_var.get()
    userphone = phone_var.get()
    userage = age_var.get()
    checkbox = checkbox_var.get()
    radio_user = usertype.get()
    user_gender = gender_var.get()

    def calculate(event):
        try:
            
            age = age_var.get()

            max_rate = 220- age

            slow = max_rate * 0.65
            fast = max_rate * 0.89
            

        except ValueError:

            
    
    

    """The checkbox gives a default value of 0 if it is unchecked,
    but 1 when it is checked."""
    if checkbox == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'

    f"{user_gender}, {radio_user}, {subscribed}" #Does nothing print result to terminal

    
    #Create a csv file that saves the entry data
    #newline stores the entry data on the next line in the csv file
    with open ('file.csv', 'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['UserName', 'User Email Address', 'User Phone Number', 'User Age', 
        'Gender', 'User Type', 'Subscribed'])

        #The os module prevents the data from repeating the header in the file.
        #Instead, it stores the header once.
        if os.stat('file.csv').st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'UserName' : username,
            'User Email Address': useremail,
            'User Phone Number': userphone,
            'User Age': userage,
            'Gender': user_gender,
            'User Type' : radio_user,
            'Subscribed': subscribed

        })
      
        name_entrybox.delete(0, tk.END)
        email_entrybox.delete(0, tk.END)
        phone_entrybox.delete(0, tk.END)
        age_entrybox.delete(0, tk.END)
       
           
submit_button = ttk.Button(win, text='Submit', command=action)
submit_button.grid(row=7, column=1)
     

if __name__ == "__main__":
    main()