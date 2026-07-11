value = float(input("Enter the value:"))
print("1. Meters to Centimeters")
print("2. Centimeters to Meters")
print("3. Liters to Milliliters")
print("4. Milliliters to Liters")
print("5. Kilograms to Grams")
print("6. Grams to Kilograms")
choice = int(input("Enter your choice:"))
if choice == 1:
    print("Result:",value*100,"Centimeters")
elif choice == 2:
    print("Result:",value/100,"Meters")
elif choice == 3:
    print("Result :",value*1000,"Milliliters")
elif choice == 4:
    print("Result:",value/1000,"Liters")
elif choice == 5:
    print("Result:",value*1000,"Grams")
elif choice == 6:
    print("Result:",value/1000,"Kilograms")
else:
    print("Invalid Choice")