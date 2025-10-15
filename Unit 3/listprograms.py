thanksgiving = ['Mac and Cheese', 'Turkey', 'Mashed Potatoes', 'Collard Greens']

print(thanksgiving[0])
print(thanksgiving[3])
thanksgiving[3] = 'Stuffing'

print(thanksgiving) 

thanksgiving.pop(1)
thanksgiving.pop(2)
print(thanksgiving)


def todaysmeal():
    print ('Hello, what time of day is it today?')
    print(' 1. morning')
    print ('2. afternoon')
    print ('3. evening')
    select= int(input('Please choose the time: '))
    if select == 1:
        morningmenu = ['Panini', 'Bagel', 'Bacon egg and cheese']
        print(morningmenu)
        print('It is morning, please choose an item')
    elif select == 2:     
           lunchmenu = ['Hoagie', 'Pizza', 'Wing combo']
           print(lunchmenu)
           print('It is afternoon, please choose an item for lunch')

    elif select == 3:
         dinnermenu = ['Soup',  'Steak and fries', 'Chicken Alfredo']
         print(dinnermenu)
         print('It is evening, please choose an item for dinner')

    else:
         print('Sorry, we dont recognize your input. Please input it again.')      


todaysmeal()    