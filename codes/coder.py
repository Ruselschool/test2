
# code_val = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f":6, "g": 7, "h":8,"i": 9, "j": 10, "k": 11, "l": 12, "m":13, "n": 14, "o":15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, " ": 196}
#
#
# #def menu():
#     # print("1. code text")
#     # print("2. uncode text")
#     #
#     # choice = int(input("enter choice: "))
#     # while choice != 1 and choice != 2:
#     #     choice = int(input("enter valid choice: "))
#     #
#     # return choice
#
# def code(code_val):
#     code_this=input("Enter message: ")
#     for char in code_this:
#         letter = code_val[char]
#         print(letter, end=' ')
#     print()
#     return letter
#
# def uncode(code_val,letter):
#     uncode_this = input("Enter coded message: ")
#     for key,value in code_val.items():
#         if value == letter:
#             print(key)
#
# def main(codeV):
#     print("1. code text")
#     print("2. uncode text")
#
#
#     # return choice
#
#     while True:
#         # try:
#             choice = int(input("enter choice: "))
#             while choice != 1 and choice != 2:
#                 choice = int(input("enter valid choice: "))
#
#             if choice ==1:
#                 code(codeV)
#             elif choice ==2:
#                 uncode(codeV)
#             elif choice ==3:
#                 break
#
#
#         # except ValueError:
#         #     print("Choice must be a number.")
# #selection = menu()
# main(code_val)

#----------------------------- This one works ----------------------------

code_val = {
    "a": "1", "b": "2", "c": "3", "d": "☺", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9",
    "j": "10", "k": "11", "l": "12", "m": "13", "n": "14", "o": "15", "p": "16", "q": "17",
    "r": "18", "s": "19", "t": "20", "u": "21", "v": "22", "w": "23", "x": "24", "y": "25",
    "z": "26", " ": "196", ".": "27", ",": "28", "!": "29", "?": "30"
}


def read(message, code):
    encoded_message = ''
    for char in message:
        if char in code:
            encoded_message += code[char] + " "
    print("Encoded Message:", encoded_message)
    return encoded_message


def decode(encoded_message, code):
    decoded_message = ''
    coded_symbols = encoded_message.split()

    for char in coded_symbols:
        for key, value in code.items():
            if char == value:
                decoded_message += key
                break

    print("Decoded Message:", decoded_message)


def main():
    while True:
        print("\nMenu")
        print("1. Code a message")
        print("2. Decode a message")
        print("3. Quit")

        try:
            choice = int(input("Enter: "))
            while choice < 1 or choice > 3:
                choice = int(input("Re-enter selection: "))

            if choice == 1:
                message = input("Enter your message to encode: ").lower()
                read(message, code_val)
            elif choice == 2:
                encoded = input("Enter the encoded message (space separated): ")
                decode(encoded, code_val)
            elif choice == 3:
                print("Exiting program.")

                break

        except ValueError:
            print("\n|Choice must be a number|\n")
main()