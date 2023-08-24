from board import Board, SYMBOLS
import random

CORNERS = [1, 3, 7, 9]
SIDES = [2, 4, 6, 8]


def is_empty(var):
    try:
        if _ := float(var) / 1:
            return True
    except Exception:
        return False


class CPU:
    def __init__(self, board: Board, level: int = 9):
        self.b = board
        self.number_of_plays = 0
        self.level = level/10

    def reset(self):
        self.number_of_plays = 0

    def make_a_play(self) -> int:
        """
        This function will make a move based on the board's previous plays
        :return: The position to play
        """
        self.number_of_plays += 1

        # Sometimes the AI will make a random play (to increase player's chances)
        if random.random() > self.level:
            return random.choice(self.b.available_moves())

        # first move
        if self.number_of_plays == 1:
            if 5 in self.b.available_moves():
                return 5
            else:
                # Any of the corners will do.
                return random.choice(CORNERS)

        # nth move (if p1 has 2 places in same row/column)
        if my_win_cond := self.check_win_condition(SYMBOLS[1]):
            return my_win_cond
        if human_win_condition := self.check_win_condition(SYMBOLS[0]):
            return human_win_condition

        if self.number_of_plays == 2:
            # 2nd move if p1 has 2 corners - AI must play a SIDE)
            if sorted(self.b.p1_moves) in [[1, 9], [3, 7]]:
                return random.choice(SIDES)

        # second move (if IA started or person played weirdly)
            p1_move = self.b.p1_moves[-1]
            # AI started middle and P1 played one side
            # P1 is DOOMED!!!
            if not self.b.p1_starts and p1_move in SIDES:
                # AI have to chose an opposite corner to p1 move
                if p1_move == 2:
                    return random.choice([7, 9])
                elif p1_move == 4:
                    return random.choice([3, 9])
                elif p1_move == 6:
                    return random.choice([1, 7])
                elif p1_move == 8:
                    return random.choice([1, 3])

            # P1 didn't play wrong
            if p1_move == 1:
                return random.choice([3, 7])
            elif p1_move == 3:
                return random.choice([1, 9])
            elif p1_move == 7:
                return random.choice([1, 9])
            elif p1_move == 9:
                return random.choice([3, 7])
            else:
                return random.choice(CORNERS)

        # Plays a random side
        random.shuffle(SIDES)
        for pos in SIDES:
            if pos in self.b.available_moves():
                return pos

        if len(self.b.available_moves()) == 1:
            return self.b.available_moves()[0]

        # TODO: evaluate this part
        # Plays a random corner
        random.shuffle(CORNERS)
        for pos in CORNERS:
            if pos in self.b.available_moves():
                return pos


    def check_win_condition(self, player) -> int:
        """
        Checks if the player given can win with next move
        :param player: o or x
        :return: winnable position or 0
        """
        p = self.b.positions
        for i in [0, 1, 2]:
            # checking lines:
            if p[i][0] == p[i][1] == player and is_empty(p[i][2]):
                return p[i][2]
            if p[i][2] == p[i][1] == player and is_empty(p[i][0]):
                return p[i][0]
            if p[i][0] == p[i][2] == player and is_empty(p[i][1]):
                return p[i][1]

            # checking columns:
            if p[0][i] == p[1][i] == player and is_empty(p[2][i]):
                return p[2][i]
            if p[2][i] == p[1][i] == player and is_empty(p[0][i]):
                return p[0][i]
            if p[2][i] == p[0][i] == player and is_empty(p[1][i]):
                return p[1][i]

        # checking diagonals
        if p[0][0] == p[1][1] == player and is_empty(p[2][2]):
            return p[2][2]
        if p[2][2] == p[1][1] == player and is_empty(p[0][0]):
            return p[0][0]
        if p[2][2] == p[0][0] == player and is_empty(p[0][0]):
            return p[1][1]

        if p[0][2] == p[1][1] == player and is_empty(p[2][0]):
            return p[2][0]
        if p[2][0] == p[1][1] == player and is_empty(p[0][2]):
            return p[0][2]
        if p[2][0] == p[0][2] == player and is_empty(p[0][2]):
            return p[1][1]


if __name__ == '__main__':
    b = Board()
    c = CPU(b)
    b.print_board()
    c.make_a_play()
