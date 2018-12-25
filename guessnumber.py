# This is a guess the number game
import random
secretnumber = random.randint(1,20)
print('I think a number between 1 to 20')
 
# Ask the player to guess 6 times
for guessTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess >secretnumber:
       print("your number is too large")
    elif guess < secretnumber:
       print("you  number is too small")
    else:
       break # This conditon  is  the correct guess
if guess == secretnumber:
   print("Good job,you guessed my number in "+str(guessTaken)+' guesses!')
else:
   print("Nope.The number I was thinking of was"+str(secretnumber))       