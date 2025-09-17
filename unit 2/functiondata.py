# how to create a function that passes data
# step 1. create a function definition
def bnbRefund(username, refundAmount):
    print('Sorry, '+ username + 'for your cancellation.')
    print(' We will refund $'+ str(refundAmount) +' to your bank.')

    # Step 2. Call the function/ execute instructions
bnbRefund('Mary' , 1000)


def happybirthday(username, birthdate): 
    print(' Hello, I am ' + username + ' And my birthday is on 9/24.') 
    print(' On the day of ' + str(birthdate) + ' I will turn 17')

happybirthday( 'Keita' , 'September 24th')


def munyun(dollar):
    pennies = dollar * 100
    print('My ' + str(dollar) + 'dollar(s) is equal to ' + str(pennies) + ' pennies.') 
 
munyun(25)


def joelstriangleshapedhead(length, width):
    area = length*width*0.5
    print('the area of joels fat head is ' + str(area))

joelstriangleshapedhead(60, 70)



def temp(Fahrenheit):
    celsius = Fahrenheit - 32 * 0.59
    print('The weather today is' + str(Fahrenheit) + 'in Fahrenehit but it is' + str(celsius)  + ' Degrees in celsius .')
temp(67)