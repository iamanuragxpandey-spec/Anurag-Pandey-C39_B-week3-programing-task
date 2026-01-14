# write a program that keeps asking the user to enter positive integer. the program should add them up ans stop when the user enters 0.
# finally , print the totak sum.
"""
sum=0
while True:
    user_input=int(input("enter  positive integers: "))
    if user_input<=0:
        break
    sum+=user_input
print(sum)"""

# Write a program that takes a positive integer n as input and counts down 
# from n to 1 using a while loop,
#  printing each number. When it reaches 1, print 'Lower threshold reached'

"""
n=int(input("enter a positive number: "))

while True:
    print(n)
    n-=1
    if n==1:
        print("Lower thresshold reached")
        break
    """

    
# rock paper true
"""player1=0
player2=0
rule={'rock':'scissor','scissor':'paper','paper':'rock'}

while True:
 player1_i=input('enter your choice (rock paper scissor):')
 player2_i=input('enter your choice (rock paper scissor):')
 if player1_i==player2_i:
  print('its a tie')
 elif rule[player1_i]==player2_i:
  player1+=1
 else:
  player2+=1

 if player1==5:
  print(player1_i, 'won the game')
  break
 if player2==5:
  print(player2_i, 'won the game')
  break"""
 
# Generate a random number between 1 and 100. Ask the user to guess it repeatedly using a
#  while loop until they guess correctly. Provide hints like 'Too high' or 'Too low
"""
import random as r
random_number=r.randint(1,100)
attempt=0
while True:
    print(random_number)
    num=int(input("enter the number you think between 1 to 100: "))
    if num==random_number:
        print("correct guesses ")
        attempt+=1
        print(f'attempt: {attempt}')
    elif num>random_number:
        print("Wrong guess (hint:number too high)")
        attempt+=1
    else:
        print("wrong guess (hint:number too low)")
        attempt+=1

        """

# take a number and use a while loop to print its multiplication table
"""
num = int(input("Enter the number: "))
mul = 1   # start from 1

while mul <= 10:   
    product = num * mul
    print(f"{num} x {mul} = {product}")
    mul += 1
   
   """
    


# Generate a random number (1-50). Give the user up to 7 attempts to guess it using
# a while loop. Track remaining attempts and stop early if they guess correctly or run out of tries.
""" 
import random as r
number=r.randint(1,100)
attempt=1
while attempt<=7:
    guess=int(input('enter a number: '))
    if guess==number:
        print(f"congrats you guessed it in {attempt} attempt")
        break
    attempt+=1

"""
#9  
"""Write a Python program that simulates a basic elevator system. 
The program should keep track of the elevator's current position and allow a user to
 travel to different floors until they choose to exit.

Requirements:

a) Starting State: The elevator should start on floor 1.

b) Continuous Loop: Use a while loop to repeatedly ask the user for a destination floor.

c) Input Handling: If the user enters 0, the program should print a goodbye message and
 terminate. If the user enters something that 
isn't a number, handle the error gracefully so the program doesn't crash.

d) Logic: If the target floor is higher than 
the current floor, print a 'Going up' message. If the target floor is lower than the current
 floor, print a 'Going down' message. If the user is alre…"""
"""

current_floor=1
print('current_floor:',current_floor)
while True:
    
    floor=int(input('enter your desired floor: '))
    if floor==0:
        print("good bye")
        break
    elif current_floor>floor:
        print("going down")
        current_floor=floor
        print('current_floor:',floor)
    elif current_floor<floor:
        print('going up')
        current_floor=floor
        print('current_floor:',floor)
    elif current_floor==floor:
        print("same floor")
        print('current_floor:',floor)"""

# 10)
"""10. Generate a frequency table for the ratings list which is initialized below.
 Ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
   a. Start by creating an empty dictionary named content ratings b. Loop through the ratings list. 
   For each iteration, complete the following: > If the rating is already in content ratings then increment the
frequency of that rating by 1.
Else, initialize the rating with a value of 1 inside the content_ratings dictionary."""

Ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
content_rating={}








