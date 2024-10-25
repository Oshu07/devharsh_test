import csv
import os

file_path = 'users.csv'

if not os.path.exists(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone Number"]) 

def add_user():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone_number = input("Enter Phone Number: ")
    
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone_number])

    print("User added successfully!\n")

def display_users():
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) <= 1:
            print("No users found.\n")
        else:
            print("\nStored Users:")
            for row in rows[1:]:  
                print(f"Name: {row[0]}, Email: {row[1]}, Phone Number: {row[2]}")
            print()

def main():
    while True:
        print("Select an option:")
        print("1. Add User")
        print("2. Display Users")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_user()
        elif choice == '2':
            display_users()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()