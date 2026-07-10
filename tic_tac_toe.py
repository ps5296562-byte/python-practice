print("Tic Tac Toe")
player1=input("Player1 (X),enter position(1-9)")
player2=input("Player2 (O),enter position(1-9)")
print("Player1 chose:",player1)
print("Player2 chose:",player2)
if player1 == player2:
    print("Invalid! Both player chose same position. ")
else:
    print("Game Started!")