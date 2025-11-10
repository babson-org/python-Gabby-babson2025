import random
from typing import List, Tuple

MINE_VAL = -1

def place_random_mines(base_board: List[List[int]], mine_count: int, seed: int = None) -> None:
    rows = len(base_board)
    cols = len(base_board[0]) if rows > 0 else 0
    total = rows * cols
    if mine_count < 0 or mine_count > total:
        raise ValueError("Invalid mine_count")

    if seed is not None:
        random.seed(seed)

    all_positions = [(r, c) for r in range(rows) for c in range(cols)]
    chosen = random.sample(all_positions, mine_count)
    for (r, c) in chosen:
        base_board[r][c] = MINE_VAL