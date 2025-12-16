# i no black papi im dominican
def gpacalcformath():
  totalmathgrade = 0
  weeks = 17
  semestergrade = totalmathgrade / weeks      
  gradeletter = ''


  for week in range(1, weeks + 1):
        while True:
            
              grade = float(input("What's your grade for this week?: "))
              if 0 <= grade <= 100:
               totalmathgrade += grade
              break
  

  if semestergrade >= 90:
      gradeletter = 'A'
  elif semestergrade >= 80:
      gradeletter = 'B'
  elif semestergrade >= 70:
      gradeletter = 'C'
  elif semestergrade >= 60:
      gradeletter = 'C'
  else: gradeletter = 'F'  

  print('Your average grade for math is' + float(semestergrade) + 'Which results in you having a ' + gradeletter + ' As your total grade.' )




            
gpacalcformath()

