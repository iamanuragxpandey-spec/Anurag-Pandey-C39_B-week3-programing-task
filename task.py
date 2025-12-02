# Write a program that ask the user for their full name and then prints a clean, formatted usernme .
'''
username=input('Enter your name:')
step1=username.split()
print('-'.join(step1))'''   
'''
username=input('Enter your name:  ')
step1=username.maketrans('aeios','@3!0$')
print(f'your agent code is :{username.translate(step1)}0##9')
'''
'''
#reverse word
User_input= "I love south indian movies"
step1 =User_input.split()
print(' '.join(step1[::-1]))
'''
# ask user for name  randpom order to first letter in capital 
# for eg joHN cENa to John Cena
#username = "Enter your full name" 
"""
phone_number=input('Enter your phone number:')
ste1p=phone_number.split()
step1=phone_number.maketrans('-+','  ')
step2=(f"+{phone_number.translate(step1)}")
print(''.join(step2))
"""
        
"""
images="image1.jpg"    
print(images.endswith((".jpg",".png")))"""

'''
email_name=input("enter your full email:")
step1=email_name.replace("."," ").replace("@")
print(f'Your username :{email_name.translate(step1)}') ''' 
# Extract everything before the '@'
# Ask the user for their email





email = input("Enter your email: ")
username = email.strip().split("@")[0].replace('.','')
print(f"your username:{username}")
