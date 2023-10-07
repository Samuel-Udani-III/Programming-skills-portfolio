"""
Chapter 6
Exercise 1
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.
"""
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break
#Alright, so this code is a simple example of using a while loop to ask the user for any toppings they might like on their pizza and adding the toppings to a pizza one at a time... except not really, as you may notice that when the user enters "quit" as their topping, the code will break out of the loop entirely. If you do this long enough, you'll end up with an imaginary pizza topped with every single topping the programmer has included!