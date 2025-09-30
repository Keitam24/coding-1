def permittest(age): 

   
    if age >= 16:
        print(' You are old enough to get your drivers permit, congratulations.')
    else:
        print('Sorry, you are not able to get your drivers permit.')
 
permittest(16)



# 2

def problemtwo(integer):
    if integer >= 0:
        print('This is positive.')
    else:
       print('This is negative.')


problemtwo(-3)       



def problemthree(yourgrade):
    if yourgrade >= 90:
        print(' You have an A.')
    elif yourgrade <= 90 and yourgrade >= 80:
        print('You have a B.')
    elif yourgrade <= 80 and yourgrade >= 70:
        print('You have a C.')
    elif yourgrade <= 70 and yourgrade >= 60:
        print('Your grade is a D.') 
    else:
        print ('You have a F')




problemthree(90)