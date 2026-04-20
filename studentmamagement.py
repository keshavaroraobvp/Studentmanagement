students = []

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    marks = float(input("Enter Marks: "))
    
    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }
    
    students.append(student)
    print("Student added successfully!\n")


# Function to view students
def view_students():
    if not students:
        print("⚠️ No students found!\n")
        return
    
    print("\n--- Student List ---")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
    print()


# Function to search student
def search_student():
    roll = input("Enter Roll No to search: ")
    
    for s in students:
        if s["roll"] == roll:
            print(f" Found: {s}")
            return
    
    print("Student not found!\n")


# Function to delete student
def delete_student():
    roll = input("Enter Roll No to delete: ")
    
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print(" Student deleted successfully!\n")
            return
    
    print(" Student not found!\n")


# Main menu function
def menu():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice!\n")


# Run program
menu()