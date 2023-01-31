from turtle import Turtle

ALIGN = "center"
FONT = ('courier', 18, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # opens the data file to get stored high score
        with open('HighScores.data', mode="r") as high_scores_data:
            self.high_score = int(high_scores_data.read())
        self.hideturtle()
        self.color("green")
        self.penup()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        """ write the score on screen """
        self.clear()
        self.write(f"Score: {self.score}\t High Score: {self.high_score} ", align=ALIGN, font=FONT)

    def game_over(self):
        """ write the game over statement """
        self.home()
        self.color("red")
        self.write("Game Over", align=ALIGN, font=FONT)

    def update_score(self):
        """ update score and the high score if changed """
        self.score += 1
        self.update_high_score()
        self.write_score()

    def update_high_score(self):
        """set high score"""
        if self.score > self.high_score:
            self.high_score = self.score
            # store the new high score in the HighScores.data file
            with open('HighScores.data', mode="w") as high_score_handler:
                high_score_handler.write(f"{self.high_score}")
