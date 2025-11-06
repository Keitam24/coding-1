# For loops - A type of construct that runs code instructions a finite amount of times over a group of data.

halloweenbag = 'Snickers', 'Hershey bar', 'Twizzler', 'Candied Apple', 'Kit Kat'
count = len(halloweenbag)

print(count)

# i is a variable and is short for iterator.
#for i in halloweenbag:
    #print(i)
   #print('I got this candy in my bag ' + i)

for x in range(3):
    print('true or false: 3 is greater than 2.')
    answer = input()
    if answer != True:
        
        print('idiot')
        print('attempt: ' + str(x))
        answer = (input)

        
    else: print('good stuff')
    
# use a for loop to ask a user to type in 5 words and print each word out in the terminal.
# Once the user has finished typing  5 words, the for loop should end.

#CLarification: program should ask the user to typei n one word. Then the program should print it out and ask them to type another word.
# Your program should do this 5 times.

for x in range(5):
    mud = input(' Type in 5 words: ')
    count = len(mud)








    