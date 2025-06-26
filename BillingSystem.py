print("\n      Welcome to MonyHotel\n")

items = []
qty = []
total = []
total_bill = 0

while True:
    print("========== MENU CARD ==========")
    print("1. South Indian")
    print("2. Gujarati")
    menu = int(input("Enter your menu: "))

    if menu < 1 or menu > 2:
        break

    if menu == 1:
        print("===============================")
        print("1. Idli        - ₹30")
        print("2. Dosa        - ₹50")
        print("3. Uttpam      - ₹100")
        print("4. MenduVada   - ₹150")
        print("5. Cold Drink  - ₹40")
        print("6. Exit")
        choice = int(input("Enter your choice (1 to 6): "))

        if choice < 1 or choice > 5:
            print("Invalid choice! Exiting...\n")
            continue

        if choice == 1:
            food_name = "Idli"
            price = 30
        elif choice == 2:
            food_name = "Dosa"
            price = 50
        elif choice == 3:
            food_name = "Uttpam"
            price = 100
        elif choice == 4:
            food_name = "MenduVada"
            price = 150
        elif choice == 5:
            food_name = "Cold Drink"
            price = 40

    elif menu == 2:
        print("===============================")
        print("1. Sev-tameta  - ₹50")
        print("2. Undhiyu     - ₹100")
        print("3. Daal-bhat   - ₹50")
        print("4. Rotli       - ₹30")
        print("5. Cold Drink  - ₹40")
        print("6. Exit")
        choice = int(input("Enter your choice (1 to 6): "))

        if choice < 1 or choice > 5:
            print("Invalid choice! Exiting...\n")
            continue

        if choice == 1:
            food_name = "Sev-tameta"
            price = 50
        elif choice == 2:
            food_name = "Undhiyu"
            price = 100
        elif choice == 3:
            food_name = "Daal-bhat"
            price = 50
        elif choice == 4:
            food_name = "Rotli"
            price = 30
        elif choice == 5:
            food_name = "Cold Drink"
            price = 40

    print("================================")
    quantity = int(input("Enter quantity: "))
    print("================================")
    print(f"You ordered {quantity} {food_name}(s)")

    items.append(food_name)
    qty.append(quantity)
    total_price = price * quantity
    total.append(total_price)
    total_bill += total_price

    print("================================")
    cont = input("Do you want to order more? (y/n): ")
    if cont.lower() != 'y':
        break

# Final Bill
print("\n\n=========== MonyHotel ============\n")
print("Items\t\tQty\t\tTotal")
print("---------------------------------------------")

for i in range(len(items)):
    print(f"{items[i]}\t\t{qty[i]}\t\t{total[i]}")

print("---------------------------------------------")
discount = total_bill * 0.10
net_total = total_bill - discount
cgst = net_total * 0.09
sgst = net_total * 0.09
grand_total = net_total + cgst + sgst

print(f"Sub Total\t\t\t₹{total_bill:.2f}")
print(f"Discount @10%\t\t\t₹{discount:.2f}")
print("---------------------------------------------")
print(f"Net Total\t\t\t₹{net_total:.2f}")
print(f"CGST @9%\t\t\t₹{cgst:.2f}")
print(f"SGST @9%\t\t\t₹{sgst:.2f}")
print("---------------------------------------------")
print(f"Grand Total\t\t\t₹{grand_total:.2f}\n")
