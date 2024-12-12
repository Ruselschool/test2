# Birthdays


bday = {}
choice = 0
def get_menu_choice():

    print("\n1. find birthday")
    print("2. add birthday")
    print("3. change birthday")
    print("4. delete birthday")
    print("5. display all birthdays")
    print("6. quit program\n")

    choice = int(input("enter your choice: "))
    while choice <1 or choice >6:
        choice = int(input("enter a valid choice: "))

    return choice

def find(bday):
    name = input("Enter name: ")
    # look up name in dictionary
    print(bday.get(name,"Name not found\n"))
    # found = False

    # outfile = open('birthdays.txt', 'r')
    # for line in outfile:
    #     name, bday_add = line.strip().split(', ')
    #     if name.lower() == name:
    #         print({name}, {bday_add})


def add(bday):
    name = input("enter a name: ")
    bday_add = input("enter a birthday: ")
    if name not in bday:
        bday[name]= bday_add
        # infile = open('birthdays.txt', 'a')
        # infile.write(name + ', ' + bday_add + ' ' + '\n')
        # infile.close()

    else:
        print("name already exists")

def change(bday):
    name = input("Enter a name: ")
    if name in bday:
        new_bday = input("Enter new birthday: ")
        bday[name]= new_bday

    else:
        print("Name not found\n")

def delete(bday):
    name = input("Enter a name: ")
    if name in bday:
        del bday[name]

    else:
        print("Name not found\n")

def display(bday):
    # outfile = open('birthdays.txt', 'r')
    # bday_all = outfile.read()
    print(bday)


def main(choice):
    while choice != 6:
        choice = get_menu_choice()

        if choice == 1:
            find(bday)

        elif choice ==2:
            add(bday)

        elif choice ==3:
            change(bday)

        elif choice ==4:
            delete(bday)

        elif choice == 5:
            display(bday)

main(choice)