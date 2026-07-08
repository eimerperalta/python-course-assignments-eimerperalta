# ALAB 356.2
# Task 1: String Manipulation Challenge
user_sentence = input("Please enter a sentence: ")

# Uppercase
print("Uppercase:\n", user_sentence.upper())

# Reversed
print("Reversed:\n", user_sentence[::-1])

# Counts number of vowels in sentence
vowels = ["a", "e", "i", "o", "u"]
vowel_count = sum(1 for char in user_sentence.lower() if char in vowels) # Using list comprenhension; a regular for loop can be used too.
print(f"Number of vowels found:\n {vowel_count} vowels")

# Replaces whitespace with hyphen (-)
print(f"Spaces replaced with hyphen:\n {user_sentence.replace(' ', '-')}")
