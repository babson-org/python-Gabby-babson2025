from typing import Tuple

def in_bounds(r: int, c: int, rows: int, cols: int) -> bool: 
# Make sure both row and column are within the allowed range
    return 0 <= r < rows and 0 <= c < cols

def coord_to_str(r: int, c: int) -> str:
# Create a formatted string showing the row and column
    return f"({r},{c})"