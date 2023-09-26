"""
Chapter 2
Exercise 5

"""

def calculate_usb_sticks(total_pounds, cost_per_stick):
    num_sticks = total_pounds // cost_per_stick
    pounds_left = total_pounds % cost_per_stick
    return num_sticks, pounds_left

total_pounds = 50
cost_per_stick = 6

num_sticks, pounds_left = calculate_usb_sticks(total_pounds, cost_per_stick)

print(f"The girl can buy {num_sticks} USB sticks and will have £{pounds_left} left.")