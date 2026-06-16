# ALAB 351.3 - Part 1.2

# For loop (for this case, for loop is more concise)
sum = 0
for i in range(1, 51):
  if i % 2 == 0:
    sum += i
print(f"For loop: The sum of even numbers from 1 to 50 is {sum}.")

# While loop
total = 0
count = 1
while count <= 50:
  if count % 2 == 0:
    total += count 
  count += 1
print(f"While loop: The sum of even numbers from 1 to 50 is {total}.")