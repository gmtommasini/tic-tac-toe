from enum import Enum
from color import yellow_b, gray_f


INITIAL_POSITIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class Player(Enum):
    x = 'X'
    o = 'O'


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
        self.positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.available_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.p1_starts: bool = True
        self.p1_plays: bool = True
        self.not_finished = True

    def clean_board(self):
        self.positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.available_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def print_position(self, pos):
        if pos in self.available_positions:
            return gray_f(pos)
        else:
            return pos

    def print_board(self):
        pp = self.print_position
        print(f"""
  {pp(self.positions[0][0])} │ {pp(self.positions[0][1])} │ {pp(self.positions[0][2])}  
 ═══╪═══╪═══
  {pp(self.positions[1][0])} │ {pp(self.positions[1][1])} │ {pp(self.positions[1][2])}  
 ═══╪═══╪═══
  {pp(self.positions[2][0])} │ {pp(self.positions[2][1])} │ {pp(self.positions[2][2])}
""")

    def make_a_play(self, player, position):
        if position in self.available_positions:
            p = POSITIONS[str(position)]
            self.positions[p[0]][p[1]] = player
            self.available_positions.remove(position)
            self.p1_plays = not self.p1_plays
        if self.check_win():
            self.not_finished = False

    def check_win(self):
        p = self.positions
        for i in [0,1,2]:
            # checking lines:
            if p[i][0] == p[i][1] == p[i][2]:
                print(f"WIN on line {i+1}")
                p[i][0] = p[i][1] = p[i][2] = yellow_b(p[i][0])
                return True
            # checking columns:
            if p[0][i] == p[1][i] == p[2][i]:
                print(f"WIN on column {i+1}")
                p[0][i] = p[1][i] = p[2][i] = yellow_b(p[2][i])
                return True

        # checking diagonals
        if p[0][0] == p[1][1] == p[2][2]:
            p[0][0] = p[1][1] = p[2][2] = yellow_b(p[2][2])
            print("WIN on primary diagonal")
            return True
        if p[0][2] == p[1][1] == p[2][0]:
            p[0][2] = p[1][1] = p[2][0] = yellow_b(p[2][0])
            print("WIN on secondary  diagonal")
            return True


if __name__ == '__main__':
    b = Board()
    b.make_a_play('x', 1)
    b.make_a_play('o', 2)
    b.make_a_play('x', 9)
    b.make_a_play('o', 4)
    b.make_a_play('x', 5)
    # b.make_a_play('o', 7)
    b.print_board()
