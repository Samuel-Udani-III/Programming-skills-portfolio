"""
Chapter 1
Exercise 3
Write a Python program to display the current date and time.


"""

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =" , now)

#print the date like this dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
