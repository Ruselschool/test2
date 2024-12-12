import random
import pickle

employees = {}

def add_employee():
   name = input("Enter employee name: ")
   department = input("Enter department: ")
   job_title = input("Enter job title: ")
   emp_id = random.randint(10000, 99999)
   employees[emp_id] = {"name": name, "department": department, "job_title": job_title}
   print(f"Employee added with ID: {emp_id}")


def look_up_employee():
   emp_id = input("Enter Employee ID: ")
   emp_id = int(emp_id)
   if emp_id in employees:
       emp = employees[emp_id]
       print(f"Name: {emp['name']}, ID: {emp_id}, Department: {emp['department']}, Job Title: {emp['job_title']}")
   else:
       print("Employee not found.")


def edit_employee():
   emp_id = input("Enter Employee ID to edit: ")
   emp_id = int(emp_id)
   if emp_id in employees:
       employees[emp_id]["name"] = input("Enter new name: ")
       employees[emp_id]["department"] = input("Enter new department: ")
       employees[emp_id]["job_title"] = input("Enter new job title: ")
       print("Employee updated.")
   else:
       print("Employee not found.")


def delete_employee():
   emp_id = input("Enter Employee ID to delete: ")
   emp_id = int(emp_id)
   if emp_id in employees:
       del employees[emp_id]
       print("Employee deleted.")
   else:
       print("Employee not found.")


def view_all_employees():
   if not employees:
       print("\nNo employees found.")
   else:
       print("\nEmployee Information:")
       i = 1
       for emp_id, emp in employees.items():
           print(f"Employee {i}: Name: {emp['name']}, ID: {emp_id}, Department: {emp['department']}, Job Title: {emp['job_title']}")
           i += 1


def menu():
   print("\n1. Add Employee")
   print("2. Look Up Employee")
   print("3. Edit Employee")
   print("4. Delete Employee")
   print("5. View All Employees")
   print("6. Quit\n")
   return int(input("Enter your choice: "))


def save_data():
   with open("employees.pkl", "wb") as file:
       pickle.dump(employees, file)


def load_data():
   try:
       with open("employees.pkl", "rb") as file:
           return pickle.load(file)
   except (FileNotFoundError, EOFError):
       return {}


def main():
   global employees
   employees = load_data()
   while True:
       choice = menu()
       if choice == 1:
           add_employee()
       elif choice == 2:
           look_up_employee()
       elif choice == 3:
           edit_employee()
       elif choice == 4:
           delete_employee()
       elif choice == 5:
           view_all_employees()
       elif choice == 6:
           save_data()
           print("Goodbye")
           break


main()