# Jesse Page
# Lab 5 assignment
# This program reads the contactsLab4.txt file and will print
# out every contact's name, age, the season they were born,
# and whether not they were born in a leap year. Finally,
# this program will print out the average age of all the contacts

import lab5_class_Page

def main():
    # opens contactsLab4 file to read
    try:
        contacts = open("contactsLab5.txt", "r")
        contact_list = []

        # begins reading the first line of the file
        name = contacts.readline()

        # reads each line of the file til it reaches the end
        while name != "":
            # removes trailing whitespace from name 
            name = name.rstrip("\n")
            # removes trailing whitespace from birthday 
            birthday = contacts.readline()
            birthday = birthday.rstrip("\n")

            # creates the Contact object and sets the name and birthday attributes
            a_contact = lab5_class_Page.Contact()
            a_contact.set_name(name)
            a_contact.set_birthdate(birthday)

            # puts contact object in a list
            contact_list.append(a_contact)
            name = contacts.readline()
        contacts.close()

        # call function to display contact info
        display_contacts(contact_list)
    
    # Check for invalid file name
    except FileNotFoundError:
        print("Error: Invalid file name")

    except Exception as error_msg:
        print("Error:", error_msg) 


#####################################################
# Function name: display_contacts                   #
# Input: The lists of names and birthdates          #
# Output: none                                      #
# Purpose: This function displays in a table, the   #
#          names, ages, seasons born and whether    #
#          their birth year was a leap year or not  #
##################################################### 

def display_contacts(contact_list):
    # Initialize the total age and leap year column display
    yes_no = ""
    age_total = 0

    # reads date input from user
    current_date = input("Enter the current date in the format Month D, YYYY: ")

    # displays headings for columns
    print(
        format("Names", '25'), 
        format("Age", '5'), 
        format("Season Born", '12'), 
        "Leap Year?")
    
    print(
        format("-----", '25'), 
        format("----", '5'), 
        format("---------", '12'), 
        "---------")

    # iterates through the length of birthdates_list 
    for i in range(len(contact_list)):

        # Call function to determine if the year was a leap year or not
        leap_year = contact_list[i].is_leap_year()
        if leap_year == True:
            yes_no = "Yes"
        else:
            yes_no = "No"

        # gets contact's age
        age = contact_list[i].calculate_age(current_date)
        # Accumulate ages for the average age calculation
        age_total = (age_total + age)
        
        # displays message to the user
        print(
            format(contact_list[i].get_name(), '25'), 
            format(str(age), '5'), 
            format(contact_list[i].find_season(), '12'), 
            yes_no)
    
    print("")
    # displays average age of all contacts
    print("Average age of contact is", int(age_total / len(contact_list)))
    
main()