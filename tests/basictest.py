from basictestworld import world
# print(world['start_room']['text'])
finished = False
location = 'start_room'

print('\n\n\nWelcome to PyVenture Test')
print('This mostly exists to test Behave, a python test thingy.\n\n')



def print_location():
    return world[location]['text']
    # return the location text.

def print_exits():
    output = 'EXITS: '
    for i in world[location]['exits']:
        output = output + world[location]['exits'][i]
        output = output + ' '
    return output



while finished == False:
    print(print_location() + '\n')
    print(print_exits() + '\n')
    rawtext = input('What do ye doeth? ')
    if rawtext == "quit":
        finished = True
    elif rawtext == "q":
        finished = True
    else:
        if rawtext == "dank memes":
            print("dank dreams")
            finished = True
