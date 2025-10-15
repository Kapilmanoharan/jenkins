# Simple Hospital Management System in Python

patients = []

def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    disease = input("Enter patient's disease/condition: ")

    patient = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Disease": disease
    }
    patients.append(patient)
    print(f"\n Patient '{name}' added successfully.\n")

def view_patients():
    if not patients:
        print("\n No patient records found.\n")
        return
    print("\n Patient Records:")
    for idx, p in enumerate(patients, start=1):
        print(f"{idx}. Name: {p['Name']}, Age: {p['Age']}, Gender: {p['Gender']}, Disease: {p['Disease']}")
    print()

def search_patient():
    name = input("Enter name to search: ")
    found = False
    for p in patients:
        if p['Name'].lower() == name.lower():
            print(f"\n Found: Name: {p['Name']}, Age: {p['Age']}, Gender: {p['Gender']}, Disease: {p['Disease']}\n")
            found = True
            break
    if not found:
        print(f"\n No patient found with name '{name}'.\n")

def delete_patient():
    name = input("Enter name of patient to delete: ")
    for p in patients:
        if p['Name'].lower() == name.lower():
            patients.remove(p)
            print(f"\n Patient '{name}' deleted successfully.\n")
            return
    print(f"\n No patient found with name '{name}'.\n")

def menu():
    while True:
        print("=== Hospital Management System ===")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            print("\n Exiting... Goodbye!")
            break
        else:
            print("\n Invalid choice. Please try again.\n")

# Run the program
menu()
