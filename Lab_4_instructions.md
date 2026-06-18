# Lab 4: Functions, Tuples, Dictionaries, and Exceptions

## Overview and Objectives

In this lab, you will create and use functions, including those that take parameters and return values. You will also work with Python tuples and dictionaries, and handle exceptions in simple scenarios. These tasks integrate several concepts to solidify your understanding of how larger programs are structured. By completing this lab, you will be able to:

- Define and call functions with and without parameters.
- Use return values from functions and understand scope (local vs global variables).
- Work with tuples (immutable sequences) and dictionaries (key-value pairs).
- Handle exceptions using try/except blocks to catch errors or unexpected conditions.
- Write a program that uses all these concepts in combination for data processing.

## Instructions and Tasks

### Part 1: Writing and Using Functions

Write a script `basic_functions.py` that defines and uses simple functions:

1. Define a function `greet_user()` that takes a name (string) as a parameter and prints a greeting, e.g., `"Hello, <name>! Welcome!"`. If no name is provided (you can simulate this by calling `greet_user()` with an empty string or by using a default parameter value), it should print `"Hello! Welcome!"`.
2. Define a function `add_two_numbers(a, b)` that returns the sum of two numbers `a` and `b`.
3. Define a function `is_even(num)` that returns `True` if `num` is even or `False` otherwise.
4. In the main part of the script (outside the functions), demonstrate each function:
   - Call `greet_user()` with a sample name and without a name.
   - Call `add_two_numbers()` with two numbers, print the result.
   - Call `is_even()` on a couple of numbers (one even, one odd) and print the results in a descriptive way (e.g., `"4 is even: True"`).

Include comments explaining what each function is intended to do. Use appropriate return statements for functions 2 and 3, and show that the returned values can be stored in variables or used in expressions.

Create a script `calc_with_functions.py` that refactors the calculator from Module 2 (Task 2.3) using functions:

- Write separate functions for each operation: `add(a,b)`, `subtract(a,b)`, `multiply(a,b)`, `divide(a,b)` – each returning the result.
- Write a `calculate(a, b, op)` function that takes two numbers and a symbol for operation, and uses if/elif to call the correct operation function. It should handle an invalid operation by returning or printing an error message.
- In the main program, ask the user for two numbers and an operation (just like before), but now use the `calculate` function to get the result and print it.
- Add exception handling to gracefully handle errors such as division by zero or invalid numeric input. Use `try/except` around the input conversion and the division operation at minimum.

This task will demonstrate functions calling other functions and basic exception handling.

### Part 2: Tuples and Dictionaries

Write a script `tuples_dicts.py` that:

1. Creates a tuple `months` containing the names of the twelve months.
2. Prints the first and last month from the tuple (index 0 and index -1).
3. Attempts to modify the tuple (e.g., `months[0] = "NewMonth"`) inside a try/except block to demonstrate that tuples are immutable. Catch the exception and print a message like: `"Tuples are immutable, error: <error_message>"`.
4. Creates a dictionary `students` where keys are student names and values are their grades (choose 3-5 sample name-grade pairs).
5. Adds a new student and grade to the dictionary, then prints all student names and grades.
6. Updates one of the existing student’s grades, then prints the updated entry.
7. Uses a loop to print out each student’s name and grade in a formatted way, e.g., `"Alice: 90"`.

Create a script `data_processing.py` that simulates a simple data processing scenario:

- Define a function `get_average_grade(grades_tuple)` that takes a tuple of numeric grades and returns the average. Include a try/except to handle the case if the tuple is empty (to avoid division by zero), returning None or printing a warning in that case.
- Define a dictionary `course_grades` where keys are course names (e.g., "Math", "Science", "History") and values are tuples of grades.
- Use a loop to iterate over `course_grades`. For each course, call `get_average_grade(grades_tuple)` and print a message like: `"The average grade for Math is 85.2"`. Handle any None values or exceptions gracefully.
- Intentionally include an edge case, such as one course having an empty tuple of grades, to demonstrate your exception handling works.

### Part 3: Exception Handling (Additional Focus)

Write a script `exception_demo.py` that contains the following:

