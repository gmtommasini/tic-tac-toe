import os
from board import Board
from scoreboard import ScoreBoard
from ia import CPU


b = Board()
score = ScoreBoard()


def print_screen():
    # clear()
    print(score)
    b.print_board()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_input(prompt, max_choices=9):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= max_choices:
                return value
            else:
                print("Invalid choice. Please chose an valid option.")
        except ValueError:
            print("Invalid choice. Please chose an valid option.")


def run():
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



def run_cpu():
    cpu = CPU(b)
    keep_playing = True
    while keep_playing:
        while True:
            print_screen()
            (symbol, player) = ('x', 'Player 1') if b.p1_plays else ('o', '  CPU  ')
            if b.p1_plays:
                user_input = get_user_input(f"{player}: choose the board position you want to play\n(a number between 1 and 9. 0 to end round): ")
                if user_input == 0:
                    break
            else:
                user_input = cpu.make_a_play()
            if winner := b.make_play(symbol, user_input):
                score.score(winner)
                print_screen()
                if winner == -1:
                    print("DRAW!")
                else:
                    print(f"Player {'1' if winner == 1 else '2'} wins the round.")
                break
        if keep_playing := True if input("Keep playing? (y/n)\n Enter to continue") != 'n' else False:
            b.clean_board()
            cpu.reset()
        else:
            # ENDING game
            if winner := score.winning():
                print("The winner is", winner)
            else:
                print("It is a Draw!!")


if __name__ == '__main__':
    players = get_user_input(f"Please, chose the number of players ( 1 or 2 )\nAny other key to quit: ")
    if players == 1:
        run_cpu()
    elif players == 2:
        run()
