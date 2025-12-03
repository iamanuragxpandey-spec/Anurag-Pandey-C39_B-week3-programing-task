# 1. Take a number and print “Even” or “Odd”.  
"""
number=int(input("Enter a number:"))
if number==0:
    print(f"{number} is zero")
elif number%2==0:
    print(f"{number} is even")
else:
    print(f"{number}is odd")
    """

#2. Take a character and print “Vowel” or “Consonant”. 
"""
char=input("enter a character:")

if char in "aieou":
    print("its vowel")
else:
    print("its consonant")  """

#3. Take age and print “Minor” if <18, else “Adult”.  
"""
age=int(input("Enter your age:"))
if age<18:
    print("Minor")
else:
    print("Adult")
        """

# 4)Take marks (0–100) and print “Pass” if ≥40, else “Fail”. 

"""
marks=int(input("Enter the mark:"))
if marks>0 and marks<100:
    if marks>=40:
        print("pass")
    else:
        print("fail")
else:
    print("invalid marks please put a valid mark")
    """

#5. Take 3 numbers and print the largest using only if-else 
 
"""num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
if num1>num2 and num1>num3:
    print(f"{num1} is the greatest")
elif num2>num1 and num2>num3:
    print(f"{num2} is the greatest")
else:
    print(f"{num3}is the greatest")"""

#6. Take a month number (1–12) and print the month name.
""" 

month=int(input("Enter the month number:"))
if month>=1 and  month<=12:
 if month==1:
  print("january")
 elif month==2:
   print("febuary")
 elif month==3:
   print("march")
 elif month==4:
   print("april")
 elif month==5:
   print("may")
 elif month==6:
   print("june")
 elif month==7:
   print("july")
 elif month==8:
   print("augest")
 elif month==9:
   print("september")
 elif month==10:
   print("octuber")
 elif month==11:
   print("november")
 elif month==12:
   print("december")
else:
  print("please provide a valid month number")"""  

# 7. Take temperature in Celsius → print “Hot” (>35), “Warm” (25–35), “Cold” (<25). 
 
"""
temp=int(input("Enter  temperature in Celsius(C:)"))
if temp>35:
    print("Hot")
elif temp<25:
    print("Cold")
else:
    print("Warm")"""

#8. Take salary → if >50000 print “High”, elif >30000 print “Medium”,else “Low”. 

"""
salary=int(input("enter the salary:"))
if salary>50000:
    print("high")
elif salary<=50000 and salary>30000:
    print("Medium")
else:
    print("Low")"""

#9. Take a number → print “Positive”, “Negative”, or “Zero”. 

"""num=int(input("enter a number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")"""

# 10. Take day number (1–7) → print “Weekday” or “Weekend”. 
"""day=int(input("Enter the day number of week:"))
if day>=1 and day<=7:
    if day==7:
        print("weekend")
    else:
        print("weekday")
else:
    print("please enter a valid week day")"""
# 11. Take a number → check if it is divisible by both 5 and 7.
"""
num=int(input("Enter a number:"))
if num%5==0 and num%7==0:
    print(f"{num} is divisible by 5 and 7")
else:
    print(f"{num} is  not divisible by 5 and 7")"""

# Write a program to check weather the number is between 1 and 100
"""
num=int(input("Enter a number:"))
if num>1 and  num<100:
    print("number lies between 1 and 100")
else:
    print("number  does not lies between 1 and 100")"""

# Write a program that takes a student's marks and prints their grade.
# Print the grade according to this table:MarksGrade
# 90-100  A+        # 80-89  A              # 70-79 B+   
#  # 60-69 B      # 50-59 C      # 40-49 D           # Below 40 E

"""
marks=int(input("Enter the student's mark: "))
if marks>0 and marks<=100:
    if marks>=90 and marks<=100:
        print("A+")
    elif marks>=80 and marks<=89:
        print("A")
    elif marks>=70 and marks<=79:
        print("B+")
    elif marks>=60 and marks<=69:
        print("B")
    elif marks>=50 and marks<=59:
        print("C")
    elif marks>=40 and marks<=49:
        print("D")
    else:
         print("E")
else:
    print("Enter a valid marks")"""
