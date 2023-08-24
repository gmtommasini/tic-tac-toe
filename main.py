import os
from board import Board, SYMBOLS
from scoreboard import ScoreBoard
from ia import CPU


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_screen(board: Board, score: ScoreBoard):
    clear()
    print(score)
    board.print_board()


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


def run(one_player: bool = True, p1_name='Player 1', p2_name='Player 2', level=1 ):
    b = Board()
    if one_player:
        cpu = CPU(b, level)
    score = ScoreBoard(p1_name, p2_name)
    while True:
        print_screen(b, score)
        (symbol, player) = (SYMBOLS[0], p1_name) if b.p1_plays else (SYMBOLS[1], p2_name)
        if b.p1_plays or not one_player:
            user_input = get_user_input(f"{player}: choose the board position you want to play\n(a number between 1 and 9. 0 to finish the game): ")
            if user_input == 0:
                break
        elif one_player:
            user_input = cpu.make_a_play()
        if winner := b.make_play(symbol, user_input):
            score.score(winner)
            print_screen(b, score)
            if winner == -1:
                print("Round DRAW!")
            else:
                print(f"{p1_name if winner == 1 else p2_name} wins the round.")

            _ = input("Press any ENTER to continue...")
            b.clean_board()
            if one_player:
                cpu.reset()

    # ENDING game
    if winner := score.winning():
        print("The winner is", winner)
    else:
        print("It is a Draw!!")


def get_player_name(player: int):
    p = f'Player {player}'
    p_name = input(f"{p}, enter your name: ")
    return p_name if len(p_name) > 0 else p


def select_difficulty():
    while True:
        try:
            diff = int(input("Select level (0-Practice to 10-Impossible):"))
            if diff in range(0, 11):
                return diff
        except Exception:
            pass


def main():
    players = get_user_input(f"Please, chose the number of players ( 1 or 2 )\nAny other number to quit: ")
    if players == 1:
        p1_name = get_player_name(1)
        difficulty = select_difficulty()
        run(one_player=True, p1_name=p1_name, p2_name='CPU', level=difficulty)
    elif players == 2:
        p1_name = get_player_name(1)
        p2_name = get_player_name(2)
        run(one_player=False, p1_name=p1_name, p2_name=p2_name)


if __name__ == '__main__':
    main()
