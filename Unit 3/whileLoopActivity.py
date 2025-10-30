def numbers():
  numberlist = []
  yournumber = input('Type in your number: ')
  while yournumber != 'quit':
    transformNumber = int(yournumber)
    numberlist.append(yournumber)
    print(numberlist)
    yournumber = input('Please type in a number: ')


  else:
    print('Loop stopped...')


    



def questiontwo():
  numberlist = []
  yournumber = input('Type in your number: ')
  while yournumber != 'quit':
   labubu = int(yournumber)
   numberlist.append(labubu)
   print(yournumber)
   numberlist = input('Add to the list before i get mad: ')
   





def question3():
  thecorrectnumber = 41
  yournumber = int(input('Guess the correct number'))
  while yournumber != thecorrectnumber:
    if yournumber == thecorrectnumber:
      print('Congratulations, you chose the correct number!')
      break
    elif yournumber > thecorrectnumber:
      print('Your number is higher then the correct number, try again.')
    elif yournumber < thecorrectnumber:
      print('Your number is less than the correct number, try again.')
    yournumber = int(input('Guess the correct number'))

question3()      

      