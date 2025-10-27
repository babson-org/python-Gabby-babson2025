MINE_VAL = -1

def is_mine_at(base_board, r: int, c: int) -> bool:
    return base_board[r][c] == MINE_VAL