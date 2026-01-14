"""dictionary={}
unique_words=set()
user_input=int(input('how many words do you want to add:'))
for i in range(1,user_input+1):
    choice=int(input('press1. add 2. display 3. remove 4. exit'))
    if choice==1:
         word=input('enter a word: ')
         if word in unique_words:
           print(f'{word} already exists')
         else:
          meaning=input('enter a meaning: ')
          dictionary[word]=meaning
          unique_words.add(word)
    elif choice==2:
       for key,value in sorted(dictionary.items()):
          print(key,' ',value)
    elif choice==3:
       word=input('enter a word you want to remove: ')
       if word not in unique_words:
          print(f'{word} does not exists')
       else:
          dictionary.pop(word)
          unique_words.remove(word)
    elif choice==4:
       break
print(unique_words)

"""
#2 
"""
items=[]
item_purchased=int(input("how many items you purchased: "))

total_price=[]
for i in range(item_purchased):
    name=input("enter items name: ")
    price=float(input("enter the price of item: "))
    items.append(name)
    total_price.append(price)

total=sum(total_price)
print("total price:" ,total)"""


