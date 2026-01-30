cart = []

def add_item():
    item = input("Enter item name: ")
    print = float(input("Enter price: "))
    cart.append((item, price))
    print("Item added to cart")

def view_cart():
    if not cart:
        print("Cart is empty")
        return
    
    print("\n----Your Cart----")
    total = 0
    for item,price in cart:
        print(f"{item}: {price}")
        total += price
    print("Total AMount: ",total)


def remove_item(): 
    item = input("Enter item name to remove: ")
    for i in cart:
        if i[0] == item:
            cart.remove(i)
            print("Item removed")
            return
    print("Item not found")

while True:
    print("\n---- Shopping Cart Menu ----")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        view_cart()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        print("Thank you for shopping")
    else:
        print("Invalid choice")





