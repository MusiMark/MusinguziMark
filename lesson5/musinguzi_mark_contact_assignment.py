contacts = {}

# Task 1 Helpers
def is_valid_phone(phone):
    allowed = "0123456789-+"
    for char in phone:
        if char not in allowed:
            return False
    return True


def is_valid_email(email):
    if email == "":
        return True
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True

# CRUD Functions
def add_contact(name, phone, email=""):
    # Validate phone
    if not is_valid_phone(phone):
        print(f"  [Error] Invalid phone number '{phone}'.")
        print("  Phone may only contain digits, hyphens, and '+'.")
        print("  Operation cancelled.")
        return

    # Validate email
    if not is_valid_email(email):
        print(f"  [Error] Invalid email '{email}'.")
        print("  Email must contain '@' and '.'.")
        print("  Operation cancelled.")
        return

    if name in contacts:
        print(f"  [Error] A contact named '{name}' already exists.")
        return

    contacts[name] = {"phone": phone, "email": email}
    print(f"  Contact '{name}' added successfully.")


def view_contact(name):
    if name not in contacts:
        print(f"  [Error] No contact found with name '{name}'.")
        return

    info = contacts[name]
    print("Contact Details".center(10,"~"))
    print(f"  Name  : {name}")
    print(f"  Phone : {info['phone']}")
    print(f"  Email : {info['email'] if info['email'] else 'N/A'}")
    print("~"*10)

def update_contact(name, new_phone=None, new_email=None):
    if name not in contacts:
        print(f"  [Error] No contact found with name '{name}'.")
        return

    # Validate and update phone if a new one was provided
    if new_phone is not None:
        if not is_valid_phone(new_phone):
            print(f"  [Error] Invalid phone number '{new_phone}'.")
            print("  Phone may only contain digits, hyphens, and '+'.")
            print("  Operation cancelled.")
            return
        contacts[name]["phone"] = new_phone

    # Validate and update email if a new one was provided
    if new_email is not None:
        if not is_valid_email(new_email):
            print(f"  [Error] Invalid email '{new_email}'.")
            print("  Email must contain '@' and '.'.")
            print("  Operation cancelled.")
            return
        contacts[name]["email"] = new_email

    print(f"  Contact '{name}' updated successfully.")


def delete_contact(name):
    if name not in contacts:
        print(f"  [Error] No contact found with name '{name}'.")
        return

    del contacts[name]
    print(f"  Contact '{name}' deleted successfully.")


# Task 2 – Advanced Search (name, phone, and email)
def search_contacts(query):
    query_lower = query.lower()
    results = []

    for name, info in contacts.items():
        name_match  = query_lower in name.lower()
        phone_match = query_lower in info["phone"]
        email_match = query_lower in info["email"].lower()

        if name_match or phone_match or email_match:
            results.append((name, info["phone"], info["email"]))

    # Clean display
    if len(results) == 0:
        print(f"  No contacts found matching '{query}'.")
        return

    print(f"\n  Search results for '{query}'  ({len(results)} found)")
    print("  " + "-" * 52)
    print(f"  {'Name':<20} {'Phone':<15} {'Email'}")
    print("  " + "-" * 52)
    for name, phone, email in results:
        email_display = email if email else "N/A"
        print(f"  {name:<20} {phone:<15} {email_display}")
    print("  " + "-" * 52)


def list_all_contacts():
    if len(contacts) == 0:
        print("  No contacts saved yet.")
        return

    print(f"\n  All Contacts  ({len(contacts)} total)")
    print("  " + "-" * 52)
    print(f"  {'Name':<20} {'Phone':<15} {'Email'}")
    print("  " + "-" * 52)
    for name, info in contacts.items():
        email_display = info["email"] if info["email"] else "N/A"
        print(f"  {name:<20} {info['phone']:<15} {email_display}")
    print("  " + "-" * 52)


# Task 3 – Interactive CLI Menu
def main():

    while True:
        print("Contact Manager Menu".center(15,"="))
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            print("\n  -- Add Contact --")
            name  = input("  Enter name  : ").strip()
            phone = input("  Enter phone : ").strip()
            email = input("  Enter email (press Enter to skip): ").strip()
            add_contact(name, phone, email)

        elif choice == "2":
            print("\n  -- View Contact --")
            name = input("  Enter name to view: ").strip()
            view_contact(name)

        elif choice == "3":
            print("\n  -- Update Contact --")
            name  = input("  Enter name to update: ").strip()
            phone = input("  New phone (press Enter to keep current): ").strip()
            email = input("  New email (press Enter to keep current): ").strip()

            new_phone = phone if phone != "" else None
            new_email = email if email != "" else None
            update_contact(name, new_phone, new_email)

        elif choice == "4":
            print("\n  -- Delete Contact --")
            name    = input("  Enter name to delete: ").strip()
            confirm = input(f"  Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                delete_contact(name)
            else:
                print("  Deletion cancelled.")

        elif choice == "5":
            print("\n  -- Search Contacts --")
            query = input("  Enter search term (name, phone, or email): ").strip()
            search_contacts(query)

        elif choice == "6":
            list_all_contacts()

        elif choice == "7":
            print("\n  Goodbye! Exiting Contact Manager.")
            break

        else:
            print("  [Error] Invalid option. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()