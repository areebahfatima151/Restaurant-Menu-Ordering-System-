# Define the menu of the restaurant
menu = {
    'Pizza': 100,
    'Pasta': 150,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 40,
}

# Greet the customer
print("Welcome to PYTHON Restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

# First item
item_1 = input("Enter the name of the item you want to order: ").title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Sorry, the item '{item_1}' is not available.")

# Second item (optional)
another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()

if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").title()

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Sorry, the item '{item_2}' is not available.")

# Final bill
print(f"The total amount to pay is: Rs{order_total}")