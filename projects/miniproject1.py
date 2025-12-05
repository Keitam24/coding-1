def quiz():
    print('It is time for you to take your coding quiz, are you ready?')
    print('Which one of the following are not datatypes? A: str B: bool: C: Float D: if')
    questions = 0
    correctanswer1 = 'D'
    studentanswer1 = input()
    yourscore = 0
    if correctanswer1 == studentanswer1:
        yourscore += 1
        print('Next Question')
        print('current score is ' + str(yourscore) + '/5')
    else:
        print('Next Question.')
        print('current score is ' + str(yourscore) + '/5')

    questions += 1
    print('Which of these symbols belong to the comparison operator family?')
    print(' A: - B: > C: * D: +')
    correctanswer2 = 'B'
    studentanswer2 = input()
    if correctanswer2 == studentanswer2:
       print('Next Question.')
       print('current score is ' + str(yourscore) + '/5')
       yourscore += 1
    
       questions += 1
    
    else: 
     print('current score is ' + str(yourscore) + '/5')
     print('Next Question.')
    
    
    questions += 1   
    print('What datatype turns numbers into a decimal?')
    print(' A. bool. B. Int. C. Float. D.List')
    correctanswer3 = 'C'
    studentanswer3 = input()
    if correctanswer3 == studentanswer3:
        yourscore += 1
        questions += 1
        print('current score is ' + str(yourscore) + '/5')
        print('Next Question.')
    else:  
       print('current score is ' + str(yourscore) + '/5')
       print('Next Question.')
       questions += 1

    print('What datatype do you use to let the user put in their answer?')
    print('A. input. B.int. C. intinput. D.str')
    correctanswer4 = 'A'
    studentanswer4 = input()
    
    if correctanswer4 == studentanswer4:
       yourscore += 1
       questions += 1
       print('current score is ' + str(yourscore) + '/10')
       print('Next Question.')
    else:
        print('current score is ' + str(yourscore) + '/10')
        print('Next Question.')
        questions += 1

    print('What was the most annoying part about making this')
    print('A:the function itself, B.Indents. C.Trying to figure out how to make this code actually work. D. Calling the function.')
    correctanswer5 = 'B'
    studentanswer5 = input()
    if correctanswer5 == studentanswer5:
       yourscore+=1
       
       print('current score is' + str(yourscore) + '/10')
       print('Your test is now completed, your score is:' + str(yourscore))
       print(' i lied you have to keep going')
    elif yourscore == 0:
       print('my god you suck dude')


    else:
       print('current score is ' + str(yourscore) + '/10')
       
       print('Your test is now completed, your score is:' + str(yourscore))
       print(' i lied you have to keep going')
      
       print('. what is a function parameter? ')
    print("A. a variable that uses data")
    print('B. a peice of code that does operations')
    print('C. a peice of data that is a placeholder for data')
    print('D. real data that is worked on in a function')
    correctanswer = 'C'
    studentanswer = input()
    if correctanswer == studentanswer:
       yourscore+=1
       
       print('current score is' + str(yourscore) + '/10')
       print('Next Question.')
    else:
      print('current score is' + str(yourscore) + '/10')
      
      print('. What is a for loop? ')
    print("A. a type of function that repeats code forever")
    print('B. a type of function that checks conditions')
    print('C. a type of function that repeats 3 times')
    print('D. a type of function that repeats a finite amount of times')
    correctanswer = 'D'
    studentanswer = input()
    if correctanswer == studentanswer:
       yourscore+=1
       
       print('current score is' + str(yourscore) + '/10')
       print('Next Question.')
    else:
      print('current score is' + str(yourscore) + '/10')

      print('what is a function invocation? ')
    print("A. it is when we write the function instructions")
    print('B. it is when we use conditionals in a function')
    print('C. it is when we invoke and call a function')
    print('D. it is none of the above')
    correctanswer = 'A'
    studentanswer = input()
    if correctanswer == studentanswer:
       yourscore+=1
       
       print('current score is' + str(yourscore) + '/10')
       print('Next Question.')
    else:
      print('current score is' + str(yourscore) + '/10')
      print('Next Question.')
      

      print('4. True or false, a 0 and 1 can be considered booleans? ')
    print("A. True") 
    print('B. False') 
    correctanswer = 'A'
    studentanswer = input()
    if correctanswer == studentanswer:
       yourscore+=1
       
       print('current score is' + str(yourscore) + '/10')
       print('Next Question.')
    else:
      print('current score is' + str(yourscore) + '/10')
      print('Next Question.')

quiz()         