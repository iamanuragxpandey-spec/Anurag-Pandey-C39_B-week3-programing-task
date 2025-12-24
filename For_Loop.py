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
"""
list=[2,3,4,1,8,9]
list2=[]
for i in list[5::-1]:
    list2.append(i)
print(list2)
"""

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
"""
a=12
b=5
print(a^b)
"""
# quiestion model for exam mcq
"""
count=0
for x in [5,10,15]:
    count= count+1
    print(count)"""
"""
emails=[1,2,3]
for m in emails:
    print("New mail!")
    print("done")
"""
"""for i in [1,2]:
    print("A")
    for j in [1]:
        print("B")"""
"""
points=[1,2,3]
for p in points:
    print(p*2)"""
"""
friends=["Aman","Sarah","John"]
for f in friends:
    if f=="Sarah":
     continue
    print(f)"""
"""
folders=[["pic1"],["pic2","pic3"]]
for sub in folders:
    for item in sub:
        print(item)"""
"""
words=["hi","hello"]
for w in words:
    print(len(w))"""
"""
for i in range(8,5):
    print(i)"""
"""
for i in range(0,10,5):
    print(i)"""

"""
for row in range(6):
  for column in range(5):
    if (column==0 or column==1 or column==3 or column==4) and (row==0):
     print("*",end=' ')
    elif column==2:
     print("*",end=' ')
    else:
      print(end=' ')
  print()
  """
"""
for row in range(6):
   for column in range(5):
    if (column==0 or column==4) :
      print("*",end=" ")
    elif (column==1 or column==3) and (row==4):
      print("*",end=" ")
    elif (column==2) and (row==3):
      print("*",end=" ")
    else:
      print(end="  ")
   print()"""
'''
items={'name':'rita','age':'21'}
for i in items.items():
    print(i)'''
'''
items={'name':'rita','age':'21'}
for i,i in items.items():
    print(i,i)'''
"""
quiz_questions={'Qno1':{'Question':'What is the correct way to create anf-string in Python?','option':
          {'a':'f"Hello {name}"','b':'"Hello {name}"','c':'$"Hello {name}"','d':'fmt"Hello {name}"'},"correct_answer":'a'},
          'Qno2':{'Question':'Question Which of the following statements is used to create an empty set in Python?','option':
                  {'a':'{*()} ','b':'set( )','c':'( )','d':'both ab'},'correct_answer':'d'} }







score=0
for key,value in quiz_questions.items():
    print(key,' ',value['Question'])
    for key,j in value['option'].items():
        print(key,'',j)
    choice=input("choose the correct options:(a,b,c,d)")
    if choice==value['correct_answer']:
        score+=1
    else:
        pass
print(f"Your final score is {score}")
"""

word=str(input("Enter the sentence you want:"))
vowels=set()
for i in word:
    if i in  "aeiou" :
        vowels.add(i)
print(vowels)
print(len(vowels))