# To check weather the year is a leap year or not

# Making a function and passing the parameter year into it.

def checkLeapYear(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print("This year is a leap year")
    else:
        print("This is not a leap year")


year = int(input("Enter Year to check weather it is a leap year or not:"))

checkLeapYear(year)
