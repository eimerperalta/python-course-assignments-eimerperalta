# ALAB 351.3 - Part 2

my_list = [64, 25, 12, 22, 11] # list to sort
print(f"Original list: {my_list}")


print("performing bubble sorting algorithm on the list...")
swapped = True # Switch needed to enter the loop

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # swap
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    print(my_list)

print(f"Final list: {my_list}")

