#1) You have a list containing mixed data types represented as strings. Write a Python 
# program using a filter() and lambda function to keep only the alphabetic items 
# (letters only) and remove any numeric strings from the 
# list." items = ['sql', '123', 'python']
"""
items = ['sql', '123', 'python']
f=list(filter(lambda x:x.isalpha() , items))
print(f)"""


#2) 
"""You are managing an e-commerce inventory database. Given a list of product
dictionaries, write a Python program using a filter() and lambda function to
extract and display only the products that are currently in stock (instock: True)
products = [
 {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
 {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':
False}
]"""

"""products = [
    {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
    {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock': False}
]

f = list(filter(lambda p: p['instock'], products))
print("Products currently in stock:")
for product in f:
    print(product)"""

#3) 
""" Given a list of course dictionaries, write a Python program using a lambda function
to filter and display only those courses that belong to the 'history' genre.
course = [ {'title': 'Ancient Civilizations', 'genre': 'history'}, {'title': 'Corporate
Finance', 'genre': 'commerce'}, {'title': 'Modern World History', 'genre': 'history'} ]"""

"""course = [
    {'title': 'Ancient Civilizations', 'genre': 'history'},
    {'title': 'Corporate Finance', 'genre': 'commerce'},
    {'title': 'Modern World History', 'genre': 'history'}]

f = list(filter(lambda c: c['genre'] == 'history', course))
print("Courses in the 'history' genre:")
for c in f:
    print(c)"""

#4) 
"""You have a list of blacklisted domains. Write a Python program using a lambda
function to filter a list of emails and return only the ones that are considered spam
those that match any domain in the blacklist.
emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net',
‘shyam.kumar@workcorp.com’]
blacklist = ('@hooya.com', '@malware.net') """
#

"""
emails = [
    'ram.sharma@gmail.com',
    'spam@hooya.com',
    'virus@malware.net',
    'shyam.kumar@workcorp.com' ]
blacklist = ('@hooya.com', '@malware.net')
spam_emails = list(filter(lambda e: any(domain in e for domain in blacklist), emails))
print("Spam emails:")
for email in spam_emails:
    print(email)"""

# 5) Applying a 20% discount to all items in a shopping cart:
# price = [100, 50, 200, 75] implement using lambda function
"""
price = [100, 50, 200, 75]
discounted_prices = list(map(lambda p: p * 0.8, price))
print("Original prices:", price)
print("Discounted prices:", discounted_prices)"""

# 6) Create a function, skip_two that takes a list as input, and returns a list that: 
# Startswith the second element of the input. While skipping every two elements. Does
# not keep any element whose index is greater than 11
"""
def skip_two(lst):
    return lst[1:12:3]

data = list(range(20))
result = skip_two(data)
print("Original list:", data)
print("Filtered list:", result)"""

#7)
"""7. Create a function, remove_at_idx, with the following features:
 Takes a list as its first argument.
 Takes a positive index as its second argument.
 Removes the element at the given index and decreases the index of all
subsequent elements by one.
 Returns a new list."""
"""
def remove_at_idx(lst, idx):
   
    if idx < 0 or idx >= len(lst):
        raise IndexError("Index out of range")
    
    return lst[:idx] + lst[idx+1:]
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
new_list = remove_at_idx(items, 2)  
print("Original list:", items)
print("New list:", new_list)"""

# 8)
"""You are developing a data-cleaning tool for a messaging application. The
application collects user input which may contain special characters like @, #, !,
%, etc., which could be problematic during processing or searching. To sanitize
this input, your task is to replace all special characters with a # symbol, while
keeping letters and digits unchanged. Write a Python program that:
 Accepts a string input from the user.
 Replaces all non-alphanumeric characters (special characters) with #.
 Prints the cleaned string"""

"""
def sanitize_input(user_input):
    cleaned = ''.join(map(lambda ch: ch if ch.isalnum() else '#', user_input))
    return cleaned

text = input("Enter your message: ")
print("Cleaned message:", sanitize_input(text))"""

# 9)
"""Write a Python program that implements a simple user registration and login
system with the following requirements:
Create a global dictionary called users_db to store user information. Implement a
register_user(username, password, email) function that:
 Checks if the username already exists and returns ‘Username
already exists’ if it does
 Stores the user's password and email in the database
 Returns a success message in the format: Registration successful for
{username}
Implement a login_user(username, password) function that:
 Returns ‘User not found’ if the username doesn't exist
 Returns ‘Incorrect password’ if the password is wrong
 Returns ‘Welcome back, {username}’ if login is successful
 Test the program by registering three users:
 ram with password ‘ram123’ and email ‘ram@email.com’
 shyam with password ‘shyam456’ and email ‘shyam@email.com’
 hari with password ‘hari231’ and email ‘hari@email.com’
"""

#---Answer=
"""
users_db = {}
def register_user(username, password, email):
    
    if username in users_db:
        return "Username already exists"
    users_db[username] = {
        'password': password,
        'email': email
    }
    return f"Registration successful for {username}"

def login_user(username, password):
    
    if username not in users_db:
        return "User not found"
    
    if users_db[username]['password'] != password:
        return "Incorrect password"
    
    return f"Welcome back, {username}"
print(register_user("ram", "ram123", "ram@email.com"))
print(register_user("shyam", "shyam456", "shyam@email.com"))
print(register_user("hari", "hari231", "hari@email.com"))

print(login_user("ram", "ram123"))        
print(login_user("shyam", "wrongpass"))   
print(login_user("unknown", "test123"))   """

