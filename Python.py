"""
import keyword
print(keyword.kwlist)

import keyword
print(len(keyword.kwlist))
"""
'''
age = 35
print(type(str(age))) '''

# name = "keshab"
#print(len(name))

"""
name = "keshab"
if len(name) >=8:
    print("valid")
else:
    print("invalid")

"""



'''
name='ramrraa'
result=name.count("r") 0 if R is in ("R")
print(result)
'''

'''
name='ram'
result=name.replace('r','R') # output = Ram
print(result)
"""
name='ram'
result=name.replace('r','RR')  output= RRam
print(result)
"""
name='ram'
result=name.replace('r','R').replace('m','R') #output = RaR
print(result)

a='rarm'
result=a[:2]+'R'+a[3] # output= raRm
print(result)

'''

# maketrans =for it to reassign value it should have pair of key and value
'''
name='rarm'
result=name.maketrans('rm','R') # wont work
print(result)
 '''
#name='rarm'
#result=name.maketrans('r','R')
#print(result)

# asciivalue

'''name='rarm'
result=name.maketrans('rM','RR')
print(name.translate(result))
print(ord('r')) # A = 65  Z = 90
print(ord('a')) # a=97 z=122
print(ord('m'))'''
 # strip ,lstrip, rstrip , split
'''
username = '   ram   123  '
print(username.rstrip())
username = '   ram   123  '
print(username.lstrip())
username = '   ram   123  '
print(username.strip()) '''

'''
username = '   ram   123  '
step1=username.split()
print(''.join(step1)) '''

"""
name= "i love python"
print(name.capitalize()) # capalitze first letter 

name= "i love python"
print(name.isupper()) # check whether aall letter are upper or not


"""
"""
import string
string=string.punctuation
print(string)

"""
"""
password= 'abc@123'
print(password.isupper())
flag=False
for i in password:
    if i.islower():
        flag=True
    break
print(flag)

"""
'''
num1=input("enter a first no:")
num2=input("enter a second no:")
print(num1+num2)
''' # this gives asnwer in string 
"""
num1=eval(input("enter a first no:"))
num2=eval(input("enter a second no:"))
print(num1+num2) 
"""
# integer = 10 12 14 123
# float = 12.13
# boolean True FAlse
# a=3+1
# print(a.real,a.imag)
#list []
"""
tuple= 1,2,3,4
print(type(tuple))
"""
# {1,2,3,4} set
# in dictionary {key:value}
#eg
"""
students_grade={"ram":"A+","shayam":"A+"}
a={}
print(type(a))
# empty set set()
a=set()
print(type(a))
a={*()}
print(type(a))
"""

"""
slogon=input("enter your slogan:").title()
print("*"*30)
step1= slogon.center(30)
print(step1)


print("*"*30)
"""
"""
password=input("enter your password:")
print("*"*30)
step1=len(password)-2
step2=password[0]+'*'*step1+password[-1]
print(step2)
print("*"*30)
"""
"""
phone_number=input('enter your phone no:')
print("*"*30)
step1=phone_number[:4]

step2=phone_number[-4:]

step3=6*"*"
print(''.join((step1,step3,step2)))
"""


username = '     ram   123  '
print(username.strip())
