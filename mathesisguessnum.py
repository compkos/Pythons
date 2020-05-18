 # This is a guess the number game.
import random

def isnum(n = ''):
    if not type(n) is str : 
        return False
    n = n.strip()
    if n.isdigit(): 
        return True
    elif n[0] in '+-' and isnum(n[1:]):
        return True
    elif "." in n:
        if n.count(".")<= 1 and isnum(n.replace(".", "")):
            return True
        else:
            return False
    else :
        return False

guessesTaken = 0
print('Hello! What is your name?')
myName = input()
score=0
guess=-1
newgame=1
number=0
finalscore=0
print('Well, ' + myName + ', I am thinking of a number between 1 and 100')
while guess !=0 :
  print('Take a guess between 1 and 100 or 0 to stop.') 
  guess = input()
  if not isnum(guess):
     continue  
  guess = int(guess)
  if guess<0 or guess>100 :
     continue
  if newgame==1 :
    number = random.randint(1, 100)
    newgame=0
  if guess==0 :
     print ( "Your score is " + str(score) + " and the number I thought was " + str(number))
     break
  guessesTaken = guessesTaken + 1
  if guess < number:
     print('Your guess is too low.') 
  if guess > number:
     print('Your guess is too high.')
  if guess == number:
     score=10-guessesTaken
     if score<0 :
       score=0
     print('Good job, ' + myName + '! You guessed my number in ' + str(guessesTaken) + ' guesses and your score is ' + str(score))
     print("Do you wish start over ? (y/n)")
     answ=input()
     if answ =="n" or answ=="N":
      finalscore=finalscore+score 
      break
     else :
       finalscore=finalscore+score
       newgame=1
       score=0
       guess=-1
       guessesTaken=0
print ("Thanks " + myName)
print ("Your final score is "+ str(finalscore))

