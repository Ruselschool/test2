
infile = open("superbowlwinners.txt", 'r')

winner = infile.readline().rstrip('\n')

search = input('Enter a team to search: ')
numwin = []

while winner != "":
    teamname = winner.strip()

    if search == teamname:
        numwin.append(teamname)

    winner = infile.readline().rstrip('\n')

infile.close()

print(search, "has won a total of", len(numwin), "Super Bowl(s).")

while True:
    search = input('Enter another team to search (or type "quit" to exit): ')

    if search.lower() == 'quit':
        print("Exiting the program.")
        break

    infile = open("superbowlwinners.txt", 'r')
    numwin = []

    winner = infile.readline().rstrip('\n')
    while winner != "":
        teamname = winner.strip()

        if search == teamname:
            numwin.append(teamname)

        winner = infile.readline().rstrip('\n')

    infile.close()

    # Print the result for the new search
    if len(numwin) > 0:
        print(search, "has won a total of", len(numwin), "Super Bowl(s).")
    else:
        print("Team not found or has not won any Super Bowls.")