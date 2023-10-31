"""
Chapter 5
Exercise 3
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

#This code does a very similar thing to the code before, but it does so by looping through the glossary dictionary, 
#printing every key-value pair. Here, it goes through the various key-value pairs of the dictionary, prints the key's title 
#followed by the value, and repeats it with the next pair, all the way until every single definition has been printed in the console. 
#This code is a good example of how you can loop through a python dictionary, and print out the key-value pairs one by one.

