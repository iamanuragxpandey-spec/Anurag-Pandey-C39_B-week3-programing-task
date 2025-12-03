print("Welcome to the magic forest ".upper())
direction = input("choose the direction: ")
if direction=="south":
    print("Game over")
else:
    choice=input("you want to : ( Cross the river or Follow the river ): ")
    if choice== "Cross the river":
        print("Game over")
    else:
        choice=input(" you want to choose :(Fairy , Orge , elf ): ")
        if choice=="Fairy" or choice=="orge":
            print("Game over")
        else:
            print("you win")





"""

print("Welcome to the Space Mission")
planet=input("You want to go to Moon or to Mars" )
if planet=="Mars":
    print("Game over")
elif planet=="Moon":
    choice=input("")


else:
    print("invalid option")







""" # not completed

"""
Number=int(input("Enter a Number: "))
if Number >0:
    if Number %2==0:
        print("even")
    else:
        print("odd")
elif Number <0:
    print("negative")
else:
    print("given number is zero")
    """
"""

salary=int(input(" Current salary:"))
years_of_service=int(input("enter thr year of service:"))
if years_of_service>10:
    bonus_amount=salary*10/100
    salary=salary+bonus_amount
elif years_of_service>6 and years_of_service <=10 :
    bonus_amount=salary*8/100
    salary=salary+bonus_amount
else:
    bonus_amount= salary*5/100
    salary=salary+bonus_amount 
   
print(f"Bonus =:{bonus_amount}")
print(f"Actual salary:{salary}")
"""
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
"""
is_valid=True
initial_balance=5000
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
            elif amount>5000:
                print("insufficent balance")
            else:
                balance=initial_balance-amount
                print(f"your actual balance is : {balance}")
        elif choice==2:
            print(f"your actual balance is: {initial_balance}")

    else:
        print("please enter a correct pin")


else:
    print("invalid card")   """