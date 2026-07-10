number = 7
guess = int(input("guess the number:"))
if guess == number:
    print("Correct")
elif guess < number:
    print("low")
else:
    print("high")