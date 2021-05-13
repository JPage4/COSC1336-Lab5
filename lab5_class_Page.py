class Contact:
    def __init__(self):
        self.__name = ""
        self.__birthdate = ""

#########################################
# Function Name: set_name
# Input: string
# Output: string
# Purpose: mutator method
#########################################
    def set_name(self, name):
        self.__name = name

#########################################
# Function Name: set_birthdate
# Input: string
# Output: string
# Purpose: mutator method
#########################################
    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate

#########################################
# Function Name: get_name
# Input: string
# Output: string
# Purpose: accessor method
#########################################
    def get_name(self):
        return self.__name

#########################################
# Function Name: get_birthdate
# Input: string
# Output: string
# Purpose: accessor method
#########################################
    def get_birthdate(self):
        return self.__birthdate


################################################
# Function name: find_season                   #
# Input: birthdate as a string                 #
# Output: season as an string                  #
# Purpose: This function gets the season the   #
#          month is in                         #
################################################
    def find_season(self):
        # isolates month element of birthdate string
        space = self.get_birthdate().index(" ")
        month = self.get_birthdate()[:space]

        #if-else condition to check month and 
        # assign correct season
        if month == "December" or month == "January" or month == "February":
            season = "Winter"
        elif month == "March" or month == "April" or month == "May":
            season = "Spring"
        elif month == "June" or month == "July" or month == "August":
            season = "Summer"
        elif month == "September" or month == "October" or month == "November":
            season = "Fall"
        return season

################################################
# Function name: is_leap_year                  #
# Input: birthdate as a string                 #
# Output: True if year is a leap year          #
#         False if it is not                   #
# Purpose: This function determines if a year  #
#          is a leap year or not               #
################################################
    def is_leap_year(self):
        # isolates year element of birthdate string
        year = int(self.get_birthdate()[-4:])

        #if-else condition to check if year is a leap year
        if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
            leap_year = True
        else:
            leap_year = False
        
        return leap_year

################################################
# Function name: calculate_age                 #
# Input: user input for the current date and   #
# contact's birthdate as a string              #
# Output: contact's age as an int              #
# Purpose: This function calculate's the age   #
#  of the contact based on the current date    #
################################################    
    def calculate_age(self, current_date):
        # gets appropriate index to use for slicing the date strings below
        bday_space = self.get_birthdate().index(" ")
        bday_comma = self.get_birthdate().index(",")
        current_space = current_date.index(" ")
        current_comma = current_date.index(",")

        # separates each part of the birthdate string into month, day and year
        birthday_month = self.get_birthdate()[:bday_space]
        birthday_day = int(self.get_birthdate()[bday_space + 1:bday_comma])
        birthday_year = int(self.get_birthdate()[-4:])

        # separates each part of the current date string into month, day and year
        current_month = current_date[:current_space]
        current_day = int(current_date[current_space + 1:current_comma])
        current_year = int(current_date[-4:])

        # Convert month strings to integers for calculations
        if birthday_month == "December":
            birthday_month = 12
        elif birthday_month == "January":
            birthday_month = 1
        elif birthday_month == "February":
            birthday_month = 2
        elif birthday_month == "March":
            birthday_month = 3
        elif birthday_month == "April": 
            birthday_month = 4
        elif birthday_month == "May":
            birthday_month = 5
        elif birthday_month == "June": 
            birthday_month = 6
        elif birthday_month == "July": 
            birthday_month = 7
        elif birthday_month == "August":
            birthday_month = 8
        elif birthday_month == "September": 
            birthday_month = 9
        elif birthday_month == "October": 
            birthday_month = 10
        elif birthday_month == "November":
            birthday_month = 11
        
        # Convert month strings to integers for calculations
        if current_month == "December":
            current_month = 12
        elif current_month == "January":
            current_month = 1
        elif current_month == "February":
            current_month = 2
        elif current_month == "March":
            current_month = 3
        elif current_month == "April": 
            current_month = 4
        elif current_month == "May":
            current_month = 5
        elif current_month == "June": 
            current_month = 6
        elif current_month == "July": 
            current_month = 7
        elif current_month == "August":
            current_month = 8
        elif current_month == "September": 
            current_month = 9
        elif current_month == "October": 
            current_month = 10
        elif current_month == "November":
            current_month = 11       

        # calculates the contact's age
        if (current_month, current_day) < (birthday_month, birthday_day):
            age = current_year - birthday_year - 1
        else:
            age = current_year - birthday_year

        return age




