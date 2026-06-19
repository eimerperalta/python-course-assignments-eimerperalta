# SBA 351 - Python Essentials 1
# Contact Book (dictionary)

# dictionary to store contact names and phone numbers (with sample data)
contact_book = { 
  'john': '3471234567',
  'alice': '18001234567',
  'tom': '9299876543'
}

# function to add a new contact to the contact book
def add_contact(name="", phone=""):
  if not name:
    name = input("\nEnter new contact's name: ")
  if not phone:
    phone = input("Enter new contact's phone: ")
  if not name or not phone:
    print("\ncontact name and phone must not be empty.")
    return None
  if name in contact_book: # check if contact already exists
    print("\nThis contact already exists in the Contact Book")
    return None
  else:
    contact_book[name] = phone # add new contact to the dictionary
    print(f"\nNew contact added to the Contact Book: {name} -> {contact_book[name]}")

# function to view all contacts in the contact book
def view_contacts():
  if contact_book == {}: # check if the contact book is empty
    print("Contact list is empty")
    return None
  print("\nAll contacts:")
  for name in sorted(contact_book): # sorted() function to sort the contact names alphabetically
    print(f"{name}: {contact_book[name]}")

# function to search for a contact in the contact book
def search_contact(name=""):
  try:
    if name == "":
      name = input("\nEnter contact's name: ")
      print(f"\n{name}: {contact_book[name]}")
    else:
      print(f"\n{name}: {contact_book[name]}")
  except KeyError: # if the contact name is not found in the dictionary, a KeyError will be raised
    print(f"\nNo entry found for contact: '{name}'")

# function to delete a contact from the contact book
def delete_contact(name=""):
  if name == "":
    name = input("Enter contact's name: ")
  if name == "":
    print("Contact name cannot be empty")
    return None

  try:
    contact_book.pop(name) # 'del contact_book[name]' can also be used
    if name not in contact_book:
      print(f"\nContact '{name}' successfully removed from the Contact Book")
    else:
      print(f"\nError: could not remove contact: {name}")
  except KeyError: # if the contact name is not found in the dictionary, a KeyError will be raised
    print(f"\nNo entry found for contact: '{name}'")

def show_menu():
  print(
    "\nContact Book Menu:\n"
    "1. Add New Contact\n"
    "2. View All Contacts\n"
    "3. Search Contact\n"
    "4. Delete Contact\n"
    "5. Exit"
  )

# main function to run the contact book application
def main():
  while True:
    try:
      show_menu()
      user_selection = str(input("Enter your choice (1-5): "))
    except:
      print("Error in menu:")
      break
    try: # handle user selection and call the appropriate function
      if user_selection == '1':
        add_contact()
      elif user_selection == '2':
        view_contacts()
      elif user_selection == '3':
        search_contact()
      elif user_selection == '4':
        delete_contact()
      elif user_selection == '5':
        print("Bye!\n")
        break
      else: # handle invalid menu selection
        print("Invalid option. Please select a valid menu option (1-5)")
    except Exception as error: # catch any unexpected errors that may occur during function execution
      print(f"Error: {error}")

if __name__ == "__main__":
  main()