#1. Write a Python script using a for loop and the range() function to iterate through the numbers from 1 up to and including 5.
# Inside the loop, check if each number is even or odd, and then print the result in the format: "Number X is [even/odd]."
# Output
"""
for i in range(1,6):
 if i%2==0:
  print(f"Number {i} is an even ")
 else:
  print(f"Number {i} is a odd ")
"""

# 2. Write a Python script that uses a for loop to calculate the sum of all elements in the given list.
# list = [10,20,30,40] Your script must:
#Initialize a variable to keep track of the running total.
#Iterate through the data list using a for loop.
#Inside the loop, print the value currently being added and the new running total.
#Finally, print the total sum after the loop finishes.
"""
list=[10,20,30,40]
Running_total=0
for i in list:
    Running_total+= i
    print(f"Added {i}. Running total is {Running_total}")

print("-"*30)
print(f"Total sum is : {Running_total}")"""


#3. Write a program that uses a for loop to iterate through 
# the list student_names = ["Ram", "Hari", "Sita"] and prints a personalized message 
# for each student in the format 'Hi [Name], your course approval is ready!'
#     . Include the header ' --- Email Greetings Generated ---' before the loop.
"""
print("--- Email Greetings Generated ---".upper())
student_names=["Ram", "Hari", "Sita"]
for i in student_names:
    print(f" Hi {i}, your course  approval is ready")"""


#4. write a program that iterates through the list of chapter page counts [45, 30, 50, 40]  
# and (starting the count at 1) to print a message for each chapter in the format: 
# 'Chapter [Number]' ' has [Pages] pages.'. Include the header '--- Book Chapter Summary ---'."
"""
print('--- Book Chapter Summary ---'.upper())
page_counts= [45, 30, 50, 40] 
chapter=0
for i in page_counts:
    chapter+= 1
    print(f"Chapter {chapter} has {i} pages")"""

# 5. Write a Python script to calculate the product (multiplication) of all numeric elements 
# in a given list. given list=[4,5,3,2]
"""
list=[4,5,3,2]
product=1
for i in list:
    product*=i
print(product)"""

# 6. multiplication table of a given number. number= 11
"""
number=11
for i in range(1,11):
    
    print(f"{number} * {i} is {number*i}")

# or 
number=11
for i in range(1,11):
    table=number*i
    print(f"{number} * {i} is {table}")"""

# 7. reverse a list given list = [3,2,1,4,5]
"""    
list=[3,2,1,4,5]
list2=[]
for i in list[5::-1]:
    list2.append(i)
print(list2)"""


# 8.  You have two lists of numbers, and you need to find out which numbers appear
# in both lists.

"""
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common=[]

for i in list1:
    if i in list2:
        common.append(i)
print(common)"""

#9. Given list is lst=[1,2,3,4] but print 1 and 4 only 
"""
lst=[1,2,3,4]
choosen=[]
for i in lst[0::3]:
    choosen.append(i)
print(choosen)"""

# Given list is lst=[1,2,3,4] but print 1 2 and 4 only 
"""
lst1=[1,2,3,4]
lst2=[1,2,4]
choosen=[]
for i in lst1:
    if i in lst2:
     choosen.append(i)
print(choosen)
"""
#or 
'''lst=[1,2,3,4]
lst.remove(3)
print(lst)'''


#11. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
"""
list=[1,2,3,4]
for i in list:
   if i==3:
      list.remove(i)
list.insert(1,'a')
print(list)"""


# 12. Given list is [1,2,3,4,5] separate the elements into odd and even categories.
"""      
list=[1,2,3,4,5] 
odd=[]
even=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)"""


# 13. Write a program to determine whether a given number is a prime number.
"""
num=int(input("Enter your number : "))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(f'{num} is prime number')
else:
    print(f'{num} is not prime number')"""

# 7. You are given a list of student records, where each record is a dictionary containing
#  the student's name and their math grade. Write a Python program that:
# Iterates through each student in the list.
# Adds a new key "status" to each student's dictionary with the value:
# "Approved" if their "math_grade" is 70 or above,
# "Rejected" if their "math_grade" is below 70.
"""
students = [
    {'name': 'ram', 'math_grade': 43}
    , {'name': 'hari', 'math_grade': 65}
    , {'name': 'shyam', 'math_grade': 90}
]
for student in range(len(students)):
    if students[student]['math_grade'] >= 70:
        students[student]['status'] = 'approved'
    else:
        students[student]['status'] = 'rejected'
print(students)"""

#14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
"""
list = [1, 2, 3, 4, "a", "b"]
int_list = []
str_list = []
for i in list:
    if isinstance(i, int):
        int_list.append(i)
    elif isinstance(i, str):
        str_list.append(i)
print("Integer list:", int_list)
print("String list:", str_list)"""

#15. Python program that accepts a string and calculate the number of digits and letters

# val=input("Enter anything ")

# list_val=list(val)
# print(list_val)
# print(len(list_val))
"""
a=input("Enter:")
letter=0
number=0
for i in a:
    if i.isdigit():
        number+=1
    else:
        letter+=1

print("There is ",letter,"letter")
print("there is ",number,"number")"""

# 16. Python program to check the validity of username and password input by users

"""

user={
    "ram":"ram123",
    "shyam":"shyam123"}

for attempt in range(1,4):
    username= input("Enter username: ")
    password= input("Enter password: ")

    if username in user and user[username]==password:
        print("login succesfully ")
        break

    else :
        print("Invalid username or passowrd")
        print("Attempt left:", 3-attempt)

if attempt==3:
    print("Account Locked. Too mamy attempt")"""

