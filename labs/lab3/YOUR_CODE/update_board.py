from typing import List, Tuple
from globals import BLANK_REVEALED, MINE_SYMBOL, HIDDEN
from get_adjacent_cells import get_adjacent_cells
from is_mine_at import is_mine_at

MINE_VAL = -1

def reveal_cell(base_board: List[List[int]], display_board: List[List[str]], r: int, c: int) -> str:
    rows = len(base_board)
    cols = len(base_board[0]) if rows > 0 else 0

    if is_mine_at(base_board, r, c):
        # reveal the mine
        display_board[r][c] = MINE_SYMBOL
        return 'mine'

    # If already revealed, do nothing
    if display_board[r][c] != HIDDEN:
        return 'ok'

    # If number > 0, reveal just this cell
    val = base_board[r][c]
    if val > 0:
        display_board[r][c] = str(val)
        return 'ok'

    # val == 0 -> flood-fill using stack
    stack: List[Tuple[int,int]] = [(r, c)]
    while stack:
        cr, cc = stack.pop()
        if display_board[cr][cc] != HIDDEN:
            continue
        cell_val = base_board[cr][cc]
        if cell_val == 0:
            display_board[cr][cc] = BLANK_REVEALED
            # push neighbors: if neighbor is zero or >0 we reveal accordingly.
            for (nr, nc) in get_adjacent_cells(cr, cc, rows, cols):
                if display_board[nr][nc] == HIDDEN:
                    # If neighbor is zero, we want to expand it. If >0, reveal the number.
                    if base_board[nr][nc] == 0:
                        stack.append((nr, nc))
                    else:
                        display_board[nr][nc] = str(base_board[nr][nc])
        else:
            # If we popped a number cell (shouldn't happen first pass), reveal it
            display_board[cr][cc] = str(cell_val)
    return 'ok'