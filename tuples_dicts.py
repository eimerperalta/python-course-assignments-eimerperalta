# ALAB 351.4 - Functions, Tuples, Dictionaries, and Exceptions
# Part 2: Tuples and Dictionaries

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December") # Tuple of months
print(months[0]) # Indexing first elemtent of a tuple
print(months[-1]) # indexing last element of a tuple

try:
  months[0] = "NewMonth" # This will raise an error because tuples are immutable
except TypeError as error:
  print(f"Tuples are immutable, error: {error}")

# Dictionary of students and their grades
students = { 
  "John": 85,
  "Jane": 92,
  "Tom": 78,
  "Emily": 90,
  "Albert": 88
}

students["Rose"] = 63 # Adding new key/value pair to the dictionary
print(students)

students["Tom"] = 80 # Updating value of an existing key in the dictionary

for student, grade in students.items():
  print(student, ': ', grade, sep='')