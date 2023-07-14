# Write your solution here
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for arr in game_board:
        for num in arr:
            if num == 1:
                player1 += 1
            elif num == 2:
                player2 += 1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0