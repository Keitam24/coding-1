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
       print('current score is ' + str(yourscore) + '/5')
       print('Next Question.')
    else:
        print('current score is ' + str(yourscore) + '/5')
        print('Next Question.')
        questions += 1

    print('What was the most annoying part about making this')
    print('A:the function itself, B.Indents. C.Trying to figure out how to make this code actually work. D. Calling the function.')
    correctanswer5 = 'B'
    studentanswer5 = input()
    if correctanswer5 == studentanswer5:
       yourscore+=1
       
       print('current score is' + str(yourscore) + '/5')
       print('Your test is now completed, your score is:' + str(yourscore))

    else:
       print('current score is ' + str(yourscore) + '/5')
       
       print('Your test is now completed, your score is:' + str(yourscore))


    

quiz()         