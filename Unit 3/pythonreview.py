
   
    



def numberguessinggame():
        correctnumber = 9
        attempt = 0
        guess = int(input("Please guess a number. :"))
        while int(guess) != correctnumber:
            if guess > correctnumber:
                print('Incorrect. Number too high. Please guess again.')
                guess  = int(input("Please guess a number."))
                attempt += 1
            elif guess < correctnumber:
                print('Incorrect. Number too low. Please guess again.')
                guess = int(input('Please guess a number?'))
                attempt += 1

        print('Correct!')
        print("attempts = " + str(attempt))

        numberguessinggame()            
                