#17. program to print the given number is odd or even
"""
num=int(input("enter the number:"))
if num%2==0:
    print(f"{num}  is even number")
else:
    print(f"{num} is odd")
"""

#18. factorial of a given number
"""
num=int(input("enter number : "))
n=1
for i in range(1,num+1):
    n=n*i
print(n)"""

#19. 19. Print multiplication table of  1,2,3,4,5,6,7,8  
"""

for i in range(1,9):
    print(f"----Table of {i}----")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")"""

# 20.  Given list is lst=[1,2,3,4] but print 1 and 2 only
"""

lst=[1,2,3,4]

for i in lst:
    if i==1 or i==2:
        print(i)"""

#21. Python program to calculate the sum of all the odd numbers within the given range.

"""
var=int(input("Enter number : "))
sum_odd=0
for i in range(1,var+1):
    if i%2!=0:
        sum_odd+=i

print(sum_odd ,"is sum of odd")"""

#22. Python program to calculate the sum of all the even numbers within the given range
"""
var=int(input("Enter number : "))
sum_even=0
for i in range(1,var+1):
    if i%2==0:
        sum_even+=i

print(sum_even,"is sum of even ")"""

#23  Python program to count the space of a given string
"""str=input("Enter sentences :")
count=0
for i in str:
    if i==" ":
        count+=1

print(count)"""

#24 . given list is [1,2,3,4] but expected output is [1,8,27,64]
"""
lst=[1,2,3,4]

temp=[]

for i in lst:
    
    temp.append(i**3)
print(temp)"""

# 25.  reverse of a string a="programming". 

"""str="programming"
rev_str=""
for i in str[::-1]:
    rev_str=rev_str+i

print(rev_str)"""

#26. Place a break statement in the for loop 
# so that it prints from 0 to
#  7 only (including 7). Given range(50)
"""
for i in range(50):
    print(i)
    if i==7:
        break"""

#27. Write a for loop that iterates through
#  a string and prints every letter.
"""
str=input("enter string : ")

for i in str:
    print(i)"""

#28.  Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
"""
list=["ram","shyam","hari",1,2,3]
for i in list:
    if type(i)==str:
        print(f"hello!, {i}")"""

#29.  Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
"""
list=["ram", "shyam","hari"]
temp=[]
for i in list:
    temp.append("Dr."+i)

print(temp)"""

#30.  Write a for loop which appends the square of each number to the new list.
"""
list=[1,2,3,4]
temp=[]
print(list)
for i in list:
    
    temp.append(i**2)
print(temp)"""

#31.  Write a for loop using an if 
# statement, that appends each number 
# to the new list if it's positive.given
# lst1=[111, 32, -9, -45, -17, 9, 85, -10]

"""list1=[111, 32, -9, -45, -17, 9, 85, -10]
positive=[]
for i in list1:
    if i>0:
        positive.append(i)

print(positive)"""

#32. Write a Python program that prints
#all the numbers from 0 to 6 except 3 
# and 6. given list=[0,1,2,3,4,5,6]
"""
list=[0,1,2,3,4,5,6]

for i in list:
    if i==3 or i==6:
        continue
    print(i)"""

#33. Write a for loop which appends the type of
#  each element in the first list to the second list.
"""
list=[1,2,3,4,"a","b"]
list2=[]
for i in list:
    if type(i)==int:
        
        list2.append("int")
    

    else:
       
        list2.append("Str")

print(list)
print(list2)"""

#34. Use else block to display a message “Done” after successful execution of for loop.

"""
for i in range(6):
    print(i)

else:
    print("done")"""

#35. Write a for loop statement to
#print the following 
#series: 105 98 -------7
"""
for i in range(105,0,-7):
    print(i)"""

#36. removal bad characters from the 
# given string. Given 
# bad_chars = [';', ':', '!', "*"], 
# string = "py;th* o:n ! ;py * t*h:o !n".  
# Expected output = pythonpython

"""str="py;th* o:n ! ;py * t*h:o !n"

bad_chars = [';', ':', '!', "*"," "]
output=""
for i in str:
    if i in bad_chars:
        continue

    output+=i

print(output)"""

#37.  #37. Python program to count the number of even and
#  odd numbers from a series of numbers.  
"""
count_even=0
count_odd=0

for i in range(100):
    if i %2==0:
        count_even+=1

    else:
        count_odd+=1

print("Even number :",count_even)
print("Odd number :",count_odd)"""

#38. Write a for loop to find the sum
#of all multiples of 3 or 5 below a 
#given number range from 3 to 99.
"""
sum=0
for i in range(3,100):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)"""


#39. Write a for loop to find the sum of even and
#odd numbers separately in a range from 1 to 100.
"""

sum_even=0
sum_odd=0
for i in range(1,101):
    if i %2==0:
        sum_even+=i


    else:
        sum_odd+=i

print(sum_odd,"is sum of odd number from 1 to 100")
print(sum_even,"is sum of even number from 1 to 100")"""

#40. program to check given number 
# is palindrome or not
"""
num=int(input("enter number"))
str_num=str(num)
rev_num=""
for i in str_num[::-1]:
    
    rev_num+=i


if (rev_num)==num:
    print(f"{num} is palindrome")

else :
    print(f"{num} is not palindrome")"""

# 41. program to check given number is armstrong or not

num=1634
p=0

str_num=str(num)
for i in str_num:
    p=int(i)**3+p

if num==p:
    print(f"{num} is armstrong")

else:
    print(f"{num} is not armstrong")