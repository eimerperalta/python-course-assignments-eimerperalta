# ALAB 356.2
# Task 2: List Management with Error Handling

def display_menu():
    """Prints the main menu options to the console."""
    print("\n" + "="*30)
    print("      List Manager")
    print("="*30)
    print("1. Add a number")
    print("2. Remove a number")
    print("3. Display the list")
    print("4. Quit")
    print("="*30)

def add_number(lst):
    try:
        number_to_add = int(input("Enter an integer to add to the list: "))
        lst.append(number_to_add) # adding number to list
        print(f"'{number_to_add}' has been added to the list!")
    except ValueError:
        print("Error: wrong input (add_number)")
    except Exception:
        print("Unknown Error (add_number)")

def remove_number(lst):
    try:
        index_to_delete = int(input("Enter the index of the number you'd like to remove from the list: "))
        print(f"Deleting {lst[index_to_delete]} at position {index_to_delete}")
        lst.pop(index_to_delete)
        print(f"Number successfully deleted!")
    except IndexError:
        print("Error: index out of range (remove_number)")
    except ValueError:
        print("Error: wrong input (remove_number)")
    except Exception:
        print("Unknown Error (remove_number)")

def print_list(lst):
    print(f"[Current list]\n {lst}")

def main():
    lst = []
    while True:
        display_menu()
        
        # Grab user menu option
        try:
            user_choice = int(input("Please select a menu option (1-4): "))
        except ValueError:
            print("Error: wrong input") # Input must be an integer
            continue
        
        # Validate user choice range
        if user_choice < 1 or user_choice > 4:
            print("Error: please select a valid menu option (from 1 to 4)")
            continue

        # Quit program
        if user_choice == 4:
            print("Quitting List Manager program. Bye!")
            break
        
        # Print current list
        elif user_choice == 3:
            print_list(lst)
        
        # Remove number from list
        elif user_choice == 2:
            remove_number(lst)
        
        # Add number to list
        elif user_choice == 1:
            add_number(lst)
        

if __name__ == "__main__":
    main()