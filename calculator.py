num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operator = input("Enter +,-,*,/:")
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
     if num2 != 0:
         print(num1/num2)
     else:
         print("Cannot divide by 0")
else:
     print("Invalid Operator")
