"""
Chapter 3
Exercise 2
Start with the list you used in Exercise 1, but instead of just

printing each person’s name, print a message to them. The text of each message should be the same, but each message should be

personalized with the person’s name.
"""
# I used the same list from exercise 1 and print a sentence using the list from the variable
names = ['Zetsu', 'Rozi', 'Aki', 'Az']

for name in names:
    print(f"Sup, {name}! Have a good day mates.")