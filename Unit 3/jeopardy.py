def theelevator():
    print ('Hello, floor do you want to go to?')
    print(' 1. first')
    print ('2. second')
    print ('3. third')
    print('4. fourth')
    select= int(input('Please choose your floor: '))
    if select == 1:
        floorone = str('Hello, welcome to the first floor')
        print(floorone)
        print('We have a pool and a sauna')
    elif select == 2:     
           secondfloor = str('Welcome to the second floor')
           print(secondfloor)
           

    elif select == 3:
         thirdfloor = str('Welcome to the third Floor')
         print(thirdfloor)
    elif select == 4:
         fourthfloor = str('Welcome to the fourth floor.')
         print(fourthfloor)


    else:
         print('Sorry, we dont recognize your input. Please input it again.')      


theelevator()    