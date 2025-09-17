# Function- is a set of conde instructions labelled under a custom name that the computer will run.

# Function Syntax (rules of how it is written)
# Functions have 2 phases: function definition and function call.

# Function definition - we are describing the instruction for our custom code. 
# We are adding logic to the computers vocabulary.
# This code does not run- it only gives the computer the meaning, not the action.
def example():
        print('Joel Is Hideous.') # 1 instruction: print Joel Is Hideous.

 # phase 2: function call
  #  Once we have the definition, we can now run the instructions by writing the function name.

example()

# we indent to inform the computer that we are about to write code instructions. If we don't, we will get an error.
def example2():
   print(' good day')
   a = input('enter a number: ')
   print(a) 
example2()

def math():
      a = input("please enter a number: ")
      b = 30
      print("Here is your result! ")
      print(int(a)+ b)
      #math()  




# Create a function that will calculate 2 numbers with different arithmetic operators
def calculate():
   numx = input('please enter a number: ') 
   numy = input('please enter another number: ')
   print(numx, numy)

calculate()