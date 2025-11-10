from initialize_board import initialize_board
from place_random_mines import place_random_mines
from count_adjacent_mines import count_adjacent_mines
from print_board import print_board_with_indices
from get_validated_input import get_board_size, get_mine_count, get_move
from update_board import reveal_cell
from game_won import game_won
from globals import HIDDEN, MINE_SYMBOL, MAX_ROWS, MAX_COLS
import sys

def get_board_size():
    while True:
        try:
            rows = int(input(f"Enter number of rows (1-{MAX_ROWS}): "))
            cols = int(input(f"Enter number of cols (1-{MAX_COLS}): "))
            if 1 <= rows <= MAX_ROWS and 1 <= cols <= MAX_COLS:
                return rows, cols
            else:
                print(f"Rows and columns need to be between 1 and {MAX_ROWS}")
        except ValueError:
            print("Invalid, enter an integer")
  
def get_mine_count(max_mines):
    while True:
        try:
            mines = int(input(f"Enter number of mines (1-{max_mines}): "))
            if 1 <= mines <= max_mines:
                return mines
            else: 
                print(f"Mines must be between 1 and {max-mines}")
        except ValueError:
            print("Invalid. Enter an integer")

def get_move(rows, cols):
    while True:
        try:
            r = int(input(f"Enter row (0-{rows-1}): "))
            c = int(input(f"Enter col (0-{cols-1}): "))
            if 0 <= r < rows and 0 <= c < cols:
                return r, c
            else:
                print(f"Coordinates must be within board bounds.")
        except ValueError:
            print("Invalid input. Enter integers.")

def main():
    print("=== Minesweeper ===")
    rows, cols = get_board_size()
    max_mines = rows * cols - 1
    mine_count = get_mine_count(max_mines)

    base_board, display_board = initialize_board(rows, cols)
    place_random_mines(base_board, mine_count)
    count_adjacent_mines(base_board)
    while True:
        print_board_with_indices(display_board)
        r, c = get_move(rows, cols)
        result = reveal_cell(base_board, display_board, r, c)
        if result == 'mine':
            # reveal all mines
            for rr in range(rows):
                for cc in range(cols):
                    if base_board[rr][cc] == -1:
                        display_board[rr][cc] = MINE_SYMBOL
            print_board_with_indices(display_board)
            print("You hit a mine. Game Over.")
            return
        
        if game_won(base_board, display_board):
            print_board_with_indices(display_board)
            print("Congratulations, you win!")
            return
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye.")
        sys.exit(0)