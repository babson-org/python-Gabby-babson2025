from typing import List

def print_board_with_indices(board: List[List[str]]) -> None:
# If the board is empty, just prints message and stop
    if not board:
        print("(empty board)")
        return
# Gets how many rows and columns are in the board
    rows = len(board)
    cols = len(board[0])
# Create a header line showing column numbers at the top
# Ex.) "0  1  2  3  4"
# PRINTS THE COLUMN INDICES
    header = "    " + " ".join(f"{c:2}" for c in range(cols))
    print(header)
# Print a separator line under the header for clarity
    print("   " + "-" * (3 * cols))
# Go through each row and print the row number + the cell content
    for r in range(rows):
    # Format each cell so everything lines up in columns
        row_str = " ".join(f"{board[r][c]:>2}" for c in range(cols))
        # Print the row index and the row contents
        print(f"{r:2} | {row_str}")
        
    print()