- A function `safe_divide(a, b)` that returns the result of `a / b` if `b` is not zero. If `b` is zero, the function should raise a `ValueError` with a message like "Cannot divide by zero".
- Use a try/except structure to call `safe_divide` with some test values that include a zero divisor. Catch the ValueError and print an error message to the user.
- Include a `finally` clause in the try/except that prints a message like "Division operation completed" whether or not an error occurred.
- Also demonstrate catching a generic exception by performing an unsafe operation (for example, converting an invalid string to int in a try block) and catching the generic `Exception` to print a message.

This will showcase your understanding of raising and catching exceptions.

## Submission

Submit all required scripts: `basic_functions.py`, `calc_with_functions.py`, `tuples_dicts.py`, `data_processing.py`, and `exception_demo.py` via a link to a single GitHub repository containing all the files.. Provide sample outputs and any notes on what you learned in each part, especially noting how exceptions were caught and handled. Ensure all code is well-commented to explain functions, parameters, return values, and exception handling.

## Grading Rubric

The total points for this lab is 60 points.

| **File**                   | **Criteria**              | **Points** | **Description**                                                                                                                                                                                                                        |
| -------------------------- | ------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **basic_functions.py**     | Function Definitions      | 6          | All three functions (`greet_user`, `add_two_numbers`, `is_even`) are defined correctly with proper parameters and functionality. `greet_user` handles a missing name (via default parameter or logic).                                 |
| **basic_functions.py**     | Function Calls and Output | 3          | Each function is called and demonstrated correctly in the script, and the output is as expected (greeting, sum, even check results).                                                                                                   |
| **basic_functions.py**     | Clarity and Style         | 3          | Code is well-structured with comments explaining each function’s purpose and proper use of return values for `add_two_numbers` and `is_even`.                                                                                          |
| **calc_with_functions.py** | Operation Functions       | 6          | Four basic operation functions (`add`, `subtract`, `multiply`, `divide`) are correctly implemented and return the correct result.                                                                                                      |
| **calc_with_functions.py** | Calculate Function        | 3          | The `calculate(a, b, op)` function correctly calls the appropriate operation or handles invalid operation symbols.                                                                                                                     |
| **calc_with_functions.py** | Integration and I/O       | 3          | The main program successfully takes input, uses `calculate` to get a result, and prints the result.                                                                                                                                    |
| **calc_with_functions.py** | Exception Handling        | 6          | The program gracefully handles division by zero and invalid inputs with user-friendly error messages.                                                                                                                                  |
| **tuples_dicts.py**        | Tuple Usage               | 3          | The tuple of months is created and accessed correctly (first and last elements printed).                                                                                                                                               |
| **tuples_dicts.py**        | Immutability Demo         | 3          | An attempt to modify the tuple correctly raises an exception that is caught, with an explanatory message printed.                                                                                                                      |
| **tuples_dicts.py**        | Dictionary Operations     | 6          | The dictionary of students is created and modified correctly: a new item is added, an existing item is updated, and all items are printed in a clear format using a loop.                                                              |
| **data_processing.py**     | Function for Average      | 3          | The `get_average_grade` function is correctly implemented to calculate the average of grades in a tuple and handles empty tuples appropriately.                                                                                        |
| **data_processing.py**     | Data Structure            | 3          | The `course_grades` dictionary is correctly set up with courses as keys and tuples of grades as values, including at least one empty tuple edge case.                                                                                  |
| **data_processing.py**     | Loop and Output           | 3          | Looping over the dictionary and printing average grades is done correctly; messages are clear and handle empty cases gracefully.                                                                                                       |
| **data_processing.py**     | Error Handling            | 3          | The script properly demonstrates error handling (using try/except) for empty data or other issues without crashing.                                                                                                                    |
| **exception_demo.py**      | Custom Exception Raise    | 3          | The `safe_divide` function correctly raises a `ValueError` when attempting to divide by zero.                                                                                                                                          |
| **exception_demo.py**      | Try/Except/Finally Usage  | 3          | The try/except block catches the `ValueError` and prints an error message, with a finally clause that prints a completion message. Also, a generic exception is caught in another scenario to demonstrate understanding of error flow. |

> [!NOTE]
>
> Each task section will be graded for both correctness and the quality of code and explanations. Partial credit is possible for incomplete implementations that show understanding. For example, if the calculator functions are written but exception handling is not fully correct, some points under Exception Handling can be awarded if an attempt is made. Code that is commented and easy to follow will score higher in clarity categories. Overall, well-structured and tested code with clear output and handling of edge cases will receive full credit.
