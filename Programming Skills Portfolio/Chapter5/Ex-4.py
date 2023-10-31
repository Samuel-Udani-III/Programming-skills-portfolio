"""
Chapter 5
Exercise 4
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())
    
#This code is a sample of utilizing a dictionary once more! In this case, the rivers dictionary has key-value 
#pairs that tie the names of major rivers to the countries that they flow through. The first part of the code loops through the 
#river/country pairs, and prints the name of the river and the associated country in the dictionary. Then, the latter part of the code 
#goes through the river keys, and prints out all of the rivers listed in the definition, and then goes through the country values, 
#listing out what countries are involved in the data set. This is a great example how to utilize a dictionary for data storage.