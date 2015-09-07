# --- main part of program ---#
#edit to make a to do list creator

FILENAME = 'list.txt' # define the filename used to store the list
lineList = getList(FILENAME) # call the getList function to read the file into a list

while True: # this endless loop displays the list and prompts the user for a command

    showList(lineList) # call showList to show the current content of the list

    # show the instructions for the possible commands - [a]dd, [d]elete, e[x]it
    print('\nType "a" to add an item.')

    if len(lineList) > 0: # only show the delete instruction if the list has items
        print('Type "d" to delete an item.')

    print('Type "x" to exit.')

    command = input('> ') # prompt for a command

    # if "a", calladdToList to prompt for item and add to list
    if command == 'a': 
        lineList = addToList(FILENAME, lineList)

    # if "d", call deleteFromList to prompt for item number and delete from list        
    elif command == 'd' and len(lineList) > 0:
        lineList = deleteFromList(FILENAME, lineList)

    elif command == 'x': # if "x", break out of the loop to end the program
        print('Goodbye!')
        break

    else: # if anything else, show an error message
        print('Invalid command.\n')
