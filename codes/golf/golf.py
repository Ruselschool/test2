# golf program

def main():
    while True:
        print("\nMenu")
        print("1. Write to a file")
        print("2. Read from a file")
        print("3. Search for a player's scores")
        print("4. Quit")
        try:
            choice = int(input("Choice: "))
            if choice == 1:
                write()
            elif choice == 2:
                read()
            elif choice == 3:
                search_by_name()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Choice must be a number.")

def write():
    filename = input("\nEnter filename: ")
    try:
        infile = open(filename + '.txt', 'a')
        name = input("Enter player's name: ")
        date = input("Enter date: ")
        score = int(input("Enter player's score: "))
        infile.write(name + ', ' + date + ', ' + str(score) + '\n')
        print("Record added successfully.")
        infile.close()
    except ValueError:
        print("Invalid score. Please enter a number for the score.")
    except IOError:
        print("File error occurred.")

def read():
    try:
        filename = input("\nEnter filename: ").lower()
        outfile = open(filename + '.txt', 'r')
        name = outfile.readline()
        if not name:
            print("No records found.")
        while name != '':
            name, date, score = name.strip().split(', ')
            print(f"\nName: {name}")
            print(f"Date: {date}")
            print(f"Score: {score}")
            name = outfile.readline()
        outfile.close()
    except FileNotFoundError:
        print("File not found. Please add records first.")
    except Exception as e:
        print(f"An error has occurred: {e}")

def search_by_name():
    search_name = input("\nEnter the player's name: ").lower()
    found = False
    try:
        filename = input("Enter filename: ").lower()
        outfile = open(filename + '.txt', 'r')
        for line in outfile:
            name, date, score = line.strip().split(', ')
            if name.lower() == search_name:
                print(f"\nName: {name}, Date: {date}, Score: {score}")
                found = True
        if not found:
            print(f"No records found for player: {search_name}")
        outfile.close()
    except FileNotFoundError:
        print("File not found. Please add records first.")
    except Exception as e:
        print(f"An error has occurred: {e}")

main()