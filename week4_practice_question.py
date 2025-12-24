#Qno.1
"""
word=str(input("Enter the sentence you want:"))
vowels=set()
for i in word:
    if i in  {'a','e','i','o','u'} :
        vowels.add(i)
print(vowels)
print(len(vowels))"""

# Qno.2
"""
user_input=int(input("How many words you want to add: "))
dictionary={}
unique_word=set()
for i in range(user_input):
    print("Choose any one option")
    choice=int(input(" Press 1. add 2.display 3.remove 4.exit"))
    if choice==1:
        word=input("Enter the word you want to add: ")
        if word in unique_word:
            print(f"{word} already exist")
        else:
            meaning=input("enter the meaning: ")
            dictionary[word]=meaning
            unique_word.add(word)
    elif choice==2:
        for key,value in sorted(dictionary.items()):
          print(key,' ',value)
    elif choice==3:
        word=input("Enter the word you want to remove: ")
        if word not in unique_word:
          print(f'{word} does not exists')
        else:
          dictionary.pop(word)
          unique_word.remove(word)
    else:
       break
print(unique_word)"""


# QNO3.
 
import random
quiz_questions = {
    1: {
        "question": "What is the capital of France?",
        "options": {
            "A": "Berlin",
            "B": "Madrid",
            "C": "Paris",
            "D": "Rome"
        },
        "answer": "C"
    },
    2: {
        "question": "Which planet is known as the Red Planet?",
        "options": {
            "A": "Earth",
            "B": "Mars",
            "C": "Jupiter",
            "D": "Saturn"
        },
        "answer": "B"
    },
    3: {
        "question": "Who developed the theory of relativity?",
        "options": {
            "A": "Isaac Newton",
            "B": "Albert Einstein",
            "C": "Galileo Galilei",
            "D": "Nikola Tesla"
        },
        "answer": "B"
    }
}
question_keys = list(quiz_questions.keys())
random.shuffle(question_keys)

score = 0
for key in question_keys:
    q = quiz_questions[key]
    print("\n" + q["question"])  
    
    for option_key, option_value in q["options"].items():
        print(f"{option_key}: {option_value}")
    
    user_answer = input("Enter your choice (A/B/C/D): ").upper()
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}")

print("\nQuiz Completed!")
print(f"Your final score is: {score}/{len(quiz_questions)}")