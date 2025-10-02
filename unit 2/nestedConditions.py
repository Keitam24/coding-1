# Nested Conditions = Are if/ else blocks of code, that contain more if/else blocks of code- conditions that have conditions.

def dunkindonuts():
    print('Welcome to Dunkin Donuts. What would u like?')
    print('1. hot drinks.')
    print('2. cold drinks')
    print('3. snacks')
    print('4. hot food')
    select = int(input('What would you like? Please enter a number.'))
    if select == 1:
        print ('here is our hot drink menu')
        print ('coffee')
        print('tea')
        print('latte')
        drink = input('Select a drink. ')
        if drink == 1:
            print('Would you like a s. m. L')
        if drink == 2:
            print('What flavor would you like?')
            print("1. peach")
            print('2. green') 
            print ('3. Earl gray')
           

    elif select == 2:
        print ('here is our cold drink menu')
        print ('ice coffee')
        print('ice tea')
        print('frappichino')
    else:
        print('We dont have that dude')


# dunkindonuts()



def atm():
    balance = 5000
    pin = 6767
    print('Welcome please type in your pin ')
    userpin= int(input())
    if userpin == pin:
        print('get your money and go we got places to be')
        print('1. withdraw money')
        print('2. deposit money')
        print('3. check balance')
        select= int(input('select an option before i get mad: '))
        if select == 1:
            print('how much you takin out b?')
            amount = int(input())
            if amount > balance:
                print('overdraft')
                print('You think you mr money or sum?')
            else:         
                 newbalance = balance - amount
                 print('you are taking out : '+  str(amount))
                 print('you have this amount left: ' +str(newbalance))
        if select == 2:
            print('Finally getting some bread in here but how much? ')
            amount = int(input())
            newbalance = balance + amount
            print('You now have ' + str(newbalance) + 'dollars in your account.')
        if select == 3:
            print('You have ' + str(balance) + ' amount of dollars in your account.')        
    else:
        print('Yo who is you b?')        
atm()