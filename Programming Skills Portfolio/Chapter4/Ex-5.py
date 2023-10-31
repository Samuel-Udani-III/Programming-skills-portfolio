"""
Chapter 4
Exercise 5
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

•Make a list of your three favorite fruits and call it favorite_fruits.

•Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block

should print a statement,such as You really like bananas!
"""
favorite_fruits = ['cherrys', 'mango', 'oranges']

if 'watermelon' in favorite_fruits:
    print("You really like watermelons!")
if 'oranges' in favorite_fruits:
    print("You really like oranges!")
if 'cherrys' in favorite_fruits:
    print("You really like cherry!")
if 'grapes' in favorite_fruits:
    print("You really like grapes!")
if 'mango' in favorite_fruits:
    print("You really like mangos!")
    
#Here's an explanation of that code:

#"favorite\_fruits" is a list containing "cherrys, mango, and oranges.

#The code checks whether a specific fruit is in the list, and then if it is, it prints a message to the console. 
#It does this for five different fruits: watermelon, oranges, cherries, grapes, and mango. If your favorite fruit 
#is one of the ones within the list, you'll get a message that says "You really like..." that particular fruit. 
#It's just a simple code checking for specific fruits within a list!