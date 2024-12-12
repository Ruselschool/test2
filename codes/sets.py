# import random

#
# class Coin:
#     def __init__(self):
#         self.sideup="heads"
#
#     def toss(self):
#         flip = random.randint(0, 1)
#         if flip == 0:
#             self.sideup="heads"
#         else:
#             self.sideup="tails"
#
#     def get_sideup(self):
#         return self.sideup
#
# def main():
#     my_coin = Coin()
#     print(my_coin.get_sideup())
#     for i in range(10):
#         my_coin.toss()
#         print(my_coin.get_sideup())
#
# main()

#import random
#------------------------------------ bankaccount assingment---------------------------------------#
import pickle


customer = {}


class BankAccount:
   def __init__(self, balance):
       self.balance = balance


   def deposit(self, amount):
       self.balance += amount


   def withdraw(self, amount):
       self.balance -= amount


   def get_balance(self):
       return self.balance


def menu():
   print("\n1. Add customer")
   print("2. Look up customer")
   print("3. Edit customer")
   print("4. Deposit")
   print("5. Withdraw")
   print("6. Delete")
   print("7. Quit (and save changes)\n")


   while True:
       try:
           choice = int(input("Enter your choice: "))
           if 1 <= choice <= 7:
               return choice
           else:
               print("Please enter a valid choice (1-7).")

       except ValueError:
           print("Invalid input. Please enter a number between 1 and 7.")


def add_customer(customer):
   name = input("Enter customer name: ")

   if name in customer:
       print("Customer already exists.")

   else:
       initial_balance = float(input("Enter initial balance: "))
       savings = BankAccount(initial_balance)
       customer[name] = savings
       print(f"Customer '{name}' added with balance: ${savings.get_balance():,.2f}")


def look_up_customer(customer):
   name = input("Enter customer name: ")

   if name in customer:
       print(f"Customer: {name}, Balance: ${customer[name].get_balance():,.2f}")

   else:
       print("Customer not found.")


def edit_customer(customer):
   old_name = input("Enter the name of the customer to edit: ")

   if old_name in customer:
       new_name = input("Enter the new name: ")
       customer[new_name] = customer.pop(old_name)
       print(f"Customer name changed from '{old_name}' to '{new_name}'.")

   else:
       print("Customer not found.")


def deposit_to_account(customer):
   name = input("Enter customer name: ")

   if name in customer:
       amount = float(input("Enter amount to deposit: "))
       customer[name].deposit(amount)
       print(f"${amount:,.2f} deposited. New balance: ${customer[name].get_balance():,.2f}")

   else:
       print("Customer not found.")


def withdraw_from_account(customer):
   name = input("Enter customer name: ")
   if name in customer:
       amount = float(input("Enter amount to withdraw: "))
       if amount <= customer[name].get_balance():
           customer[name].withdraw(amount)
           print(f"${amount:,.2f} withdrawn. New balance: ${customer[name].get_balance():,.2f}")
       else:
           print("Insufficient funds.")

   else:
       print("Customer not found.")


def delete_customer(customer):
   name = input("Enter customer name to delete: ")
   if name in customer:
       del customer[name]
       print(f"Customer '{name}' deleted.")

   else:
       print("Customer not found.")


def save_data(customer):
   try:
       with open('customer_data.pkl', 'wb') as file:
           pickle.dump(customer, file)
       print("Customer data saved.")

   except Exception as e:
       print(f"Error saving data: {e}")


def load_data():
   try:
       with open('customer_data.pkl', 'rb') as file:
           return pickle.load(file)

   except FileNotFoundError:
       return {}

   except (EOFError, pickle.UnpicklingError):
       print("Data file is corrupted or empty. Starting with an empty customer list.")
       return {}


def main():
   customer = load_data()


   while True:
       choice = menu()


       if choice == 1:
           add_customer(customer)

       elif choice == 2:
           look_up_customer(customer)

       elif choice == 3:
           edit_customer(customer)

       elif choice == 4:
           deposit_to_account(customer)

       elif choice == 5:
           withdraw_from_account(customer)

       elif choice == 6:
           delete_customer(customer)

       elif choice == 7:
           save_data(customer)
           print("Goodbye!")
           break

main()