# 10)
"""Develop a Python program for managing product inventory using a dictionary
stored in a list.
1. Initialize inventory as a list of dictionaries: [{'name': 'Laptop', 'price': 50000,
'quantity': 5}]
2. Menu options:
 Add new product (name, price, quantity)
 View all products in a formatted table
 Update product details (by product name)
 Delete a product
 Calculate total inventory value
 Exit
 3. Ensure price and quantity are positive numbers
 4. Prevent duplicate product names
 5. Show confirmation messages for all operations"""
"""
inventory = [{'name': 'Laptop', 'price': 50000, 'quantity': 5}]

def add_product(name, price, quantity):
    for product in inventory:
        if product['name'].lower() == name.lower():
            return "Product already exists!"
    if price <= 0 or quantity <= 0:
        return "Price and quantity must be positive numbers!"
    inventory.append({'name': name, 'price': price, 'quantity': quantity})
    return f"Product '{name}' added successfully!"

def view_products():
    if not inventory:
        return "Inventory is empty."
    print("\n--- Product Inventory ---")
    print("{:<15} {:<10} {:<10}".format("Name", "Price", "Quantity"))
    print("-" * 40)
    for product in inventory:
        print("{:<15} {:<10} {:<10}".format(product['name'], product['price'], product['quantity']))
    print("-" * 40)

def update_product(name, price=None, quantity=None):
    for product in inventory:
        if product['name'].lower() == name.lower():
            if price is not None:
                if price <= 0:
                    return "Price must be positive!"
                product['price'] = price
            if quantity is not None:
                if quantity <= 0:
                    return "Quantity must be positive!"
                product['quantity'] = quantity
            return f"Product '{name}' updated successfully!"
    return "Product not found!"

def delete_product(name):
    for product in inventory:
        if product['name'].lower() == name.lower():
            inventory.remove(product)
            return f"Product '{name}' deleted successfully!"
    return "Product not found!"

def calculate_total_value():
    total = sum(product['price'] * product['quantity'] for product in inventory)
    return f"Total inventory value: {total}"

while True:
    print("\n--- Inventory Management Menu ---")
    print("1. Add new product")
    print("2. View all products")
    print("3. Update product details")
    print("4. Delete a product")
    print("5. Calculate total inventory value")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        print(add_product(name, price, quantity))
    elif choice == '2':
        view_products()
    elif choice == '3':
        name = input("Enter product name to update: ")
        price = input("Enter new price (leave blank to skip): ")
        quantity = input("Enter new quantity (leave blank to skip): ")
        price = int(price) if price else None
        quantity = int(quantity) if quantity else None
        print(update_product(name, price, quantity))
    elif choice == '4':
        name = input("Enter product name to delete: ")
        print(delete_product(name))
    elif choice == '5':
        print(calculate_total_value())
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")"""



 # 11) 
"""Build a contact management system using nested data structures.
1. Initialize contacts as: [{'name': ’Ram kc’, 'phone': '9801234567', 'email':
'ram@email.com'}]
2. Menu features:
 Add contact (name, phone, email)
 Display all contacts
 Search contact by name
 Update contact information
 Delete contact
 Sort contacts alphabetically
 Exit
3. Validate phone number format (10 digits)
4. Validate email format (contains @ and.)
5. Prevent duplicate contacts"""

contacts = [
    {'name': 'Ram kc', 'phone': '9801234567', 'email': 'ram@email.com'}
]

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_email(email):
    return '@' in email and '.' in email

def add_contact(name, phone, email):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            return "Contact already exists!"
    if not validate_phone(phone):
        return "Invalid phone number! Must be 10 digits."
    if not validate_email(email):
        return "Invalid email format!"
    contacts.append({'name': name, 'phone': phone, 'email': email})
    return f"Contact '{name}' added successfully!"

def display_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("\n--- Contact List ---")
    print("{:<20} {:<15} {:<25}".format("Name", "Phone", "Email"))
    print("-" * 60)
    for c in contacts:
        print("{:<20} {:<15} {:<25}".format(c['name'], c['phone'], c['email']))
    print("-" * 60)

def search_contact(name):
    for c in contacts:
        if c['name'].lower() == name.lower():
            return f"Found: {c}"
    return "Contact not found!"

def update_contact(name, phone=None, email=None):
    for c in contacts:
        if c['name'].lower() == name.lower():
            if phone:
                if not validate_phone(phone):
                    return "Invalid phone number! Must be 10 digits."
                c['phone'] = phone
            if email:
                if not validate_email(email):
                    return "Invalid email format!"
                c['email'] = email
            return f"Contact '{name}' updated successfully!"
    return "Contact not found!"

def delete_contact(name):
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            return f"Contact '{name}' deleted successfully!"
    return "Contact not found!"

def sort_contacts():
    contacts.sort(key=lambda x: x['name'].lower())
    return "Contacts sorted alphabetically!"

while True:
    print("\n--- Contact Management Menu ---")
    print("1. Add contact")
    print("2. Display all contacts")
    print("3. Search contact by name")
    print("4. Update contact information")
    print("5. Delete contact")
    print("6. Sort contacts alphabetically")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        print(add_contact(name, phone, email))
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        name = input("Enter name to search: ")
        print(search_contact(name))
    elif choice == '4':
        name = input("Enter name to update: ")
        phone = input("Enter new phone (leave blank to skip): ")
        email = input("Enter new email (leave blank to skip): ")
        phone = phone if phone else None
        email = email if email else None
        print(update_contact(name, phone, email))
    elif choice == '5':
        name = input("Enter name to delete: ")
        print(delete_contact(name))
    elif choice == '6':
        print(sort_contacts())
    elif choice == '7':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 7.")