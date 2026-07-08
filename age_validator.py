# ALAB 356.2
# Task 3: Custom Exception Test (Age Validator)

def validate_age(age):
    if age < 0 or age > 120: # Verifying age is within valid range
        raise ValueError("Error: input age is not within valid limit (from 0 to 120)")

try:
    user_age = int(input("Please enter age (0 to 120): ")) # Prompt user for age input
    validate_age(user_age) # calling the validate_age function to check if age is valid
    print("Age accepted!") # If age is valid, print confirmation message
except ValueError as error:
    print(error)
