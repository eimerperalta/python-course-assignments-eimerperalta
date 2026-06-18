# ALAB 351.4 - Functions, Tuples, Dictionaries, and Exceptions
# Part 2: simulates a simple data processing scenario

def get_average_grade(grades_tuple):
  try:
    total = 0
    for grade in grades_tuple:
      total += grade
    return total / len(grades_tuple)
  except ZeroDivisionError:
    return None

course_grades = {
  'Math': (80, 65, 86),
  'Science': (90, 78, 81),
  'History': (70, 95, 84, 98),
  'English': ()
}

for course, grades in course_grades.items():
  average = get_average_grade(grades)
  if average is None:
    print(f"{course} course has no grades")
  else:
    print(f"The average grade for {course} is {average}")
