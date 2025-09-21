# main.py - Personal Data Manager

# TODO: Step 1 - Prompt the user to enter their name and age
# Hint: Use input() and store the values in variables

name = input("What is your name?: ")
age = int(input("What is your age?: "))


# TODO: Step 2 - Ask the user to enter 3 hobbies
# Hint: Use a loop to collect hobbies and store them in a list

hobbies = []
for i in range(0,3):
    hobby = input("Enter Hobby ?: ")#
    hobbies.append(hobby)

# TODO: Step 3 - Create a dictionary to store the user's name, age, and hobbies
# Hint: Use key-value pairs to organize the data

userData = {
    "name": name,
    "age": age,
    "hobbies": hobbies
}

# TODO: Step 4 - Display the user's information using formatted strings
# Hint: Use f-strings to format the output

print(f"Name: {userData['name']}\nAge: {userData['age']}\nHobbies: {', '.join(userData['hobbies'])}")

# TODO: Step 5 - Convert the hobbies list into a set to remove duplicates
# Hint: Use the set() function

userData["hobbies"] = set(userData["hobbies"])

# TODO: Step 6 - Calculate the user's birth year and store it in a tuple with the current year
# Hint: Use subtraction and a tuple to store both years

from datetime import date
currentDate = date.today()
currentYear = currentDate.year
birthYear = currentYear - age
YearTuple = (currentYear, birthYear)

# TODO: Step 7 - Create a function that takes the dictionary and returns a summary string
# Hint: Use string concatenation or f-strings inside the function

def create_summary(userData):
    return (
        f"---------------------------"
        f"Name: {userData['name']}\n"
        f"Age: {userData['age']}\n"
        f"Hobbies: {', '.join(userData['hobbies'])}"
        f"Years: Current {YearTuple[0]}, Birth {YearTuple[1]}"
    )


# TODO: Step 8 - Call the function and print the summary
# Hint: Pass the dictionary to the function and print the result

print(create_summary(userData))