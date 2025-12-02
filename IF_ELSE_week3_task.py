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
