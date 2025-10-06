def ai_move(board: list[int]):
# GABBY's CODE STARTS HERE:
# Loop through each cell within the board
    for cell in board:
        if abs(cell) != 10: # This indicates that the space is not already taken
            return cell # This returns AI chosen cell # as it's "move"
    return None # If all cells are taken which shouldn't occur in the middle of the game, returns to None to indicate there are no remaining moves
    """
        Simple AI that selects the first available cell.
        Remember board is a list that starts with items 1 - 9
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        after two moves with X choosing 1 and O choosing 5 the board looks like:
        [10, 2, 3, 4, -10, 6, 7, 8, 9]
        
        so in this case your function should return 2
    """
    # TODO: Loop through board
    # TODO: Find the first index where abs(cell) != 10
    # TODO: Return that index as the AI's move
    pass