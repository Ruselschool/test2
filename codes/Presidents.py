import random

presidents = {
"Biden": "Harris", "Trump": "Pence", "Obama": "Biden", "Bush Jr.": "Cheney", "Clinton": "Gore", "Bush Sr.": "Quayle","Regan": "Bush Sr.", "Carter": "Mondale", "Ford": "Rockefeller", "Nixon": "Ford", "Johnson": "Humphrey", "Kennedy": "Johnson", "Eisenhower": "Nixon", "Truman": "Barkley", "Franklin Roosevelt": "Truman", "Hoover": "Curtis", "Coolidge": "Dawes", "Harding": "Coolidge", "Wilson": "Marshall", "Taft": "Sherman", "Theodore Roosevelt": "Fairbanks"
}

correct = []
incorrect = []
score = 0

for i in range(10):
    huh = random.choice(list(presidents))
    guess = input("Who was "+huh+"'s VP? ")

    if guess.lower() == presidents[huh].lower():
        score += 1
        answer = correct.append(f"Correct: {huh} - {guess}")


    if guess.lower() != presidents[huh].lower():
        answer = incorrect.append(f"Incorrect: {huh} - {guess} Correct: {huh} - {presidents[huh]}") #

    del presidents[huh]

print("\nYour score is",score,"/10")

print()

for i in range(len(correct)):
    print(correct[i])

print()

for i in range(len(incorrect)):
    print(incorrect[i])