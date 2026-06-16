# ALAB 351.1 - Part 2

try:
  num_1 = float(input("Enter a number: "))
  num_2 = float(input("Enter another number: "))

except ValueError:
  print("Input is not a valid number.")

operation = input("Choose an operation (+, -, *, /): ")

if operation == '+':
  result = num_1 + num_2
  print(f"{num_1} {operation} {num_2} = {result}")

elif operation == '-':
  result = num_1 - num_2
  print(f"{num_1} {operation} {num_2} = {result}")

elif operation == '*':
  result = num_1 * num_2
  print(f"{num_1} {operation} {num_2} = {result}")

elif operation == '/':
  result = num_1 / num_2
  print(f"{num_1} {operation} {num_2} = {result}")

elif operation not in ('+', '-', '*', '/'):
  print("Wrong operation. Please choose a valid operation (+, -, *, or /)")
