

class ScoreBoard:
    def __init__(self):
        self.p1score = 0
        self.p2score = 0

    def score(self, player: int) -> None:
        """
        Increases player score by 1

        :param player: (int) 1 or 2
        :return: None
        """
        if player == 1:
            self.p1score += 1
        elif player == 2:
            self.p2score += 1

    def winning(self) -> str:
        """
        Return the winner of the round or False in case of draw

        :return: string or False
        """
        if self.p1score == self.p2score:
            return False
        return "Player 1" if self.p1score > self.p2score else "Player 2"

    def __str__(self):
        return f"""
        Tic-Tac-Toe Score:
    Player 1          Player 2
       {self.p1score}                 {self.p2score}"""


if __name__ == '__main__':
    s = ScoreBoard()
    print(s)
