#List
##append extend insert

#append
"""items=[1,2,3] 
items.append(1) # append cant add 2 at once 
 # eg items.append("ram", "shyam") will be  error list.append only takes 1 argument
print(items)"""
 #extend 
"""items=[123]
items.extend("1")
print(items)"""

"""items=[123]
items.extend(['shyam','ram'])
print(items)"""

#insert
"""items=[1,2,3]
items.insert(0,['shyam','ram'])
print(items)"""
 
# Updating The Elements Of A List

"""
items=[1,2,3]
items[0]='ram'
print(items)"""

# Python List Remove
"""
items=[1,2,3] #remove pop
items.remove(1) # or items.remove[items](0)
print(items)"""

'''items=[1,2,3]
result=items.pop(items[2])
print(result)'''

"""items=[1,2,3]
result=items.pop()
print(result)"""
'''
items=[1,2,3,'ram','shyam','hari','gita']
print(items)
items.insert(1,items.pop(5))

print(items)'''


"""items=[5,3,1,2,1]
items.sort()   # put the values into accending order = [1, 1, 2, 3, 5]
print(items)


items=[5,3,1,2,1]
items.sort(reverse=True)   # put the values into dcaccending order
print(items)"""



# Tuple 
# it is not mutable 


"""
items = (1, 2, 3, 4)
items=list(items)
items[3]="4"
print(tuple(items))"""


# set
#Set is a collection which is unordered and unindexed.
#It does not allow duplicate members.
#A set itself may be modified (mutable), but the elements contained in the set must be of an immutable type.
#Set can be used to perform mathematical set operations like union, intersection, symmetric differences etc.
#A set is created by placing all the items (elements) inside curly braces { }.



"""
items=()
print(type(items))
 # to create empty set
items={*()}
print(type(items))"""

"""items={'ram',1,'shyam',4}
items.add(5)
print(items)"""
"""
items={'ram',1,'shyam',4}
items.remove(5) # if given discaed value is not there it say error
print(items) 
BUT in  
items={'ram',1,'shyam',4}
items.discard(5) # if given discaed value is not there it return og valuess
print(items)"""


"""
items={'ram',1,'shyam',4}
print(items)
items.pop()  # removes first value in set
print(items)"""

"""items={'ram',1,'shyam',4}
items.clear
print(items)"""

# union set
"""data1={1,2,3,4}
data2= {3,4,5,6}
union_set = data1 | data2
print(union_set)"""



#intersection_set
"""data1 = {1,2,3,4}
data2= {3,4,5,6}
intersection_set = data1 & data2
print(intersection_set)"""


"""data1 = {1,2,3,4}
data2= {3,4,5,6}
result=data1.difference(data2)
print(result)"""


#Dictinoary

#Add
"""student_record={'ram':98098,'shyam':2344}
student_record['sagar']='9876'
print(student_record)"""

"""student_record={'ram':98098,'shyam':2344}
student_record.update({'hari':7999})
print(student_record)"""

"""student_record={'ram':9808,'shyam':2344}
result=student_record.get('ram')
print(result)"""


# pop remove
"""student_record={'ram':98098,'shyam':2344}
result=student_record.pop('ram')
print(result)


student_record={'ram':98098,'shyam':2344}
student_record.pop('ram')
print(student_record)"""

"""
student_record={'ram':98098,'apple':9878,'shyam':2344}
student_record=dict(sorted(student_record.items()))

new_key='RAM'
old_key='ram'
student_record[new_key]=student_record.pop(old_key)
print(student_record)"""


"""student_list={'id1':{'name':'ram','gender':'male','age':12}}
print(student_list['id1']['gender'])"""


# task








#2
"""
first_set={23,42,65,57,78,83,29}
second_set={57,83,29,67,73,43,48}
intersection_set=first_set & second_set
print(intersection_set)
result=first_set.difference(intersection_set)
print(result)"""

#3










#5
"""sample_list=[87,45,41,65,94,41,99,94]
step1=set(sample_list)
step2=tuple(step1)
print(f"max no:{max(step2)}")
print(f"min no:{min(step2)}")"""

