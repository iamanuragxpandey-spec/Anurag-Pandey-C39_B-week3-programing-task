'''item=[1,2,3,4]
i=0
while i in range(len(item)):
    print(item[i])
    i=i+1'''
 ## diff way do same thing
"""
item=[1,2,3,4]
i=0
while i<len(item):
    print(item[i])
    i=i+1"""
"""
count=1
sum=0
while count<=50:
    sum+=count
    count+=1
    
    
print(sum)"""
"""
password=input("enter a password:")
while  len(password)<8 and "@"  in password:
    print("Invalid password")
    password=input('enter a password:')
print('access granted')"""
'''

password=input("enter a password:")
while True:
  if len(password)<8 or "@" not in password:
    print("Invalid password")
    password=input('enter a password:')
  else: 
    print('access granted')'''


# nested while loop
"""
student_name=['ram','hari']
while True:
    print('1.Add')
    print('2.Read')
    print('3.Update')
    print('4.Delete')
    print('5.Exit')
    choice=int(input('enter a choice between 1 to 5: '))
    if choice==1:
        name=input("Enter student name : ")
        student_name.append(name)
        print("New student added successfully")
    elif choice==2:
        index_number=0
        while index_number>=0 and index_number<len(student_name):
            print(f'{index_number}={student_name[index_number]}')
            index_number+=1
    elif choice==3:
        index_number=int(input("enter the index number for updating: "))
        if index_number>=0 and index_number<len(student_name):
            name=input('enter a name: ')
            student_name[index_number]=name
            print('updated successfully')
        else:
            print("please enter a valid number")
    elif choice==4:
        index_number=int(input("enter the index number for deleting: "))
        if index_number>=0 and index_number<len(student_name):
            student_name.pop(index_number)
            print('Deleted successfully')
        else:
            print("please enter a valid number")
    elif choice==5:
        break
"""
"""
items=[3,4,5]

for i in items:
    print(f"----Table of {i}----")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")"""
"""
items=[3,4,5]
i=0
while i<len(items):
    print(f"----Table of {items[i]}----")
    j=1
    while j<=10:
      print(f"{items[i]} x {j} = {items[i]*j}")
      j=j+1
    i=i+1"""
"""
i=2
while i<5:
    i=i+1
    print(i)
    i=i+1
    print(i)"""
"""
sum=0
i=2
while i<5:
  i=i+1
  sum=sum-2
  print(i)
print(sum)"""

"""
a=[3,5,7,9]
sum=0
i=2
while i<len(a)-1:
    i=i+1
    sum=sum+a[3]
print(sum)
"""

"""
a=[3,5,7,9]
sum=0
i=2
while i<len(a):
    i=i+1
    sum=sum+a[i]
print(sum)"""


"""a=[3,5,7,9]
sum=0
i=0
while i<len(a):
    i=i+1
    sum=sum+a[i]
    if i==2:
        break
print(sum)"""

"""a=[3,5,7,9]
sum=0
i=0
while i<len(a):
    if i==2:
        sum=sum+a[i]
        break
    i=i+1
print(sum)"""

"""
a=[3,5,7,9]
sum=0
i=0
while i<len(a):
    if i==2:
        sum=sum+a[i]
        break
    i=i+1
    sum=sum+a[i]
print(sum)
"""
"""
a=[3,5,7,9]
sum=0
i=0
while i<len(a):
    if i==2:
        sum=sum+a[i]
        i=i+1
        continue
    sum=sum+a[i]
    i=i+1
    
print(sum)"""

"""
sum=0
i=5
while i!=0:
    if i==2:
        sum=sum+1
        i=i-1
        continue
    i=i-1
    
print(sum)"""

"""i = 1
while True:
    if i%7==0:
        break
    print(i)
    i+=1"""
