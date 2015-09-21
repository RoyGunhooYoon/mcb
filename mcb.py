#!/usr/bin/python3

import shelve
import sys
import pyperclip

print('\nWelcome to mcb!\n')
print('Type help to see manual\n')

while True:
    args = input('>').split()

    commands = ['help', 'list', 'load', 'save', 'quit', 'delete', 'show']
    command = args[0]

    mcb_shelve = shelve.open('mcb')

    if command not in commands:
        print("Unknown command, type help to see list of available commands.")

    # Single command operations
    else:
        if command == 'quit':
            print('Bye')
            mcb_shelve.close()
            sys.exit()
        elif command == 'help':
            doc = open('help.txt')
            print(doc.read())
            doc.close()
        elif command == 'list':
            if len(mcb_shelve) > 0:
                for k in mcb_shelve:
                    print('Keyword: {}  Overview: {}'.format(k, mcb_shelve[k][:30] + '...'))
            else:
                print("Could not find any keywords. Use save command to store clipboard into database.")
        elif command == 'save':
            try:
                keyword = args[1]
                content = pyperclip.paste()
                if keyword in mcb_shelve:
                    ask = input("Key already exist. Do you want to override it? (y/n)")
                    if ask == 'y':
                        mcb_shelve[keyword] = pyperclip.paste()
                        print("Keyword override success. New content: {}"\
                            .format(content[:30] + '...'))
                    else:
                        print("Keyword override denied by user.")
                else:
                    mcb_shelve[keyword] = pyperclip.paste()
                    print("Clipboard successfully saved with keyword\nContent: {}"\
                        .format(content[:30] + '...'))
            except:
                print("Please supply a keyword name to store clipboard content.")
        elif command == 'load':
            try:
                keyword = args[1]
                if keyword in mcb_shelve:
                    pyperclip.copy(mcb_shelve[keyword])
                    print("Content successfully copied to clipboard ctrl + v to paste.")
                else:
                    print("Given keyword is not found. Type list to see available keywords.")
            except:
                print("Please supply keyword name to load stored clipboard.")
        elif command == 'delete':
            try:
                keyword = args[1]
                if keyword in mcb_shelve:
                    del mcb_shelve[keyword]
                    print("Keyword: {} and its content has been removed"\
                        .format(keyword))
                elif keyword == '*':
                    ask = input("Are you sure you want to delete all keywords and its contents?(y/n)")
                    if ask == 'y':
                        for keyword in mcb_shelve:
                            del mcb_shelve[keyword]
                        print("Deleted all keywords in database.")
                    else:
                        print("Request denied by user.")
                else:
                    print("There are no matching keyword to delete.")
            except:
                print("Please supply keyword name that is to be deleted.")
        elif command == 'show':
            try:
                keyword = args[1]
                if keyword in mcb_shelve:
                    print(mcb_shelve[keyword])
                else:
                    print("Given keyword is not found in database.")
            except:
               print("Please supply keyword name.") 

