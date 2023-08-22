import copy
from enum import Enum
from color import yellow_b, gray_f


INITIAL_POSITIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


POSITIONS = {
    '1': (0, 0),
    '2': (0, 1),
    '3': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '7': (2, 0),
    '8': (2, 1),
    '9': (2, 2)
}


class Board:
    def __init__(self):
        self.positions = copy.deepcopy(INITIAL_POSITIONS)
        self.available_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.p1_starts: bool = True
        self.p1_plays: bool = True
        self.p1_moves: list = []
        self.p2_moves: list = []

    def clean_board(self):
        self.positions = copy.deepcopy(INITIAL_POSITIONS)
        self.available_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.p1_starts = not self.p1_starts  # switches starting player
        self.p1_plays = self.p1_starts
        self.p1_moves: list = []
        self.p2_moves: list = []

    def print_position(self, pos):
        if pos in self.available_positions:
            return gray_f(pos)
        else:
            return pos

    def print_board(self):
        print(self)

    def __str__(self):
        pp = self.print_position
        return f"""
            {pp(self.positions[0][0])} │ {pp(self.positions[0][1])} │ {pp(self.positions[0][2])}  
           ═══╪═══╪═══
            {pp(self.positions[1][0])} │ {pp(self.positions[1][1])} │ {pp(self.positions[1][2])}  
           ═══╪═══╪═══
            {pp(self.positions[2][0])} │ {pp(self.positions[2][1])} │ {pp(self.positions[2][2])}
        """

    def available_moves(self) -> list:
        return self.available_positions

    def make_play(self, player: str, position: int ):
        """
        Make a play for x or o. Return False in case of match not finished, or
        Return 0 for draw, or
        Returns the number of the winning player
        :param player: 'x' or 'o'
        :param position: 1-9
        :return: False, 0, 1, or 2
        """

        # Invalid play
        if position not in self.available_positions:
            return False

        p = POSITIONS[str(position)]
        self.positions[p[0]][p[1]] = player
        self.available_positions.remove(position)

        if self.check_win():
            # returning the winner of the round
            return 1 if self.p1_plays else 2

        # No more moves = draw
        if len(self.available_positions) == 0:
            print(len(self.available_positions))
            return 0

        # Save moves
        if player == 'x':
            self.p1_moves.append(position)
        elif player == 'o':
            self.p2_moves.append(position)

        # Alternating player
        self.p1_plays = not self.p1_plays  # alternate turns
        return False

    def check_win(self):
        p = self.positions
        for i in [0,1,2]:
            # checking lines:
            if p[i][0] == p[i][1] == p[i][2]:
                p[i][0] = p[i][1] = p[i][2] = yellow_b(p[i][0])
                return True
            # checking columns:
            if p[0][i] == p[1][i] == p[2][i]:
                p[0][i] = p[1][i] = p[2][i] = yellow_b(p[2][i])
                return True

        # checking diagonals
        if p[0][0] == p[1][1] == p[2][2]:
            p[0][0] = p[1][1] = p[2][2] = yellow_b(p[2][2])
            return True
        if p[0][2] == p[1][1] == p[2][0]:
            p[0][2] = p[1][1] = p[2][0] = yellow_b(p[2][0])
            return True


if __name__ == '__main__':
    b = Board()
    b.make_play('x', 1)
    b.make_play('o', 2)
    b.make_play('x', 9)
    b.make_play('o', 4)
    b.make_play('x', 5)
    # b.make_a_play('o', 7)
    b.print_board()
