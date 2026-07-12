inventory = {}

while True:
    print("\nInventory Management")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Update Stock")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        inventory[product] = quantity
        print("Product added.")

    elif choice == "2":
        if inventory:
            for product, quantity in inventory.items():
                print(product, ":", quantity)
        else:
            print("Inventory is empty.")

    elif choice == "3":
        product = input("Enter product name: ")

        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity
            print("Stock updated.")
        else:
            print("Product not found.")

    elif choice == "4":
        product = input("Enter product name: ")

        if product in inventory:
            del inventory[product]
            print("Product deleted.")
        else:
            print("Product not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")