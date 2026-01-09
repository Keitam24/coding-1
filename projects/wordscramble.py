# labubub albublabu labuublabu create a function thaat contains alist with 4 words
# labubub randomly select a word from the list
# 3. shuffle the select word and show it ot the user
# 4. allow user to input a guess, if it is correct, they win
# or else they lose
import random 

def ofakillayougetit():
    wordpool = ["Insidious", "Fragmentalism", "Malpractice", "Inconsequential"]
    correctword = ''
    attempts = 1
    randomselect = random.randint(0,3)
    print(randomselect)

    if randomselect == 0:
        correctword = wordpool[0]
        print(correctword)
    elif randomselect == 1:
         correctword = wordpool[1]
         print(correctword)
    elif  randomselect == 2:
        correctword = wordpool[2]
        print(correctword)
    elif randomselect == 3:
        correctword = wordpool[3]
        print(correctword)            

    convertedstring = list(correctword)
    print(convertedstring)
    random.shuffle (convertedstring)
    print(convertedstring)
    scrambled = ''.join(convertedstring)
    print(scrambled)
    print('Please guess the correct word: ' + scrambled)
    userguess = input()

    if userguess == correctword:
        print('You Win')
    while userguess != correctword:
        attempts += 1
        print('Wrong, Your number of attempts left are: ' + str(attempts) + ' / 3')
        userguess =  input('Try not to get it wrong this time.: ')
        if attempts == 3:
            print('labubuuuuuuu')
            break
   
         


ofakillayougetit()    