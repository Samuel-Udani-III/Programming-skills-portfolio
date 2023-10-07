"""
Chapter 3
Exercise 5
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.
"""


guests = ['Zetsubo Mishimune', 'Rozi Everlei', 'Akina Floresca', 'Azzy Jennings']
print("Guest list before change:", guests)

# Azzy can't make it to the party
guest_who_cant_make_it = 'Azzy Jennings'
guests.remove(guest_who_cant_make_it)
print(f"{guest_who_cant_make_it} can't make it to the dinner.")

#So I added a new guest ussing this function
new_guest = 'Jeirin Head-vue'
guests.append(new_guest)

#Then print the final list
print("Guest list after change:", guests)


for guest in guests:
    print(f"Dear {guest}, You are invited to dinner at my place")
