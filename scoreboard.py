from turtle import Turtle

# constants
# ...


class Scoreboard(Turtle):
    """
    ...
    """

    # class attributes
    # ...

    def __init__(self):
        super().__init__()
        self.right_paddle_score = 0
        self.left_paddle_score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.update()

    def update(self):
        self.clear()
        # self.goto(x=-100, y=200)
        self.goto(x=-100, y=180)
        self.write(self.left_paddle_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(x=100, y=180)
        self.write(self.right_paddle_score, align='center', font=('Courier', 80, 'normal'))

    def increase_right_paddle_score(self):
        self.right_paddle_score += 1
        self.update()

    def increase_left_paddle_score(self):
        self.left_paddle_score += 1
        self.update()
