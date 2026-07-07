# ALAB 356.1
# Task 1: Using Built-in Modules
import math, random, platform

random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
print(f"Square Root (floored): {math.floor(math.sqrt(random_number))}")
print(f"Operating System: {platform.system()}")
print(f"Python version: {platform.python_version()}")