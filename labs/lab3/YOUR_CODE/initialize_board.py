from typing import List, Tuple
from globals import HIDDEN

def initialize_board(rows: int, cols: int) -> Tuple[List[List[int]], List[List[str]]]:
# Base board (the "real" board with mines and numbers)...
# This will eventually hold numbers (1–8) or mines
# Start everything at 0 (meaning no mines yet)
    base_board = [[0 for _ in range(cols)] for _ in range(rows)]
    # Display board (what the player sees)
    display_board = [[HIDDEN for _ in range(cols)] for _ in range(rows)]
    # Return both boards together as a tuple (base_board, display_board)
    return base_board, display_board