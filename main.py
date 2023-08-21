import os
from board import Board


b = Board()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 9:
                return value
            else:
                print("Invalid choice. Please chose an available position.")
        except ValueError:
            print("Invalid choice. Please chose an available position.")


if __name__ == '__main__':
    keep_playing = True
    while keep_playing:
        while b.not_finished:
            clear()
            b.print_board()
            (symbol, player) = ('x', 'Player 1') if b.p1_plays else ('o', 'Player 2')
            user_input = get_user_input(f"{player}: choose the board position you want to play (a number between 1 and 9): ")
            b.make_a_play(symbol, user_input)

        keep_playing = True if input("Keep playing? (y/n)") == 'y' else False
