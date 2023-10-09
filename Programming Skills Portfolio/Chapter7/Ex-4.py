"""
Chapter 7
Exercise 4
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

medium shirt with the default message, and a shirt of any size with a different message.
"""

def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')
#Alright, so this function is basically the same thing as before, but with some changes. Here, it accepts a required argument of "size" and a required argument of "message." The function prints that it will create a large t-shirt, and then print the message provided. It then finally allows you to create shirts with various sizes, as well as various messages. If you provide no arguments, the default message of "large" and "I love Python" will be used!