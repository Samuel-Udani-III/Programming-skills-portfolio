"""
Chapter 6
Exercise 2
A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their

age, and then tell them the cost of their movie ticket
"""
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

#Here, this code is utilizing a while loop again, along with an if-then-else format. 
#The loop runs until the user enters "quit" as their age. Then, the code converts the age the user 
#provided into an integer value before checking if it is less than or equal to a certain age. If the age provided 
#is less than 3, the user is told that they get entry for free, if it's less than 13, the user is told that their ticket is 
#$10, and if the age provided is 13 or greater, the user is told that their ticket is $15.