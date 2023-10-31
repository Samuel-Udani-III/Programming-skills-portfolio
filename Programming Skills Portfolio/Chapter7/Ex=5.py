"""
Chpater 7
Exercise 5
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,

such as Reykjavik is in Iceland. Give the parameter for the country a default value.

Call your function for three different cities, at least one of which is not in the default country.
"""
def describe_city(city, country='chile'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')

#Alright, here is a function called "describe\_city". It has two required parameters, "city" and "country". In this case, 
#"Country" is being set to Chile by default. Once this is done, it takes the "city" parameter, and concats it with "is in " 
#and then the "country" parameter, and concats it with ". ". It then prints this message onto the console.

#For example, if "santiago" and "Chile", we get "Santiago is in Chile."