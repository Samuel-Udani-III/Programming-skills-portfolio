"""
Chapter 3
Exercise 5

"""


guests = ['Zetsubo Mishimune', 'Rozi Everlei', 'Akina Floresca', 'Azzy Jennings']
print("Guest list before change:", guests)


guest_who_cant_make_it = 'Azzy Jennings'
guests.remove(guest_who_cant_make_it)
print(f"{guest_who_cant_make_it} can't make it to the dinner.")


new_guest = 'Jeirin Head-vue'
guests.append(new_guest)


print("Guest list after change:", guests)


for guest in guests:
    print(f"Dear {guest}, You are invited to dinner at my place")
