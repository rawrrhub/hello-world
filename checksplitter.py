#Check splitter 

#numbers should automatically round up so people aren't short with change
#dont want user to see errors like tracebacks etc
#fix the ValueErrors and make it helpful to the user

import math

def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / number_of_people)

try:
    total_due = float(input("What is the total? "))
    number_of_people = int(input("How many people? "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err: #this is a new variable that will be created (err) and will be assigned the exception that was thrown
    print("Oh no! That's not a valid value. Try again...")
    print("({})".format(err)) # could also just be print(err)
else:
    print("Each person owes ${}".format(amount_due))