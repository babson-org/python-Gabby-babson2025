from typing import List
from globals import HIDDEN, BLANK_REVEALED, MINE_SYMBOL

MINE_VAL = -1

def game_won(base_board: List[List[int]], display_board: List[List[str]]) -> bool:
    rows = len(base_board)
    cols = len(base_board[0]) if rows > 0 else 0
    for r in range(rows):
        for c in range(cols):
            if base_board[r][c] == MINE_VAL:
                # mine can be hidden or flagged later (we don't implement flagging here)
                continue
            # if a safe cell is still hidden, not won
            if display_board[r][c] == HIDDEN:
                return False
    return True