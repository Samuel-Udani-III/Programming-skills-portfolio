"""
Chapter 1
Exercise 3
Write a Python program to display the current date and time.


"""

from datetime import datetime

# datetime is a part of the python library and it contains current date and time and can be used to show it in the output
now = datetime.now()

print("now =" , now)

#This prints the time in the H:M:S format when it is outputted
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
