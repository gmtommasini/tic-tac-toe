
def format_name(name):
    return name.upper()[0:10]


class ScoreBoard:
    def __init__(self, p1_name, p2_name):
        self.p1_name = format_name(p1_name)
        self.p2_name = format_name(p2_name)
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
        return self.p1_name if self.p1score > self.p2score else self.p2_name

    def __str__(self):
        return f"""
        Tic-Tac-Toe Score:
   {self.p1_name.center(10)}        {self.p2_name.center(10)}
       {self.p1score}                 {self.p2score}"""


if __name__ == '__main__':
    s = ScoreBoard('p1', "some very long name")
    print(s)
