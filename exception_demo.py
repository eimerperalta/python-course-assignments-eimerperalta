# ALAB 351.4 - Functions, Tuples, Dictionaries, and Exceptions
# Part 3: Exception Handling

def safe_divide(a, b):
  if b == 0:
    raise ValueError("Cannot divide by zero.") # ValueError follows lab instructinos but ZeroDivisionError should be used instead.
  else:
    return a / b

try: # test values
  print(safe_divide(2, 2))
  print(safe_divide(12, 3))
  print(safe_divide(15, 4))
  print(safe_divide(10, 0)) # Divides by zero
  
except ZeroDivisionError as error:
  print(f"Zero division error occurred: {error}")
except ValueError as error:
  print(f"Value error occurred: {error}")
except TypeError as error:
  print(f"Type error occurred: {error}")
finally:
  print("Division operation completed")


try:
  print(safe_divide(8, 'e')) # outputs an error because 'e' is not a interger.
except TypeError as error:
  print(f"Type error occurred: {error}")