#QNO.5
#Create a simple calculator that performs one of four operations: +, -, *, /
# # based on user choice. First number (num1) .Second number (num2)
# Operator as a single character:, , , or/ (entered on separate lines
# Print the result of the operation If the operator is invalid print "Invalid operator

"""
num1=float(input("Enter the first number(num1):"))
num2=float(input("Enter the second number(num2):"))
operator=input("operator as a single character(+,-,*,/)")
if operator=="+":
    result= num1 + num2
    print(result)
elif operator=="-":
    result= num1 - num2
    print(result)
elif operator=="*":
    result= num1 * num2
    print(result)
elif operator=="/":
    if num2!=0:
     result= num1 / num2
     print(result)
    else:
       print("Error:Division by zero")
else:
   print("invalid operator")
"""

# QNO-6)
# Write a program to check whether a person is eligible for voting or not 
# (accept age from user)
"""
age=int(input("Enter your age:"))
if age>=18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")"""


# Qno-7)
# Ask a user for a username and password. If username is correct, check if
# the password is correct,and display apporiate login messages.
 
"""
correct_username = "admin"
correct_password = "12345"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == correct_username:
    if password == correct_password:
        print("Login successful! Welcome,",)
    else:
        print("Incorrect password. Please try again.")
else:
    print("Username not found. Access denied.")"""

# Qno-8
# Write a program to check whether a number entered by user is divisible by 7 or not
"""
num=int(input("Enter the number:"))
if num%7==0:
    print("Number is divisible by 7 ")
else:
    print("number is not divisible by 7")"""


# Qno-1)
#  Write a program that takes three numbers as input and determines: 
# If all three are equal then print "All numbers are equal" 
# If exactly two are equal then print "Two numbers are equal" 
# If all are different then print "All numbers are different"

"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b == c:
    print("All numbers are equal")
elif a == b or b == c or a == c:
    print("Two numbers are equal")
else:
    print("All numbers are different")"""
#2. Write a complete Python program that: 
# Asks Player 1 to enter their move ( input: rock, paper, or scissors)  Asks Player 2 to enter their move ( input: rock, paper, or scissors) 
# Uses only nested if and else statements  
# Prints who wins or if it's a tie 
"""
p1 = input("Player 1, enter your move (rock, paper, or scissors): ")
p2 = input("Player 2, enter your move (rock, paper, or scissors): ")

if p1 == "rock" or p1 == "paper" or p1 == "scissors":
    if p2 == "rock" or p2 == "paper" or p2 == "scissors":
        if p1 == "rock":
            if p2 == "rock":
                print("It's a tie")
            else:
                if p2 == "paper":
                    print("Player 2 wins")
                else:
                    print("Player 1 wins")
        else:
            if p1 == "paper":
                if p2 == "rock":
                    print("Player 1 wins")
                else:
                    if p2 == "paper":
                        print("It's a tie")
                    else:
                        print("Player 2 wins")
            else:
                if p1 == "scissors":
                    if p2 == "rock":
                        print("Player 2 wins")
                    else:
                        if p2 == "paper":
                            print("Player 1 wins")
                        else:
                            print("It's a tie")
    else:
        print("Invalid move by Player 2")
else:
    print("Invalid move by Player 1")"""

#4. In a smart building lift system, the lift is currently at floor 5. A person presses 
#floor 3. Write a program to decide and display whether the lift should go up, go 
# down, or stay at current floor. 
"""
floor=5
button_pressed=3
if floor>button_pressed:
    print(f"lift Go down to and stop at floor {button_pressed}")
elif floor<button_pressed:
    print(f"lift Go up  and stop at floor {button_pressed}")
else:
    print(f" Lift will stay at curent floor")"""

# 6. Take two numbers and find the greater of the two. If they are equal, check if the 
# number is positive, negative, or zero. 
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("The greater number is:", a)
else:
    if b > a:
        print("The greater number is:", b)
    else:
        if a > 0:
            print("Both numbers are equal and positive")
        else:
            if a < 0:
                print("Both numbers are equal and negative")
            else:
                print("Both numbers are equal and zero")"""

