'''
"Contact information book"
Eshaan Tripathi
11/4/22
Contact information book
'''

#import csv and pandas libraries
import csv
import pandas as pd

#print starting message
print("Hello! Welcome to the contact information book.")

#ask if the user wants to start or not
start = input("Enter 'Y' to start or 'N' to quit: ")

#define contact info types
contact_info_types = ["First Name: ", "Last Name: ", "Phone: ", "Email: ", "Address: "]

#if the user chooses to start...
if start.lower() == "y":
    print("\n\nEnter 'quit' to exit.")

    #ask for input
    original_input = input("$")

    #split input into command
    command = original_input.split()[0]

    #while the command isnt quit...
    while command.lower() != "quit":
        #split original input again for the repeat
        command = original_input.split()[0]

        #if the command is add...
        if command == "add":
            #define the c_info list
            c_info = []
            #loop through the info types
            for i in contact_info_types:
                #ask for input for them
                c_info_el = input(i)
                #append that input into the c_info list
                c_info.append(c_info_el)

            #print the process message
            print("Adding...")

            #open the contacts file to append
            with open("contacts.csv","a+") as f:
                #define the writer
                writer = csv.writer(f)

                #write the information into the file
                writer.writerow(c_info)
            
            #print the success message
            print("Success!")

        #if the command is get...
        if command == "get":
            #split the original input into an argument
            arg = original_input.split()[1]

            #open the contacts file to read
            with open("contacts.csv", "r") as f:
                #remove column names
                k = f[1:]

                #loop through column-name-less dataframe
                for i in k:
                    #split piece of information
                    x = i.split(",")
                    #loop through each column in row
                    for j in x:
                        #check whether one of the data types is equal to wha the user entered
                        if j.lower() == arg.lower():
                            #get that person's information index
                            person = x.index(j)

                            #print the person's name
                            print(f"That person is: {x[0]} {x[1]}.")
                            print("\nTheir Information:\n")

                            #loop through their data and print it
                            for l in x:
                                ind = x.index(l)

                                print(contact_info_types[ind]+l)

        #if the command is remove...
        if command == "remove":
            #print all contacts
            print("\nContacts: ")
            with open("contacts.csv", "r") as f:
                #define dataframe wihtout column names
                j = f[1:]

                #loop through the dataframe
                for i in j:
                    #split the row into each data type
                    x = i.split(",")
                    #concatenate full name
                    name = x[0]+" "+x[1]
                    #print contact name
                    print(name)

            #ask for a piece of informaiton on the contact you want to delete.
            deleted_contact = input("Enter the last name of the contact you want to delete: ")

            #open the contactbook to read
            with open("contacts.csv", "r") as f:
                #loop through each row
                for i in f:
                    #split the row into each data type
                    x = i.split(",")
                    #loop through the splitted row
                    for j in x:      
                        #check if the deleted_contact variable is equal to any of the piece of data.
                        if j.lower() == deleted_contact.lower():
                            person = x.index(j)
                            #read csv with pandas and store into dataframe
                            df = pd.read_csv("contacts.csv")
                            #get index of the row
                            row = df[((df.fname == deleted_contact) |( df.lname == deleted_contact) | (df.phone == deleted_contact)|(df.email == deleted_contact)|(df.address == deleted_contact))].index
                            #delete that row.
                            df.drop(row)

            #open the contact book to write
            with open("contacts.csv", "w+") as f:
                #define the writer
                writer = csv.writer(f)
                #replace the contents with those in the dataframe.
                writer.writerow(df)

        #ask for input again.
        original_input = input("$")