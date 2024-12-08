# Write your solution here
def who_won(game_board: list[list[int]]) -> int:
    n_player1: int = sum(row.count(1) for row in game_board)
    n_player2: int = sum(row.count(2) for row in game_board)
    if n_player1 > n_player2:
        who_won_ = 1
    elif n_player2 > n_player1:
        who_won_ = 2
    else:
        who_won_ = 0
    return who_won_


if __name__ == "__main__":
    """
    In a game of Go two players take turns to place black and white stones on a game board. 
    The winner is the player who manages to encircle a bigger area on the board with 
    their own game pieces.


    Please write a function named who_won(game_board: list), 
    which takes a two-dimensional array as its argument. 
    The array consists of integer values, which represent the following situations:

    0: empty square
    1: player 1 game piece
    2: player 2 game piece
    The scoring rules of Go can be quite complex, but in this exercise 
    it is enough to compare the number of pieces each player has on the game board. 
    Also, the size of the game board is not limited.

    The function should return the value 1 if player 1 won, and the value 2 if player 2 won. 
    If both players have the same number of pieces on the board, the function 
    should return the value 0.
    """
    print(who_won([[1, 2, 2, 2], [0, 0, 0, 1], [0, 0, 2, 1]]))
