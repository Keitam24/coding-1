# conditional satements - code instructions that have different outcomes based on the inputted data
# input --> condition --> output

# Conditional statement syntax
# if keyword - controls the condition that we want to satisfy.

# else - Our default outcome. the things that happens when our conditions are not satisfied.

weather = input('what is the weather like today? ')
if weather == 'sunny':
    print(" it is beautiful outside. Bring sunglasses. So you don't have to see Joel.")
elif weather == 'rainy': 
    print(' Bring an umbrella and hit joel with it')
elif weather == 'windy':
    print(' Bring a jacket and kick Joel')
else: 
    print("I can't tell you the weather, but have a good day unless your name is Joel.")


password = input('Please enter your password.')
if password == 'skibiditoilet':
    print(' Welcome to your account.')

else:
    print("Your password or email was incorrect, please try again.")