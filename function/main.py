"""a=875
b=288

while b!=0:
    a,b=b,a%b


print(a)"""

# map function

'''price=['$25','$34','$45']
f=list(map(lambda x:x.replace('$',''),price))
print(f)'''
'''
lst=[1,2,3]
f=list(map(lambda x:x+5,lst))
print(f)'''

# filter function
'''
lst=[1,2,3,4,5]
odd=list(filter(lambda x: x%2!=0,lst))
print(odd)'''
"""
items=[['ram',30],['shyam',40],['hari',40]]
f=list(filter(lambda x: x[1]>=40,items))
print(f)"""

'''
name=[['ram',30],['shyam',40],['hari',40]]
f=list(filter(lambda x: x[0].startswith('r'),name))
print(f)'''


'''
name=[['ram',30],['shyam',40],['hari',40],['ravi',70]]
f=list(filter(lambda e: e[0].startswith('r') and e[0].endswith('m'),name))
print(f)'''