# 7. Accept input from user If given number is a multiple of both 3 and 5 prints "Fizz 
# Buzz" instead of number If given number is a multiple of 3 but not 5 prints "Fizz" 
# instead of number If given number is a multiple of 5 but not 3 prints "Buzz" instead 
# of number If given number is not multiple of 3 or 5 prints value as usual. 

"""
num=int(input("Enter the number:"))

if  num%3==0:
    if num%5==0:
        print("Fizz Buzz")
    else:
        print("Fizz")
else:
    if num%5==0:
        print("Buzz")
    else:
        print(num)"""

# 8. Snapple is a famous tea drink brand from Queens, New York. Each bottle cap 
# comes with a silly fun fact. 
# Use the random module to create a number from 0 to 5. Then use 
# an if/elif/else statement to print out one of these six random Snapple facts: 
# 0 - 'Flamingos turn pink from eating shrimp.' 
# 1 - 'The only food that doesn't spoil is honey.' 
# 2 - 'Shrimp can only swim backwards.' 
# 3 - 'A taste bud's life span is about 10 days.' 
# 4 - 'It is impossible to sneeze while sleeping.' 
# 5 - 'It is illegal to sing off-key in North Carolina.' 

"""
import random as r
facts = [
    "Flamingos turn pink from eating shrimp.",
    "The only food that doesn't spoil is honey.",
    "Shrimp can only swim backwards.",
    "A taste bud's life span is about 10 days.",
    "It is impossible to sneeze while sleeping.",
    "It is illegal to sing off-key in North Carolina."
]

a=r.randint(0,5)

if a==0:
    print(facts[0])
elif a==1:
    print(facts[1])
elif a==2:
    print(facts[2])
elif a==3:
    print(facts[3])
elif a==4:
    print(facts[4])
elif a==5:
    print(facts[5])"""

# 9. A store gives a 20% discount if the total purchase is above RS 1000 AND the 
# customer is a member, or a 10% discount if the purchase is above RS 1000 but the 
# customer is not a member. Write a program that takes total_amount and 
# is_member (True/False) as input and prints the final amount after applying the 
# correct discount (or no discount).
"""
total_amount = float(input("Enter total purchase amount: "))
is_member_input = input("Are you a member? (True/False): ")

if is_member_input == "True":
    if total_amount > 1000:
        final_amount = total_amount * 0.8
    else:
        final_amount = total_amount
    print("Final amount to be paid:", final_amount)
elif is_member_input == "False":
    if total_amount > 1000:
        final_amount = total_amount * 0.9
    else:
        final_amount = total_amount
    print("Final amount to be paid:", final_amount)
else:
    print("Invalid input for membership. Please enter True or False.")"""

# 10.) Create a weight conversion program that: 
# Asks the user what their Earth weight is (as a float). 
# Asks the user for a planet number (as an int). 
# Then, use an if/elif/else statement to calculate the user's weight on the 
# destination planet. 
#  To calculate the user's weight: destination weight=Earth weight × relative gravity 
#   Number Planet Relative Gravity 
#        1 Mercury 0.38              2 Venus 0.91 
# 3 Mars 0.38    4 Jupiter 2.53    5 Saturn 1.07    6 Uranus 0.89     7 Neptune 1.14 
#If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid 
#planet number'.
"""
wet = float(input("Enter the weight: "))
print("""
'''1 = Mercury
2 = Venus
3 = Mars
4 = Jupiter
5 = Saturn
6 = Uranus
7 = Neptune'''
""")

pla = int(input("Choose planet (1-7): "))

list_pla = {
    1: "Mercury",
    2: "Venus",
    3: "Mars",
    4: "Jupiter",
    5: "Saturn",
    6: "Uranus",
    7: "Neptune"
}

list_rg = {
    1: 0.38,
    2: 0.91,
    3: 0.38,
    4: 2.53,
    5: 1.07,
    6: 0.89,
    7: 1.14
}

if pla in list_pla:
    print(f"You chose: {list_pla[pla]}")
    user_wt = wet * list_rg[pla]
    print(f"{user_wt} kg on {list_pla[pla]}")
else:
    print("Invalid choice")"""



# 14.) Ask the user for a subject score. If it's above 90, congratulate him.
# If it's between 
# 50 and 90, suggest improvement. Otherwise, advise on retaking the course. 
"""
score = float(input("Enter the subject score: "))

if score > 90:
    print("Congratulations! Excellent performance.")
elif 50 <= score <= 90:
    print("Good effort. Keep improving to reach excellence.")
else:
    print("Consider retaking the course .")"""
