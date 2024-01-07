# Define the items and their codes
items = {"A1": {"name": "Coca-Cola", "price": 2.5, "stock": 10},
         "A2": {"name": "Al Ain Water", "price": 1.5, "stock": 15},
         "B1": {"name": "Lays", "price": 10, "stock": 8},
         "B2": {"name": "KitKat", "price": 2, "stock": 5},
         "C1": {"name": "Milk", "price": 8.5, "stock": 15},
         "C2": {"name": "Sandwiches", "price": 6, "stock": 10},
         "D1": {"name": "Sprite", "price": 2.5, "stock": 10},
         "D2": {"name": "Soy Milk", "price": 15, "stock": 7},
         "E1": {"name": "Toblrerone", "price": 14.20, "stock": 15},
         "E2": {"name": "Chesse Rings", "price": 5, "stock": 10}}

# Define the coins and their values
coins = {0.25: 10, 0.5: 10, 1: 10, 5: 10, 10: 10, 20: 10, 50: 10, 100: 10}

# Define a function to display the items
def display_items():
    print("Welcome to the vending machine!")
    print("Here are the items available:")
    for code, item in items.items():
        print(f"{code}: {item['name']} - {item['price']} AED - {item['stock']} left")

# Define a function to insert coins and return the balance
def insert_coins():
    balance = 0
    print("Please insert coins:")
    while True:
        coin = input("Enter the value of the coin or 'done' to finish: ")
        if coin == "done":
            break
        try:
            coin = float(coin)
            if coin in coins:
                balance += coin
                coins[coin] += 1
                print(f"Your balance is {balance} AED")
            else:
                print("Invalid coin value")
        except:
            print("Invalid input")
    return balance

# Define a function to select an item and return the change
def select_item(balance):
    while True:
        code = input("Enter the code of the item you want or 'cancel' to cancel: ")
        if code == "cancel":
            return balance
        if code in items:
            item = items[code]
            if item["stock"] > 0:
                if balance >= item["price"]:
                    balance -= item["price"]
                    item["stock"] -= 1
                    print(f"You have selected {item['name']}")
                    print(f"Your change is {balance} AED")
                    return balance
                else:
                    print("You do not have enough balance")
            else:
                print("This item is out of stock")
        else:
            print("Invalid item code")

# Define a function to return the change in coins
def return_coins(change):
    print("Here are your coins:")
    for coin in sorted(coins, reverse=True):
        while change >= coin and coins[coin] > 0:
            print(coin)
            change -= coin
            coins[coin] -= 1
    if change > 0:
        print(f"Sorry, the vending machine does not have enough coins to return {change} AED")

# Main program
display_items()
balance = insert_coins()
change = select_item(balance)
return_coins(change)
print("Thank you for using the vending machine!")
