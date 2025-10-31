from initialize_board import initialize_board
from place_random_mines import place_random_mines
from count_adjacent_mines import count_adjacent_mines
from print_board import print_board_with_indices
from get_validated_input import get_board_size, get_mine_count, get_move
from update_board import reveal_cell
from game_won import game_won
from globals import HIDDEN, MINE_SYMBOL
import sys

def main():
    print("=== Minesweeper ===")
    rows, cols = get_board_size()
    max_mines = rows * cols - 1
    mine_count = get_mine_count(max_mines)

    base_board, display_board = initialize_board(rows, cols)
    place_random_mines(base_board, mine_count)
    count_adjacent_mines(base_board)

    # Game loop
    while True:
        print_board_with_indices(display_board)
        r, c = get_move(rows, cols)
        result = reveal_cell(base_board, display_board, r, c)
        if result == 'mine':
            # reveal all mines for end-of-game clarity
            for rr in range(rows):
                for cc in range(cols):
                    if base_board[rr][cc] == -1:
                        display_board[rr][cc] = MINE_SYMBOL
            print_board_with_indices(display_board)
            print("BOOM! You hit a mine. Game Over.")
            return

        if game_won(base_board, display_board):
            print_board_with_indices(display_board)
            print("Congratulations — you revealed all safe squares! You win!")
            return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye.")
        sys.exit(0)