#Qno16)
"""
gender=input("enter your gender (M or F):")
age=int(input("enter your age"))
working_days=int(input("enter the number of days"))
if age>=18 and age<30:
    if gender=="M":
        wages_per_days=working_days*700
    else:
        wages_per_days=working_days*750
elif age>=30 and age<=40:
    if gender=="M":
        wages_per_days=working_days*800
    else:
        wages_per_days=working_days*850
else:
    print("invalid age")

print(f"wages=:{wages_per_days}")
"""

# 17). Write a Python program to simulate a simple ATM with the following 
# specifications:  #  Assume the card is valid (is_valid = True) 
#  Initial account balance is 50000 
# Correct PIN is 123 
# After entering correct PIN, display the menu: 
# 1. Withdraw 
# 2. Check Balance  # 3. Exit 
# If user selects 1 then ask amount and deduct from balance 
# If user selects 2 then show current balance 
# If user selects 3 then print “Thank you for visiting” 
# Show proper messages for wrong PIN and invalid option Use nested if-else 
# statements only.


"""
is_valid=True
initial_balance=50000
pin=123
if is_valid:
    print("ok")
    pin=int(input("Enter a pin:"))
    if pin ==123:
        print("1 to withdraw")
        print("2 to check balance")
        choice=int(input("enter a choice (1 or 2):"))
        if choice==1:
            amount=int(input("enter a amount:"))
            if amount<500:
                print("you have to enter the amount greater then 500")
            elif amount>50000:
                print("insufficent balance")
            else:
                balance=initial_balance-amount
                print(f"your actual balance is : {balance}")
        elif choice==2:
            print(f"your actual balance is: {initial_balance}")

    else:
        print("please enter a correct pin")


else:
    print("invalid card")   
"""

# 18. Create a Python program that greets the user with the message "Welcome to the 
'''Magic Forest". Then, ask the user whether they want to go "north" or "south". If 
they choose "south", print "Game Over". If they choose "north", ask if they want to 
"cross the river" or "follow the path". If they choose "cross the river", print "Game 
Over". If they choose "follow the path", ask them to choose between "fairy", "ogre", 
or "elf". If they choose "ogre" or "fairy", print "Game Over". If they choose "elf", 
print "You Win". '''
"""
print("Welcome to the Magic Forest".upper())

direction = input("Do you want to go 'north' or 'south'?: ")

if direction == "south":
    print("Game Over")
elif direction == "north":
    choice = input("Do you want to 'cross the river' or 'follow the path'? ").lower()
    if choice == "cross the river":
        print("Game Over")
    elif choice == "follow the path":
        creature = input("Choose between 'fairy', 'ogre', or 'elf': ").lower()
        if creature == "elf":
            print("You Win")
        elif creature in ["fairy", "ogre"]:
            print("Game Over")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")"""



#19) Create a Python program that greets the user with the message "Welcome to the 
"""Haunted House". Then, ask the user whether they want to go "upstairs" or 
"downstairs". If they choose "downstairs", print "Game Over". If they choose 
"upstairs", ask if they want to "enter the room" or "stay outside". If they choose 
"enter the room", print "Game Over". If they choose "stay outside", ask them to 
choose between "ghost", "vampire", or "werewolf". If they choose "ghost" or 
"vampire", print "Game Over". If they choose "werewolf", print "You Win"""

print("Welcome to the Haunted House".upper())
direction=input("Do you want to go 'upstair'or 'downstair':")
if direction=="downstair":
    print("Game over")
elif direction=="upstair":
    choice=input("Do yo want to'enter the room 'or'stay outside':")
    if choice=="enter the room":
        print("Game over")
    elif choice=="stay outside":
        choice=input("choose between'ghost','vampire'or'werewolf':")
        if choice=="ghost":
            print("Game over")
        elif choice=="vampire":
            print("Game over")
        elif choice=="werewolf":
            print("You win")
        else:
            print("invalid choice")
    else:
        print("invalid choice")
else:
 print("invalid choice")  


         
    

