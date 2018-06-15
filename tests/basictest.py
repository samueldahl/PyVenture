from basictestworld import world
# print(world['start_room']['text'])
finished = False
location = 'start_room'
valid_paths = list(world[location]['exits'].keys())
print('\n\n\nWelcome to PyVenture Test')
print('This mostly exists to test Behave, a python test thingy.\n\n\n')


def print_location():
    return world[location]['text']
    # return the location text.


def get_valid_paths():
    paths = 'EXITS: '
    rawpaths = list(world[location]['exits'].keys())
    valid_paths = rawpaths
    a = 0
    while a < len(rawpaths):
        place = str(rawpaths[a])
        paths = paths + place + ', '
        a += 1
    return paths
    # needs refactor to use string methods to print locoations properly.


while finished == False:
    print(print_location() + '\n')
    print(get_valid_paths())
    # print(str(get_valad_paths()) + '\n')
    rawtext = input('\nWhere do ye goeth? ')
    if rawtext == "quit":
        finished = True
    elif rawtext == "q":
        finished = True
    else:
        if rawtext in valid_paths:
            location = world[location]['exits'][rawtext]
            valid_paths = list(world[location]['exits'].keys())
        else:
            print(valid_paths)
            print("\nI'm sorry, I didin't quite get that.\n")
            print(location)