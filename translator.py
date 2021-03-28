import json
from difflib import get_close_matches as GCM

# The try statement loads the json dataset only if it does not already exist.
try:
    data
except NameError:
    data = json.load(open('data.json'))


def definition(word):

    # This while statement activates only if the user's word is not found in the
    # ddataset and they don't want to exit the program.
    while word not in data and word.lower() != 'exit!':

        # This if statement breaks the flow out of the while loop only if the
        # reason the word wasn't found in the dataset is because it should be
        # capitalised or all-caps.
        if word.title() in data:
            word = word.title()
            break
        elif word.upper() in data:
            word = word.upper()
            break
        elif word.capitalize() in data:
            word = word.capitalize()
            break
        elif word.lower() in data:
            word = word.lower()
            break
        else:
            word = word.lower()

        # Iterable with every dataset's keys in lower case as elements.
        data_keys = list(map(str.lower, data.keys()))

        # Lsit of max 5 elements with at least 75% similarity to the user word.
        matches   = GCM(word, data_keys, n=5, cutoff=0.75)

        # This if statement activates if indeed there are some similar words.
        if len(matches) > 0:
            # This for statement checks each element in matches and if the
            # corresponding word in the dataset is in all-caps or capitalized,
            # it rewrites it that way, otherwise it keeps the lower case style.
            for i in range(len(matches)):
                try:
                    data[matches[i]]
                except:
                    try:
                        data[matches[i].title()]
                        matches[i] = matches[i].title()
                    except:
                        try:
                            data[matches[i].upper()]
                            matches[i] = matches[i].upper()
                        except:
                            data[matches[i]]

            # Displaying similarities to the user so they can choose.
            for i in range(len(matches)):
                if i == 0:
                    print('')
                print(f'\t{i+1}---{matches[i]}')

            selection = input('\nEither enter one of the words above, a new word or type "exit!" to exit dictionary: ')

            # This checks whether the user enters a number corresponding to an
            # available choice, or if they're searching another word instead.
            try:
                selection = int(selection)
                if selection in range(1,len(matches)+1):
                    word = matches[selection - 1]
                else:
                    print(f'\nIf you enter a number, it has to be from 1 to {len(matches)}')
            except:
                word = selection
        else:
            word = input('No close match found for the word you entered. Enter a new word or type "exit!" to exit the dictionary: ')

    if word.lower() == 'exit!':
        word_definition = ['Dictionary exited.\n']
    else:
        word_definition = [f'\nThe definition of \"{word}\" is:'] + data[word]

    # The definition() function returns a list. The first element is always a
    # message, concatenated with data[word] (which is also a list) if the word
    # definition was found.
    return word_definition

# This ensures that the the code keeps asking the user if they want to enter a new word.
while True:
    word    = input('Choose a word: ')
    # Saving the function's outcome to make it available in the next lines.
    outcome = definition(word)

    for i in range(len(outcome)):
        if i>0: nt = '\t'
        else: nt = ''
        print(f'{nt}{outcome[i]}')

    if outcome == ['Dictionary exited.\n']:
        break
    else:
        again = input('\nChoose another word? Y/N: ').lower()

        if again in ['n', 'no']:
            print('Dictionary exited.\n')
            break
        else:
            print('\nIf you do not want to continue, just write \"exit!\" below.')
