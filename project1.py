
import random 
import numpy as np


x_lower = int(input("Enter the lower limit:"))
y_upper = int(input("Enter the upper limit:"))

ran_no = random.randrange(x_lower,y_upper)
min_no_steps = np.log2((y_upper-x_lower)+1)
min_no_steps = int(min_no_steps)

no_of_gusses = 0

while True:
    guess =  int(input("Enter your Guess:"))

    if(guess > ran_no):
        print("Try again! You guess is HIGH!")
        no_of_gusses += 1

    if(guess < ran_no):
        print(" Try again! your guess is LOW!")
        no_of_gusses += 1

    if(guess == ran_no):
        print("You guessed it right") 
        no_of_gusses += 1
        break

    if (no_of_gusses > min_no_steps):
        print("Out of Gusses")
        break

if (no_of_gusses <= min_no_steps):
    print("You won")

else: 
    print("You loose")



    
