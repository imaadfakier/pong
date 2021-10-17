from turtle import Turtle

# constants
# ...


class Ball(Turtle):
    """
    ...
    """

    # class attributes
    # ...

    def __init__(self, color):
        super().__init__()
        self.x_add_on = 10
        self.y_add_on = 10
        self.shape(name='circle')
        self.color(color)
        self.speed(speed='slowest')
        self.penup()
        # self.setheading(to_angle=45)
        self.move_speed = 0.1

    def keep_ball_moving(self):
        # self.forward(20)
        # self.goto(self.xcor(), self.ycor())
        self.goto(self.xcor() + self.x_add_on, self.ycor() + self.y_add_on)
        # self.goto(self.xcor() + 1, self.ycor() + 1)

    def bounce_y(self):
        self.y_add_on *= -1  # <--- learnt something new

    def bounce_x(self):
        self.x_add_on *= -1
        self.move_speed *= 0.9  # <--- learnt something new
        # self.move_speed -= 0.01

    def reset_position(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.1
        self.bounce_x()
