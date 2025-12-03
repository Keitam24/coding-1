'My rock paper scissor game will be able to give an option to throw rock paper or scissors'
'It should also be able to process wins or losses'
'It should also be able to processs tie games and allow you to throw again after.'

'I be able to use integer data to process records.'
'I will be able to use inputs to choose my selection'
'I will be able to use if and or statements to process who wins and who loses.'
'I will be able to use strings to let the player know the game has started. '


def rps():
    labubu = ['rock', 'paper', 'scissor']
    print('Welcome to the RPS game!')
    print('Please select from the followiung options:' )
    print(' !. start game')
    print('2. game rules')
    print('3. quit')
    selection = int(input())
    if selection == 1:
        
        print('Please select a game mode: ')
        print('1. vs human')
        print('2. vs cpu')
        gamemode =int(input())
        if gamemode == 1:
            print('not out yet lol')
        else:
            print('starting game now')
            print('*******************************')
            print('throw something')
            print('1. rock')
            print('2. paper')
            print('3. scissors')
            userselection = input()
            cpuselection =  random.choice(labubu)

            
    elif selection == 2:
        print('Game rules...')
    elif selection == 3:
        print('I didnt want to play with you anyways.')        
    else:
        print('ERROR: Invalid selection.')


rps()              

# need a loop for menu lol
