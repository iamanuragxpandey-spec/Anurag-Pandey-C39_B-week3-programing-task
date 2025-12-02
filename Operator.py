"""
num1= 12
num2=13
print(num1**num2) # means 13 is power of 12  
# ***
# ///
print(num1/num2) # / means divide 
print(num1//num2)# divides but gives answer in int value not in float """
# assainment operator
# = means value asigin 
# += , -= , *= ,/=

"""
age = 21
age+=5 # cant give gap between age+ and =5 ( concatinate )
# or 
# age =age+5
print(age) """

"""
list1=[1,2,3,4]
list2=list1
list1+=list2 # here this concatinate makes it change change the original value makinhg both change
print(list1)
print(list2)





list1=[1,2,3,4]
list2=list1
list1= list1 + list2 # thisc only change the value of list 1 andd not of list 2 not changing original value
print(list1)
print(list2) 

"""
"""
list1=[1,2,3,4]
list1.append(5)
print(list1) """

# comparission operator is used  for decison making
"""num1=12
num2=14
if num1==num2:
    print("both are equal")
else:
    print("both are not equal") """

"""num1=12
num2=14
if num1>num2:
    print("num1 is greater then num2")
    ifelse:print("both are equal")
else:
    print("num2 is greater hthen num2")
"""
"""num1=14
num2=14
if num1>=num2:
    print("num1 is greater then num2") 
    
else:
    print("num2 is greater hthen num2")
    # in thgis case where both are true then first case will be picked in this caase if will be selected
"""
# logical operator
"""num1= 15
num2= 14
if num1!=num2 or num1%4==0: # if there is (and) then both should be true to get the answer true
    print("true") # if there is or then there should be both false to get ouput false
else:
    print("false")"""

"""
# membership operator
# in not in
student_name=["ram","laxman","hari"]
name=input("enter a student name:")
if name in student_name:
    print(f"{name} is present ")
else :
    print(f"{name}is not present")
 # not in  is opposite of in if there is then its false if there is  not then its true
student_name=["ram","laxman","hari"]
name=input("enter a student name:")
if name  not in student_name:
    print(f"{name} true")
else :
    print(f"{name}false")
    """
"""
# identiy operator
name1="ram"
name2 ="shyam"
print(id(name1))
print(id(name2))
print(name1 is name2)
"""
# Bitwise Operator

# & And , | OR, ^ XOR, ~  NOT (negation ),  Bitwise left shift << , Bitwise left shift >>

num1 =12 
num2 = 13
print(num1& num2)