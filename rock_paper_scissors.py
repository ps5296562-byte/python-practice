import random
game_options = {1:"Stone",2:"Paper",3:"Scissor"}
print("Welcome to the game Stone, Paper and Scissors")
computer_choose = random.randint(1,3)
player_choose = int(input("Enter 1 for stone, 2 for paper and 3 for scissor"))
if computer_choose == player_choose:
    print("Tie!")
elif computer_choose ==1 and player_choose ==2:
    print("You Win!")
elif computer_choose ==2 and player_choose ==3:
    print("You Win!")
elif computer_choose ==3 and player_choose ==1:
    print("You Win!")
else:
    print("Computer Win!")