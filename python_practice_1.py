# To check weather the year is a leap year or not

# Making a function and passing the parameter year into it.

def checkLeapYear(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print("This year is a leap year")
    else:
        print("This is not a leap year")


year = int(input("Enter Year to check weather it is a leap year or not:"))

checkLeapYear(year)


# CODE 

sentence = "this is a python program"
word = sentence.split()
print(word)

# We have to split this in ordered form like a is program python this

sorted_words = sorted(word)
for word in sorted_words:

    print(word)


# CODE 3

# To check weather the string is float or not

x = input("Enter a word or any number: \n")

def check_float_Number(x):
    try:
        float(x)
        return True
    except:
        return False


print(check_float_Number(x))

