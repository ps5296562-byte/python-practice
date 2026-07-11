import random
length = int(input("Enter the length of password:"))
password = ""
for i in range(length):
    digit = random.randint(0,9)
    password = password + str(digit)
print("Your password is:",password)