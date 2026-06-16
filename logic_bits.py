# ALAB 351.3 - Part 3

# Read values as text first (input() always returns strings).
user_input_1 = input("Enter any boolean character (True/False or 1/0): ")
user_input_2 = input("Enter a second boolean character (True/False or 1/0): ")

# logical operators (and, or, not)
# With strings, Python treats non-empty text as True and empty text as False.
and_result = user_input_1 and user_input_2
or_result = user_input_1 or user_input_2
# Store both NOT results as a tuple: (not first_input, not second_input).
not_result = not user_input_1, not user_input_2 
print(f"{user_input_1} AND {user_input_2} =", and_result)
print(f"{user_input_1} OR {user_input_2} =", or_result)
print(f"NOT {user_input_1}, NOT {user_input_2} =", not_result)

# bitwise operators (&, |, ^, ~, <<, >>)
# Convert text inputs to integers so bitwise operations can be applied.
user_input_1 = int(user_input_1)
user_input_2 = int(user_input_2)

# Use bin() to display integer results in binary form.
and_bit = user_input_1 & user_input_2
or_bit = user_input_1 | user_input_2
print("& bitwise operator", bin(and_bit))
print("| bitwise operator", bin(or_bit))
xor_bit = user_input_1 ^ user_input_2
print("^ bitwise operator", bin(xor_bit))
# ~ is bitwise NOT (two's complement representation for negative results).
not_bit_1 = ~user_input_1
not_bit_2 = ~user_input_2
print("~ bitwise operator", bin(not_bit_1), bin(not_bit_2))
# Shift left by 1 multiplies by 2 for non-negative integers.
left_shift_1 = user_input_1 << 1
left_shift_2 = user_input_2 << 1
print("<< bitwise operator", bin(left_shift_1), bin(left_shift_2))
# Shift right by 1 divides by 2 (floor division behavior for integers).
right_shift_1 = user_input_1 >> 1
right_shift_2 = user_input_2 >> 1
print(">> bitwise operator", bin(right_shift_1), bin(right_shift_2))
