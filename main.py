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


def run(one_player: bool = True, p1_name='Player 1', p2_name='Player 2'):
    if one_player:
        cpu = CPU(b)
    while True:
        print_screen()
        (symbol, player) = ('x', p1_name) if b.p1_plays else ('o', p2_name)
        if b.p1_plays or not one_player:
            user_input = get_user_input(f"{player}: choose the board position you want to play\n(a number between 1 and 9. 0 to end round): ")
            if user_input == 0:
                break
        elif one_player:
            user_input = cpu.make_a_play()
        if winner := b.make_play(symbol, user_input):
            score.score(winner)
            print_screen()
            if winner == 0:
                print("DRAW!")
            else:
                print(f"{p1_name if winner == 1 else p2_name} wins the round.")

            if input("Keep playing? (y/n)\n Enter to continue") != 'n':
                b.clean_board()
                if one_player:
                    cpu.reset()
            else:
                break

    # ENDING game
    if winner := score.winning():
        print("The winner is", winner)
    else:
        print("It is a Draw!!")


def main():
    players = get_user_input(f"Please, chose the number of players ( 1 or 2 )\nAny other key to quit: ")
    p1_name = input("Player 1, enter your name: ")
    p1_name = p1_name if len(p1_name)>0 else 'Player 1'
    if players == 1:
        run(one_player=True, p1_name=p1_name, p2_name='CPU')
    elif players == 2:
        p2_name = input("Player 2, enter your name: ")
        p2_name = p2_name if len(p2_name) > 0 else 'Player 2'
        run(one_player=False, p1_name=p1_name, p2_name=p2_name)


if __name__ == '__main__':
    main()
