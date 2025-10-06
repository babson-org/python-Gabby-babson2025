    
def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
    prompt = "Select an empty cell (1-9): "
    while True:
        try:
            move = int(input(prompt)) # Asks the player (me) for their move 1-9
            if move < 1 or move > 9: # Verifies move is within parameters 1-9
                prompt = "Out of range, select again (1-9): "
                continue 
            index = move - 1 # This should translate the cell # to index, 1-9 --> 0-8
            if abs(board[index]) == 10: # Checks if cell is already occupied
                prompt = "Cell is already taken, choose again please: "
                continue 
            board[index] = score["player"] # Assigns valid player score to board position
            break
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "
    return board           
pass
