import os
from board import Board
from scoreboard import ScoreBoard


b = Board()
score = ScoreBoard()


def print_screen():
    clear()
    print(score)
    b.print_board()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 9:
                return value
            else:
                print("Invalid choice. Please chose an available position.")
        except ValueError:
            print("Invalid choice. Please chose an available position.")


if __name__ == '__main__':
    keep_playing = True
    while keep_playing:
        while True:
            print_screen()
            (symbol, player) = ('x', 'Player 1') if b.p1_plays else ('o', 'Player 2')
            user_input = get_user_input(f"{player}: choose the board position you want to play\n(a number between 1 and 9. 0 to end round): ")
            if user_input == 0:
                break
            if winner := b.make_play(symbol, user_input):
                score.score(winner)
                print_screen()
                if winner == 0:
                    print("DRAW!")
                else:
                    print(f"Player {'1' if winner == 1 else '2'} wins the round.")
                break
        if keep_playing := True if input("Keep playing? (y/n)") == 'y' else False:
            b.clean_board()
        else:
            # ENDING game
            if winner := score.winning():
                print("The winner is", winner)
            else:
                print("It is a Draw!!")


