def calc_score(board: list[int]):
    """
        Determines if there's a winner on the board.
        Returns 30 if X wins, -30 if O wins, 0 otherwise.
         
        there are 8 ways to win: 3 rows, 3 columns, 2 diagnols
        if the cells in a row, column or diagnol add up to 30 return 30
        if they add upto -30 return -30
        else return 0
    """
     
    def line_sum(a, b, c):
        # Function will sum three cells to check for a win
        total = board[a] + board[b] + board[c]
        if total == 30: # Means X wins
            return 30
        elif total == -30: # If O wins
            return -30
        else:
            return 0 # There is no winner in this line
    # Checks all three ROWS
    for row in range(3):
        result = line_sum(row * 3, row * 3 + 1, row * 3 + 2)
        if result != 0:
            return result # Returns immediately if it finds a winner
    # Checks all three COLUMNS
    for col in range(3):
        result = line_sum(col, col + 3, col + 6) # Gives indices of 3 cells in column b/c board is a flat list
        if result != 0:
            return result
    # Checks the two DIAGONALS
    result = line_sum(0,4,8)
    if result != 0:
        return result
    result = line_sum(2,4,6)
    if result != 0:
        return result
    return 0 # If there isn't a winner found
    '''
            line_sum takes 3 numbers and if the sum is either 30
            or -30 returns that sum otherwise do not return
        '''         
         
        # TODO: Sum the values at board[a], board[b], board[c] 
        # TODO: Return 30 if X wins, -30 if O wins otherwise do not return
pass
    # TODO: For each of the 8 ways to win
    # TODO: Check the cells in each row, column, or diagonal using line_sum
    # TODO: Return 0 if line_sum() didn't return 30 or -30
pass

