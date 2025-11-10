from typing import List, Tuple
from utils import in_bounds

def get_adjacent_cells(r: int, c: int, rows: int, cols: int) -> List[Tuple[int,int]]:
    neighbors = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc, rows, cols):
                neighbors.append((nr, nc))
    return neighbors