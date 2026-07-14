cart = {}

while True:
    print("\n===== Shopping Cart =====")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Calculate Total")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart[item] = price
        print(item, "added to cart.")

    elif choice == "2":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("\nItems in Cart:")
            for item, price in cart.items():
                print(item, "-", price)

    elif choice == "3":
        item = input("Enter item name to remove: ")
        if item in cart:
            del cart[item]
            print(item, "removed from cart.")
        else:
            print("Item not found.")

    elif choice == "4":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            total = sum(cart.values())
            print("Total Bill =", total)

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Try again.")