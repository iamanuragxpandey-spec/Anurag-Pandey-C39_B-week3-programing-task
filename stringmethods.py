
"""
age = ""1""
print(type(age)) # type to check datetype

"""
"""
items=["apple","banana"]
print(items)
items.append = ["mango"]
print(items) 
"""
"""
name="laxman"
result=name.upper()
print(result)

name="laxman"
result=name.center(12)
print(result)
"""

"""
name="laxman"
result=name.center(12,'%')
print(result)
#if length even left_side = n+1/2 right_side=n-1/2
# if length odd left_side = n-1/2 right_side =n+1/2


name="laxman"
result=name.ljust(12,'%') # for only right side
print(result)

name="laxman"
result=name.rjust(12,'%') # for only left side
print(result)

"""
"""
print("*"*30)
invoice_no=7
customer_name="john doe".title()
amount=199.99
print("INVOICE".center(31))
print(f"Invoice_No: INV-{str(invoice_no).rjust(5,"0")}".center(31))
print(f"Customer:{customer_name}".center(27))
print(f"Amount:{amount}".center(24))
print("*"*30)
"""

ticket_no=12007
movie= "inception"
seat = "F-12"
show_time= " 07:30 PM"
print("*"*30)
print("MOVIE TICKERT".center(31))
print(f"Ticket:TXT-{str(ticket_no)}".center(30))
print(f"Movie:{movie}".center(29))
print(f"Seat:{str(seat)}".center(24))
print(f"Time:{ show_time}".center(28))
print("*"*30)