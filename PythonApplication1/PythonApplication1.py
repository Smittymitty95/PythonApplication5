# Part 1: Display the heading
print("Welcome to the Price Calculator")

# Function to prompt user for price
def get_price():
    while True:
        try:
            price = float(input("Enter the price: "))
            return price
        except ValueError:
            print("Invalid price format. Please enter a valid price.")

# Function to prompt user for quantity
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            return quantity
        except ValueError:
            print("Invalid quantity format. Please enter a valid quantity.")

# Main while loop
while True:
    price = get_price()
    quantity = get_quantity()
    
    # Compute total
    total = price * quantity
    
    # Display totals
    print("Price:", "${:.2f}".format(price))
    print("Quantity:", quantity)
    print("Total:", "${:.2f}".format(total))
    
    # Prompt user for another line item
    choice = input("Do you want to enter another line item? (y/n): ")
    if choice.lower() != 'y':
        break

