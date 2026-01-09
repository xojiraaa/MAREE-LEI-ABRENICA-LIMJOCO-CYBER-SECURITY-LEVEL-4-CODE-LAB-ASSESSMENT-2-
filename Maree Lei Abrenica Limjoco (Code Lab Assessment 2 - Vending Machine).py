# The list below shows the various snacks and beverages that can be purchased using the vending machine, including each products' price and the number of stocks remaining.
Items = {
    'A1': {'Name': "Pepsi", 'Cost': 2.50, 'Stock': 12},
    'A2': {'Name': "Coca Cola Cherry", 'Cost': 2.50, 'Stock': 9},
    'A3': {'Name': "Diet Pepsi", 'Cost': 2.50, 'Stock': 13},
    'A4': {'Name': "Coca Cola Zero", 'Cost': 2.50, 'Stock': 7},
    'A5': {'Name': "Red Bull", 'Cost': 10.00, 'Stock': 15},
    'A6': {'Name': "Monster Energy Drink", 'Cost': 9.50, 'Stock': 10},
    'A7': {'Name': "Masafi Water", 'Cost': 1.50, 'Stock': 15},
    'A8': {'Name': "Evian Water", 'Cost': 4.80, 'Stock': 11},
    'A9': {'Name': "Dr. Pepper Vanilla", 'Cost': 9.50, 'Stock': 9},
    'A10': {'Name': "Chocolate Milk", 'Cost': 3.50, 'Stock': 10},
    'B1': {"Name": "Espresso", 'Cost': 2.00, 'Stock': 5},
    'B2': {"Name": "Cappuccino", 'Cost': 5.50, 'Stock': 8},
    'B3': {"Name": "Hot Chocolate", 'Cost': 4.50, 'Stock': 3},
    'B4': {"Name": "Green Tea", 'Cost': 5.00, 'Stock': 7},
    'B5': {"Name": "Karak Chai", 'Cost': 1.50, 'Stock': 2},
    'B6': {"Name": "Latte", 'Cost': 7.50, 'Stock': 5},
    'B7': {"Name": "Lemon Ginger Tea", 'Cost': 3.50, 'Stock': 13},
    'B8': {"Name": "Hot Milk", 'Cost': 2.50, 'Stock': 7},
    'B9': {"Name": "Peppermint Tea", 'Cost': 4.00, 'Stock': 3},
    'B10': {"Name": "Decaf", 'Cost': 3.50, 'Stock': 5},
    'C1': {"Name": "Flaming Hot Cheetos", 'Cost': 4.00, 'Stock': 7},
    'C2': {"Name": "Peanut M&M's", 'Cost': 4.00, 'Stock': 11},
    'C3': {"Name": "McVities Digestive", 'Cost': 6.50, 'Stock': 15},
    'C4': {"Name": "Kinder Bueno", 'Cost': 2.50, 'Stock': 10},
    'C5': {"Name": "Sweet Chili Doritos", 'Cost': 3.00, 'Stock': 3},
    'C6': {"Name": "Salt & Vinegar Lays", 'Cost': 2.95, 'Stock': 10},
    'C7': {"Name": "Nature Valley Protein Bar", 'Cost': 11.00, 'Stock': 12},
    'C8': {"Name": "Reese's", 'Cost': 3.50, 'Stock': 5},
    'C9': {"Name": "Skittles", 'Cost': 5.00, 'Stock': 14},
    'C10': {"Name": "Salad Chips", 'Cost': 1.50, 'Stock': 10},
}

# The organized list below shows the sectioning of the products.
Organized_List = ['Cold_Beverages', 'Hot_Beverages', 'Snacks']

# The list of cold beverages, their price, and number of stocks.
Cold_Beverages = {
    'A1': {'Name': "Pepsi", 'Cost': 2.50, 'Stock': 12},
    'A2': {'Name': "Coca Cola Cherry", 'Cost': 2.50, 'Stock': 9},
    'A3': {'Name': "Diet Pepsi", 'Cost': 2.50, 'Stock': 13},
    'A4': {'Name': "Coca Cola Zero", 'Cost': 2.50, 'Stock': 7},
    'A5': {'Name': "Red Bull", 'Cost': 10.00, 'Stock': 15},
    'A6': {'Name': "Monster Energy Drink", 'Cost': 9.50, 'Stock': 10},
    'A7': {'Name': "Masafi Water", 'Cost': 1.50, 'Stock': 15},
    'A8': {'Name': "Evian Water", 'Cost': 4.80, 'Stock': 11},
    'A9': {'Name': "Dr. Pepper Vanilla", 'Cost': 9.50, 'Stock': 9},
    'A10': {'Name': "Chocolate Milk", 'Cost': 3.50, 'Stock': 10},
}

