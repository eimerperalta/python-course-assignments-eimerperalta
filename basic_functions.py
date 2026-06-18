# ALAB 351.4 - Functions, Tuples, Dictionaries, and Exceptions 
# Part 1: Writing and Using Functions

def greet_user(user_name=""):
  if user_name == "": # if name is not especified, then prompt user name.
    user_name = input("Please enter your name: ")
  print(f"Hello {user_name}! Welcome!")

def add_two_numbers(a, b):
  print(f" {a} + {b} = {a + b}")
  return a + b

def is_even(num):
  if num % 2 == 0: # divisible by 2
    print(f"{num} is even")
    return True
  else:
    print(f"{num} is NOT even")
    return False

# Calling functions
greet_user() # No arguments
john = greet_user("John") # With arguments
print(john)

addition = add_two_numbers(8, 8) # Storing function result in variable
print(addition)

is_even(17) # Ouputs: 17 is NOT even
is_even(24) # Outputs: 24 is even
