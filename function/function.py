"""def area_of_rectangle():
    
    l=10
    b=2
    a=l*b
    print(a)
area_of_rectangle()
#or 

def area_of_rectangle(b,l):
    
   
    a=l*b
    print(a)
area_of_rectangle(10,20)"""


"""def area_of_rectangle(b,l=40):
    
    
    a=l*b
    print(a)
area_of_rectangle(10,50) """# 50 will ovweride the l=40

"""def area_of_rectangle(*l):
    
    print(l)
area_of_rectangle(10,50,20,30)""" # * will print all in form of tuple Output is (10, 50, 20, 30)

"""
def area_of_rectangle(b,*l):
    
    print(l)
    print(b)
area_of_rectangle(10,50,20,30)""" #  will take first one being 10 and the l takes all

"""
def area_of_rectangle(**l):
    
    print(l)
area_of_rectangle(a=10,b=50,c=20,d=30)""" # ** will print all i  form of key and value  ( dictionory)



def area_of_rectangle(**l):
    total=0
    for i in l.values():
       total+=i
    print(total)
    print(l)
if __name__=="__main__":
 area_of_rectangle(a=10,b=20,c=30,d=40,e=40)



 #scope ,
 #  name_space, global name space , non local name space ,
 # global key
 # map filter , reduce
 # legb rule , lamda function