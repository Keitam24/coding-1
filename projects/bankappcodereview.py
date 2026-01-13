# Run the following code in your terminal. 
# Once you've confirmed the code works, make the following code adjustments:
# 1. write code that will put 25% of paycheck into the savingsAccount variable
# 2. write code that will put 25% of paycheck into the retirementAccount variable
# 3. write code that will put the remaining 50% of the paycheck into the checkingAccount variable
# 4. Print what the user will have in each account. 

def payCheckFilter(payRate):
    checkingAccount = 0
    retirementAccount = 0
    savingsAccount = 0
    hours = 8
    daysWorked = 10
    paycheck = payRate * hours * daysWorked
    savingsAccount = paycheck * 0.25
    retirementAccount = paycheck * 0.25
    checkingAccount = paycheck * 0.50
    
    print('My pay check for working '+ str(daysWorked) + ' day(s) will be ' + str(paycheck))
    print('The amount of money I have now put in my savings account is ' + str(savingsAccount))
    print('The amount of money I have now put in my retirement account is ' + str(retirementAccount))
    print(' The amount of money I now have in my checking account is ' + str(checkingAccount))

payCheckFilter(10.00)
