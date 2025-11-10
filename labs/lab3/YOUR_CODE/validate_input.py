from typing import Tuple
from globals import MAX_ROWS, MAX_COLS

def get_positive_int(prompt: str, min_val: int = 1, max_val: int = None) -> int:
    while True:
        try:
            s = input(prompt).strip()
            v = int(s)
            if v < min_val:
                print(f"Please enter an integer >= {min_val}.")
                continue
            if max_val is not None and v > max_val:
                print(f"Please enter an integer <= {max_val}.")
                continue
            return v
        except ValueError:
            print("Please enter a valid integer.")

def get_board_size() -> Tuple[int, int]:
    print("Enter board size.")
    rows = get_positive_int(f"Rows (1-{MAX_ROWS}): ", 1, MAX_ROWS)
    cols = get_positive_int(f"Columns (1-{MAX_COLS}): ", 1, MAX_COLS)
    return rows, cols

def get_mine_count(max_mines: int) -> int:
    prompt = f"Number of mines (1-{max_mines}): "
    return get_positive_int(prompt, 1, max_mines)

def get_move(rows: int, cols: int) -> Tuple[int,int]:
    """
    Prompt user for a move in the form 'r c' or 'r,c'. Validates bounds.
    """
    while True:
        s = input(f"Enter move as 'row col' (0-{rows-1} 0-{cols-1}): ").strip().replace(',', ' ')
        parts = s.split()
        if len(parts) != 2:
            print("Please enter two integers separated by space.")
            continue
        try:
            r = int(parts[0]); c = int(parts[1])
        except ValueError:
            print("Please enter valid integers.")
            continue
        if not (0 <= r < rows and 0 <= c < cols):
            print("Coordinates out of bounds.")
            continue
        return r, c