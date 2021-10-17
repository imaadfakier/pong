from turtle import Turtle

# constants
# ...


class Paddle(Turtle):
    """
    ...
    """

    # class attributes
    # ...

    def __init__(self, shape, color, turtle_size, pos):
        # self.shape(name=shape)  # if shape wasn't attribute, would be okay
        # super().__init__(shape=shape)  # <--- learnt something new
        super().__init__(shape)
        self.color(color)
        self.stretch_width, self.stretch_length = turtle_size
        self.shapesize(stretch_wid=self.stretch_width, stretch_len=self.stretch_length)
        self.penup()
        self.x, self.y = pos
        self.setpos(x=self.x, y=self.y)

    def move_paddle_up(self):
        if self.y >= 240:
            return
        self.y = self.ycor() + 20
        self.goto(x=self.x, y=self.y)
        # print(self.x, self.y)

    def move_paddle_down(self):
        if self.y <= -220:
            return
        self.y = self.ycor() - 20
        self.goto(x=self.x, y=self.y)
        # print(self.x, self.y)
