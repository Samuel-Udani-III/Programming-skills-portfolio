"""
Chapter 3
Exercise 7

"""


# Store the locations in a list
places_I_wanna_go_to = ['Akihabara', 'London', 'Texas', 'San Fransisco', 'Minnesota']

# Print your list in its original order
print(places_I_wanna_go_to)

# Use sorted() to print your list in alphabetical order without modifying the actual list
print(sorted(places_I_wanna_go_to))

# Show that your list is still in its original order by printing it
print(places_I_wanna_go_to)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
print(sorted(places_I_wanna_go_to, reverse=True))

# Show that your list is still in its original order by printing it again
print(places_I_wanna_go_to)

# Use reverse() to change the order of your list. Print the list to show that its order has changed
places_I_wanna_go_to.reverse()
print(places_I_wanna_go_to)

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order
places_I_wanna_go_to.reverse()
print(places_I_wanna_go_to)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed
places_I_wanna_go_to.sort()
print(places_I_wanna_go_to)

# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed
places_I_wanna_go_to.sort(reverse=True)
print(places_I_wanna_go_to)