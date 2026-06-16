# ALAB 351.3 - Part 2

my_list = [9, 8, 7, 3, 4, 5]
print("Original list:", my_list)

print("Using sorted() function:", sorted(my_list))

my_list = [6, 7, 1, 2, 3, 4, 5]
print("New list:", my_list)
my_list.sort()
print("Using sort() method:", my_list)

my_list.append(10)
print("appended new element:", my_list)

my_list.pop()
print("popped last element:", my_list)

my_list.reverse()
print("Reversed list:", my_list)