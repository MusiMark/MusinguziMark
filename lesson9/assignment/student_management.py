from pathlib import Path
import csv
import json
import logging

# =====================================
# File Paths
# =====================================
CSV_FILE = Path("sample_students.csv")
JSON_FILE = Path("sample_students.json")
LOG_FILE = Path("student_system.log")

# =====================================
# Logging Configuration
# =====================================
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# =====================================
# Custom Exception
# =====================================
class StudentNotFoundError(Exception):
    """Raised when a student cannot be found."""
    pass


# =====================================
# Create files if they do not exist
# =====================================
def initialize_files():

    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Registration Number", "Name", "Age"])

    if not JSON_FILE.exists():
        JSON_FILE.write_text("{}", encoding="utf-8")


# =====================================
# Load JSON data
# =====================================
def load_json():
    with JSON_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


# =====================================
# Save JSON data
# =====================================
def save_json(data):
    with JSON_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# =====================================
# Add Student
# =====================================
def add_student():

    try:
        reg_no = input("Registration Number: ").strip()

        if not reg_no:
            raise ValueError("Registration Number cannot be empty.")

        name = input("Student Name: ").strip()

        if not name:
            raise ValueError("Student name cannot be empty.")

        age = int(input("Age: "))

        if age <= 0:
            raise ValueError("Age must be greater than zero.")

        address = input("Address: ").strip()
        contact = input("Contact: ").strip()
        program = input("Program: ").strip()

        # Check if student already exists
        with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if row[0] == reg_no:
                    print("Student already exists.")
                    return

        # Save basic details
        with CSV_FILE.open("a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([reg_no, name, age])

        # Save additional details
        students = load_json()

        students[reg_no] = {
            "Address": address,
            "Contact": contact,
            "Program": program
        }

        save_json(students)

        logging.info(f"Added student {reg_no}")

        print("\nStudent added successfully.")

    except ValueError as error:
        logging.error(error)
        print("Error:", error)

    finally:
        print("Add Student operation completed.\n")


# =====================================
# View Students
# =====================================
def view_students():

    try:

        students = load_json()

        with CSV_FILE.open("r", newline="", encoding="utf-8") as file:

            reader = csv.reader(file)
            next(reader)

            print("\n========== STUDENT RECORDS ==========")

            for row in reader:

                reg_no, name, age = row

                details = students.get(reg_no, {})

                print(f"\nRegistration Number : {reg_no}")
                print(f"Name                : {name}")
                print(f"Age                 : {age}")
                print(f"Address             : {details.get('Address', '')}")
                print(f"Contact             : {details.get('Contact', '')}")
                print(f"Program             : {details.get('Program', '')}")

        logging.info("Viewed all students.")

    except Exception as error:
        logging.error(error)
        print("Unable to display student records.")


# =====================================
# Search Student
# =====================================
def search_student():

    try:

        reg_no = input("Enter Registration Number: ").strip()

        students = load_json()

        found = False

        with CSV_FILE.open("r", newline="", encoding="utf-8") as file:

            reader = csv.reader(file)
            next(reader)

            for row in reader:

                if row[0] == reg_no:

                    found = True

                    print("\nStudent Found")
                    print("---------------------------")
                    print("Registration Number:", row[0])
                    print("Name:", row[1])
                    print("Age:", row[2])

                    details = students.get(reg_no, {})

                    print("Address:", details.get("Address"))
                    print("Contact:", details.get("Contact"))
                    print("Program:", details.get("Program"))

                    break

        if not found:
            raise StudentNotFoundError("Student not found.")

        logging.info(f"Searched student {reg_no}")

    except StudentNotFoundError as error:
        logging.error(error)
        print(error)


# =====================================
# Update Student
# =====================================
def update_student():

    try:

        reg_no = input("Registration Number: ").strip()

        rows = []

        found = False

        with CSV_FILE.open("r", newline="", encoding="utf-8") as file:

            reader = csv.reader(file)

            header = next(reader)

            for row in reader:

                if row[0] == reg_no:

                    found = True

                    row[1] = input("New Name: ")
                    row[2] = input("New Age: ")

                rows.append(row)

        if not found:
            raise StudentNotFoundError("Student not found.")

        with CSV_FILE.open("w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(header)

            writer.writerows(rows)

        students = load_json()

        students[reg_no] = {
            "Address": input("New Address: "),
            "Contact": input("New Contact: "),
            "Program": input("New Program: ")
        }

        save_json(students)

        logging.info(f"Updated student {reg_no}")

        print("Student updated successfully.")

    except StudentNotFoundError as error:
        logging.error(error)
        print(error)


# =====================================
# Delete Student
# =====================================
def delete_student():

    try:

        reg_no = input("Registration Number: ").strip()

        rows = []

        found = False

        with CSV_FILE.open("r", newline="", encoding="utf-8") as file:

            reader = csv.reader(file)

            header = next(reader)

            for row in reader:

                if row[0] == reg_no:

                    found = True

                else:

                    rows.append(row)

        if not found:
            raise StudentNotFoundError("Student not found.")

        with CSV_FILE.open("w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(header)

            writer.writerows(rows)

        students = load_json()

        students.pop(reg_no, None)

        save_json(students)

        logging.info(f"Deleted student {reg_no}")

        print("Student deleted successfully.")

    except StudentNotFoundError as error:
        logging.error(error)
        print(error)


# =====================================
# Menu
# =====================================
def menu():

    initialize_files()

    while True:

        print("\n===================================")
        print(" STUDENT RECORD MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            logging.info("Program closed.")
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please try again.")


# =====================================
# Program Entry
# =====================================
if __name__ == "__main__":
    menu()