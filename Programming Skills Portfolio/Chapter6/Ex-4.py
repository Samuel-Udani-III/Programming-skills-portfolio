"""
Chapter 6
Exercise 4
Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,

move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
"""

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
    
#Sure! This code defines a list called "sandwich_orders" which stores various types of sandwiches, 
#such as a veggie, grilled cheese, turkey, and roast beef. It then defines an empty list called "finished_sandwiches" 
#which will be utilized later. It then enters a loop with the condition "while sandwich_orders" which will run until the list is empty, 
#in which it removes the first sandwich from the list, and then prints out to the console that it is making the sandwich in question. It 
#then finally adds the sandwich to the "finished_sandwiches" list.