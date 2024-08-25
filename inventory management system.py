items = []
quantity = []
price = []

while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. View Inventory")
    print("4. Calculate Total Inventory Value")
    print("5. Search")
    print("6. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter item name: ")
        item_quantity = int(input("Enter item quantity"))
        item_price = float(input("Enter item price"))
        items.append(name)
        quantity.append(item_quantity)
        price.append(item_price)
        print(f"item '{name}' added to the inventory")

    elif choice == "2":
        name = input("Enter item name to delete: ")
        if name in items:
            index = items.index(name)
            items.pop(index)
            quantity.pop(index)
            price.pop(index)
            print(f"Item '{name}' deleted successfully!")

        else:
            print("Item not found!")
    
    elif choice == "3":
        if items:
            print("List of current inventory")
            for i in range(len(items)):
                print(f"{i+1}. {items[i]} - quantity: {quantity[i]}, Price: ${price[i]:.2f}")
        else:
            print("Inventory is empty")
    
    elif choice == "4":
        total_value = 0
        for i in range(len(items)):
            total_value += quantity[i] * price[i]
        print(f"Total inventory value: ${total_value:.2f}")
    
    elif choice == "5":
        search_name = input("Enter the item name you want to search for: ")
        if search_name in items:
            index = items.index(search_name)
            print(f"found {search_name} - Quantity: {quantity[index]}, Price: ${price[index]:.2f}")
        else:
            print("Item not found!")

    elif choice == "5":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 -5.")