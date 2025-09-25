# conditional satements - code instructions that have different outcomes based on the inputted data
# input --> condition --> output

# Conditional statement syntax
# if keyword - controls the condition that we want to satisfy.

# else - Our default outcome. the things that happens when our conditions are not satisfied.
def sunnyday():
    weather = input('what is the weather like today? ')
    if weather == 'sunny':
        print(" it is beautiful outside. Bring sunglasses. So you don't have to see Joel.")
    elif weather == 'rainy': 
        print(' Bring an umbrella and hit joel with it')
    elif weather == 'windy':
        print(' Bring a jacket and kick Joel')
    else: 
        print("I can't tell you the weather, but have a good day unless your name is Joel.")

def yourpassword():
    password = input('Please enter your password.')
    if password == 'skibiditoilet':
        print(' Welcome to your account.')

    else:
        print("Your password or email was incorrect, please try again.")

 

vanilla = 0
chocolate = 10
strawberry = 10

def iceCreamshop(vanilla):
    if vanilla > 1:
        print('we have vanilla in stock.')
    elif chocolate > 1:
        print ('we have chocolate in stock.') 
    elif strawberry > 1:
        print('we have strawberry in stock')
    else:
         print('we dont have that ice cream get out')       
  

def football():
    down = input('What down is it')
    yards = input('How many yards do you need to get another first down? ')

    if down == 1 and yards <= 5:
        print('rush')
    elif down == 2 and yards <= 5:
        print('rush')
    elif down == 3 and yards <= 5:
        print('pass')
    else:
        print('punt')   



def permittest(age): 

   
    if age >= 16:
        print(' You are old enough to get your drivers permit, congratulations.')
    else:
        print('Sorry, you are not able to get your drivers permit.')
 
permittest(16)