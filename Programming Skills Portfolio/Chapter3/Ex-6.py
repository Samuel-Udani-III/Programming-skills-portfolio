"""
Chapter 3
Exercise 6

"""


guests = ['Zetsubo Mishimune', 'Rozi Everlei', 'Akina Floresca', 'Azzy Jennings', 'Jeirin Head-vue']

print("You can invite only two people for dinner.")

while len(guests) > 2:
    guest = guests.pop()
    print(f"Sorry, {guest}, I can't invite you to dinner.")

print(f"\n{guests[0]} and {guests[1]}, you're still invited to dinner!")

del guests[0]
del guests[0]

print(f"\nGuest list: {guests}")
