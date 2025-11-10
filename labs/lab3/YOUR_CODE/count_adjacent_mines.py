from typing import List
from get_adjacent_cells import get_adjacent_cells

MINE_VAL = -1

def count_adjacent_mines(base_board: List[List[int]]) -> None:
    """
    Mutates base_board: for each non-mine cell sets the count of adjacent mines (0..8).
    Mines (MINE_VAL) are left unchanged.
    """
    rows = len(base_board)
    cols = len(base_board[0]) if rows > 0 else 0
    for r in range(rows):
        for c in range(cols):
            if base_board[r][c] == MINE_VAL:
                continue
            count = 0
            for (nr, nc) in get_adjacent_cells(r, c, rows, cols):
                if base_board[nr][nc] == MINE_VAL:
                    count += 1
            base_board[r][c] = count