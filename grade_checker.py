# ALAB 351.3 - Part 1.1

grade = int(input("Enter your grade (0-100): "))

while grade > 100 or grade < 0: # While loop works better than if condition here
  print("Please enter a valid grade (0-100)")
  grade = int(input("Enter your grade (0-100): "))

if grade >= 90 and grade <= 100:
  grade = 'A'

elif grade >= 80 and grade <= 89:
  grade = 'B'

elif grade >= 70 and grade <= 79:
  grade = 'C'

elif grade >= 60 and grade <= 69:
  grade = 'D'

elif grade >= 0 and grade <= 59:
  grade = 'F'

print(f"Your grade is: {grade}")

if grade in ("A", "B", "C"):
  print("Congratulations, you passed!")
else:
  print("Not a passing grade. Please keep studying and try again next time")