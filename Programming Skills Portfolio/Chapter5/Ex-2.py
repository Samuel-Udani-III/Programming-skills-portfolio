"""
Chapter5
Exercise 2
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between

each word-meaning pair in your output.
"""

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

word = 'string'
print("\n" + word.title() + ": " + glossary[word])

word = 'comment'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'loop'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])


#This code is an example of utilizing a dictionary in Python, which is just a collection of 
#key-value pairs as stated above. In this case, "word" is a variable that is assigned a number of different values, 
#namely "string, comment, list, loop, dictionary." In every case, the same code has been used: "print word.title() + glossary[word], 
#which will print the word's title followed by the defined value in the glossary. This code is just an example of how one can use a 
#dictionary to store information for quick reference later on.