# While loop definition - a while loop is a type of construct where code instructions so long as a condition is ture (boolean)

# in order to stop a loop or any program from running in ur terminal, ctrcl + c at the same time.

# While Loop Syntax

ageverify = 17
purchaserAge = int(input("Please enter your age: "))

while ageverify >= purchaserAge:
    print("Sorry, you're not old enough.")
else:
    print('Enjoy ur copy of cyberpunk 2077')

savepassword = '123abc'
userPassword = input("please type in your password")
attempts = 0

while savepassword != userPassword:
    print('Incorrect Password, try again.')
    attempts += 1
    print(' Numbers of attempts left:' + str(attempts) + ' / 3')
    userPassword = input('please try again:')
    if attempts == 3:
        print('Too many failed attempts, your account has been locked for 5m.')
        break
else:
    print('Welcome to your account!')   
    

time = 30
while time > 1:
    time -= 1
    print(time)
else:
    print('times up fat boy')

