# Operator- Operators are a construct (built-in system) thag give data types more actions and power.
# Arithmetic Operator Family - Arithmetic operators are simply math operations.
# Print () is a function where anything inside the round brackets will be printed out in the terminal.
print(2+4) # addition operator
print(10-10) # subtraction operator
print(2/1) # division operator
print(6*7) # multiplication operator

# Assignment operator family - these operators assign values to variables (otherwise known as containers)
# Key/ value pairs
schoolName= "Boys Latin"
age = 16
username = "theegoist"
password = "twentysevenk"
location = "blablabla"
age += 2 # adding a new value to our variable
age *= 3 # multiplying a new value to our variable
print(age)
# Comparison Operator Family - comparsion family of operators simply compares values.
print (2 > 1)
print (100 > 29) 
print ("123abc" == "123Avbc") # double equal signs mean its comparing if the values are "The Same"
print (2 != 3) # Not he same
# Logical Operator Family - It checks and compares if certain code conditions are true or false

print(3 > 1 and "theegoist" == "theegoist")
# the AND operator checks to see BOTH conditions are ture. If both are true the answer is true.

print (2 == 1 or 3 > 2)  # This will return true
# The OR operator checks if ONE of the conditions is TRUE. So long as ONE of the conditions is True, it will be true.

print(not(3>1 and "theegoist" == "theegoist")) # false
# The NOT operator will give the opposite result. The NOT operator flips the result.

input= "twentysevenk"
print(password == input) 
