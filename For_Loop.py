#for loop

# for variable_name in sequence/range.
"""
items=[1,2,3,4]
for i in items:
    print(i)"""

"""items=[1,2,3,4]
for i in range(len(items)):
    print(items[i])"""
"""
items=[1,2,3,4]
for i in range(len(items)):
    print(i,"",items[i])
    # 0 1 
    # 1 2
    # 2 3
    # 3 5"""
"""
num=int(input("enter the number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)"""

"""
num=int(input("enter the number:"))
for i in range(10,0,-1):
    print(num,"x",i,"=",num*i)"""

"""
num=int(input("enter the number:"))
if num%2==0:
    print("it is even")
else:
    print("odd")
# without loop we cant check all numbers in a list if there are even or odd"""

"""
items=[1,2,3,4,5,6,7,8,9,10]
for i in items:
    if i%2==0:
     print(f'{i} is even')"""

"""
items=[1,2,3,4,5,6,7,8,9,10]
evennumbers=[]
for i in items:
    if i%2==0:
      evennumbers.append(i)
print(evennumbers)"""
"""
text = 'python programming'
vowels = []
consonants = []
unique_vowels = set()

for ch in text:
    if ch in "aeiou":
        vowels.append(ch)
        unique_vowels.add(ch)
    else:
        consonants.append(ch)

print("All vowels:", vowels)
print("Unique vowels:", unique_vowels)
print("Consonants:", consonants)"""


# no2 
"""
numbers = [1, 2, 3, 4, 5]
total = 0
for i in numbers:
    total += i

print("Sum of the list:", total)"""

# no3
'''
numbers = [1,3,4,'a',5,11,-11,12,-13]
total = 0
for i in numbers:
 if isinstance(i,int):
     if i>0:
      if  i%2==0:
        total += i
 
     
print(f'sum of all even number is {total}')'''

list=[2,3,4,1,8,9]
list2=[]
for i in list[5::-1]:
    list2.append(i)
print(list2)


# Nested for  Loop

'''
floor=['floor1','floor2','floor3']
room=['roomno1','roomno2','roomno3']
for i in floor:
    print(i)
    for j in room:
        print(j)
'''
"""
floor=['floor1','floor2','floor3']
room=['roomno1','roomno2','roomno3']

for i in floor:
    print(i)
    for j in room:
        if i=='floor1' and  j=='roomno1':
         print(j)          
        elif i=='floor3'and j=='roomno3':
           print(j)"""

"""
list=[4,8,7,9]
for i in list:
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()"""
"""
a={1,2,3,4}
b={3,4,5}
print(a.difference(b))"""

a=12
b=5
print(a^b)

