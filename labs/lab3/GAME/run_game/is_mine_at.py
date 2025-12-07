MINE_VAL = -1

def is_mine_at(base_board, r: int, c: int) -> bool:
    rows = len(base_board)
    cols = len(base_board[0]) if rows > 0 else 0
    if 0 <= r < rows and 0 <= c < cols:
        return base_board[r][c] == MINE_VAL
    return False