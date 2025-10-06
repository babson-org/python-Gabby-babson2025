
from calc_score import calc_score


def game_over(board: list[int]):
    # First check if a player/AI has won
    score = calc_score(board)
    if score == 30 or score == -30:
        return True
    # Then checking if there aren't any moves yet (aka the cells are all occupied)
    for cell in board:
        if abs(cell) != 10: # If any of the cells aren't marked X or O, there is an open spot, therefore the game isn't over
            return False
    return True # If game is tied
    """
        After every move (see play_game) we check to see if the game 
        is over.  The game is over if calc_score() returns 30 or -30
        or if ther are no open moves left on the board
        Returns True if the game has a winner or no remaining moves, False otherwise.
    """

    # TODO: Check if all cells are filled (abs(cell) == 10)
    # TODO: Use calc_score to check if someone has won
    # TODO: Return True if game over, otherwise False
    pass
