                    # indexing and slicing is gonna be used for range function later
         # INDEXING
# name = "ram"
# print(name[0]) output = r
# -3 -2 -2
# r  a   m
# 0  1   2

         # SLICING

# slicing [start end step ]
# if step is not given then it works as +1 as defualt and if step value is put 0 then it will failm error will occer
#  if start and end both are not defined all word are printed eg {ram}
"""name="ram"
   print(name[:]) """
# start is defined and end is not defined then 1-last all are eg {a m}
"""    name="ram"
     print(name[1:])    """

""" name="ram"
print(name[0:-2]) # will print r   """

"""
name="rambahadur"
print(name[::4]) # will print rau 
name="rambahadur"
print(name[::-4]) # will print rha   """

#name="rambahadur"
#print(name[-5:-16:2]) # wont work

# name="rambahadur"
# print(name[11::-2]) # in this case  start value is positive so it 
#will end when the program goes to negative value  resulting ans as [rdhba]
"""
name="rambahadur"
print(name[1:-9:-2]) # both 1 and -9 are in sam eplace so it will be blank
""" 
a= 10
b= 20
print("{0}{1}".format(b,a,))

