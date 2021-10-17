# from game_screen import GameScreen
from paddle import Paddle
from turtle import Screen
import time
from ball import Ball
from scoreboard import Scoreboard

# screen = GameScreen(text='The Pong Game', background_color='black', setup=(800, 600))
# screen.listen_for_keys()
# Screen().listen()
screen = Screen()
screen.title(titlestring='The Pong Game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(n=0)

# default turtle size = 20 x 20
# but desired turtle size is 100 x 20
# therefore stretch_wid argument must
# be 5 with stretch_len argument staying
# the same when calling/invoking turtle_size
# method
right_paddle = Paddle(shape='square', color='white', turtle_size=(5, 1), pos=(350, 0))
left_paddle = Paddle(shape='square', color='white', turtle_size=(5, 1), pos=(-350, 0))
ball = Ball(color='white')
scoreboard = Scoreboard()


# def up_key_pressed():
#     right_paddle.move_paddle_up()


screen.onkey(fun=right_paddle.move_paddle_up, key='Up')


# def down_key_pressed():
#     right_paddle.move_paddle_down()


screen.onkey(fun=right_paddle.move_paddle_down, key='Down')


# def w_key_pressed():
#     left_paddle.move_paddle_up()


screen.onkey(fun=left_paddle.move_paddle_up, key='w')


# def s_key_pressed():
#     left_paddle.move_paddle_down()


screen.onkey(fun=left_paddle.move_paddle_down, key='s')

game_is_over = False

while not game_is_over:
    # screen.update_screen()
    screen.update()
    # time.sleep(0.1)
    time.sleep(ball.move_speed)
    # Screen().exitonclick()

    # detect wall collision  # <--- learnt something new
    # if ball.ycor() >= (screen.height / 2) - 15:
    # if ball.ycor() > (screen.height / 2) - 20:
    #     # ball.y_offset = -10
    #     ball.y_offset *= -1
    # # elif ball.ycor() <= -(screen.height / 2) + 15:
    # if ball.ycor() < -(screen.height / 2) - 20:
    #     ball.x_offset = -10
    #     # ball.y_offset = 10
    #     ball.y_offset *= -1
    if (ball.ycor() > (screen.window_height() / 2) - 20) or (ball.ycor() < -(screen.window_height() / 2) + 20):
        ball.bounce_y()

    # detect paddle(s) collision; went from 340 -> 320  # <--- learnt something new
    if ((ball.distance(right_paddle) < 50) and (ball.xcor() > 320)) \
            or ((ball.distance(left_paddle) < 50) and (ball.xcor() < -320)):
        # print('Made contact')
        ball.bounce_x()

    # detect paddle(s) misses  # <--- learnt something new
    # elif (ball.xcor() > 400) or (ball.xcor() < -400):
    #     ball.reset_position()
    if ball.xcor() > 400:
        scoreboard.increase_left_paddle_score()
        ball.reset_position()
    # elif ball.xcor() < -400:
    #     ball.reset_position()
    if ball.xcor() < -400:
        scoreboard.increase_right_paddle_score()
        ball.reset_position()

    ball.keep_ball_moving()

# screen.update_screen()
# Screen().exitonclick()