# The list of hot beverages, their price, and number of stocks.
Hot_Beverages = {
    'B1': {"Name": "Espresso", 'Cost': 2.00, 'Stock': 5},
    'B2': {"Name": "Cappuccino", 'Cost': 5.50, 'Stock': 8},
    'B3': {"Name": "Hot Chocolate", 'Cost': 4.50, 'Stock': 3},
    'B4': {"Name": "Green Tea", 'Cost': 5.00, 'Stock': 7},
    'B5': {"Name": "Karak Chai", 'Cost': 1.50, 'Stock': 2},
    'B6': {"Name": "Latte", 'Cost': 7.50, 'Stock': 5},
    'B7': {"Name": "Lemon Ginger Tea", 'Cost': 3.50, 'Stock': 13},
    'B8': {"Name": "Hot Milk", 'Cost': 2.50, 'Stock': 7},
    'B9': {"Name": "Peppermint Tea", 'Cost': 4.00, 'Stock': 3},
    'B10': {"Name": "Decaf", 'Cost': 3.50, 'Stock': 5},
}

# The list of snacks, their price, and number of stocks.
Snacks = {
    'C1': {"Name": "Flaming Hot Cheetos", 'Cost': 4.00, 'Stock': 7},
    'C2': {"Name": "Peanut M&M's", 'Cost': 4.00, 'Stock': 11},
    'C3': {"Name": "McVities Digestive", 'Cost': 6.50, 'Stock': 15},
    'C4': {"Name": "Kinder Bueno", 'Cost': 2.50, 'Stock': 10},
    'C5': {"Name": "Sweet Chili Doritos", 'Cost': 3.00, 'Stock': 3},
    'C6': {"Name": "Salt & Vinegar Lays", 'Cost': 2.95, 'Stock': 10},
    'C7': {"Name": "Nature Valley Protein Bar", 'Cost': 11.00, 'Stock': 12},
    'C8': {"Name": "Reese's", 'Cost': 3.50, 'Stock': 5},
    'C9': {"Name": "Skittles", 'Cost': 5.00, 'Stock': 14},
    'C10': {"Name": "Salad Chips", 'Cost': 1.50, 'Stock': 10},
}

# This prints at the start-up of the vending machine.
print("── .✦ Lei's Vending Machine ✦.──")
print("────── Vending Machine Items Data ──────")

for key, item in Items.items():
    print(f"{key}) {item['Name']} -- {item['Cost']} -- {item['Stock']}")

# Asks the user if they want to sort the choices into hot beverages, cold beverages, and snacks, or display it altogether.
print("────── Would you like to sort the choices? ──────")

# This loops until the input is valid for sorting.
while True:
    Organized = str(input("Please input 'yes' or 'no':")).strip().lower()
    if Organized == "yes":
        print("Please choose which list you want to view.")
        print(Organized_List, sep=' / ')
        Chosen_Org = str(input("\nEnter your chosen list here: ")).strip().lower()
        if Chosen_Org == "cold beverages":
            for key, item in Cold_Beverages.items():
                print(f"     {key}, {item['Name']}, {item['Cost']}, {item['Stock']}")
        elif Chosen_Org == "hot beverages":
            for key, item in Hot_Beverages.items():
                print(f"     {key}, {item['Name']}, {item['Cost']}, {item['Stock']}")
        elif Chosen_Org == "snacks":
            for key, item in Snacks.items():
                print(f"     {key}, {item['Name']}, {item['Cost']}, {item['Stock']}")
        else:
            print("Invalid request. Make sure to input a valid item number (e.g. 'A1', 'B2', 'C3').")
        break  
    elif Organized == "no":
        break
    else:
        print("Invalid choice. Please input 'yes' or 'no':")

# Below is the main loop for purchasing items in the vending machine.
while True:
    product = input("Please enter the item number you would like to purchase: ")
    if product in Items:
        selected_item = Items[product]
        if selected_item['Stock'] <= 0:
            print("Sorry, unfortunately this item is out of stock. Please choose another item.")
            continue  # If an item is out of stock, the user can choose another item.
        print(" ")
        print(f"You have chosen {selected_item['Name']}.")
        print(" ")
        amount_due = selected_item['Cost']

        while amount_due > 0:
            try:
                payment = float(input(f"Please insert {amount_due:.2f}: "))
                if payment >= amount_due:
                    change = payment - amount_due
                    # This decreases the number of stocks of a certain product after the user makes their purchase.
                    Items[product]['Stock'] -= 1
                    print(" ")
                    print(f"── .✦ You have successfully purchased {selected_item['Name']} ✦.──")
                    print(" ")
                    print(f"Thank you for choosing Lei's Vending Machine! Your total change is {change:.2f}")
                    break
                else:
                    print("Insufficient amount. Please insert more coins/bills.")
                    amount_due -= payment
            except ValueError:
                print("Invalid payment amount. Please enter a valid number.")
 
        # After purchasing an item, the vending machine asks if they want another item or not.
        while True:
            another = input("Would you like to purchase another item? Please input 'yes' or 'no':").strip().lower()
            if another == "yes":
                break  # This goes back to the main loop since the user has decided to purchase another item.
            elif another == "no":
                print("Thank you for using Lei's Vending Machine!")
                exit()  # This ends the program since the user has decided not to purchase another item.
            else:
                print("Invalid choice. Please input 'yes' or 'no':")
    else:
        print("Invalid selection. Please try again.")