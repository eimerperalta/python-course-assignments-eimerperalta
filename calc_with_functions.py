# ALAB 351.4 - Functions, Tuples, Dictionaries, and Exceptions
# Part 1: Writing and Using Functions

def add(a, b):
  return a + b

def subtract(a, b): 
  return a - b

def multiply(a, b): 
  return a * b

def divide(a, b):
  if b == 0:
    raise ZeroDivisionError("division by zero is not allowed")
  else:
    return a / b

def calculate(a, b, op):
  try:
    if op == '+':
      return add(a, b)
    elif op == '-':
      return subtract(a, b)
    elif op == '*':
      return multiply(a, b)
    elif op == '/':
        return divide(a, b)
    else:
      raise NameError("Please provide a valid operator: +, -, *, /")
  except ZeroDivisionError:
    print("Error: division by zero is not allowed")
    return None
  except NameError:
    print("Error: Please provide a valid operator: +, -, *, /")
    return None
  except Exception as error:
    print(f"An unexpected error occurred: {error}")
    return None

# main
try:
  a = int(input("Enter a number: "))
  b = int(input("Enter another number: "))
  op = input("Enter an operator (+, -, *, /)")
  print(f" {a} {op} {b} = {calculate(a, b, op)}")
except ValueError:
  print("Input is not a valid number.")
except ZeroDivisionError:
  print("Error: division by zero is not allowed")
