# arkanoid v1.0 by gozdek
# 2020.08.22

import turtle
from turtle import *
import time
import random
import math
import winsound

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("arkanoid v1.0 by gozdek")
screen.tracer(0)


class Countdown_screen(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.color("white")
        self.hideturtle()

        self.goto(-50, 0)
        self.write("3", font=("ARIAL", 80, "bold"))
        time.sleep(1)
        self.clear()

        self.write("2", font=("ARIAL", 80, "bold"))
        time.sleep(1)
        self.clear()

        self.write("1", font=("ARIAL", 80, "bold"))
        time.sleep(1)
        self.clear()

        self.goto(-200, 0)
        self.write("START", font=("ARIAL", 80, "bold"))
        time.sleep(1)
        self.clear()

        del self


class Title_Screen(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.goto(-230, 150)
        self.color("white")
        self.write("ARKANOID", font=("ARIAL", 60, "bold"))
        self.goto(-150, -100)
        self.write("PADDLE LEFT - PRESS LEFT\nPADDLE RIGHT - PRESS RIGHT\nRESET GAME - PRESS ESC\nFIRE - PRESS UP\nNEXT LEVEL - PRESS DOWN", font=("ARIAL", 12, "bold"))
        self.hideturtle()

        time.sleep(5)

        self.clear()

        del self


class Game_Over_Screen(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.goto(-160, 0)
        self.color("white")
        self.write("GAME OVER", font=("ARIAL", 40, "bold"))
        self.hideturtle()
        winsound.PlaySound("gameover.wav", winsound.SND_ASYNC)
        time.sleep(2)
        self.clear()
        del self

        lives_b.reset()
        score_b.reset()
        disabled_bricks_counter.reset()

        Title_Screen()

        levels.show_level(0)


class Level_Screen(Turtle):
    def __init__(self, x):
        super().__init__()

        self.penup()
        self.goto(-120, 0)
        self.color("white")

        self.write("LEVEL " + str(x + 1), font=("ARIAL", 40, "bold"))
        self.hideturtle()
        time.sleep(2)
        self.clear()
        del self


class Disabled_bricks_counter:
    def __init__(self):
        self.d = 0

    def add(self):
        self.d += 1

    def reset(self):
        self.d = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setpos(random.randint(-380, 380), random.randint(-200, -180))
        self.showturtle()
        self.speed(0)
        self.ball_dx = 4 * int(random.choice(['-1', '1']))
        self.ball_dy = 4

    def ball_movement(self):
        self.setx(self.xcor() + self.ball_dx)
        self.sety(self.ycor() + self.ball_dy)

    def reset_position(self):
        self.setpos(random.randint(-380, 380), random.randint(-200, -180))
        self.ball_dx = 4 * int(random.choice(['-1', '1']))
        self.ball_dy = 4


Title_Screen()

disabled_bricks_counter = Disabled_bricks_counter()

ball = Ball()

class LivesBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.lives = 3
        self.penup()
        self.goto(-300, 270)
        self.color("white")
        self.write("LIVES " + str(self.lives), font=("ARIAL", 18, "bold"))
        self.hideturtle()

    def reset(self):
        self.lives = 3
        self.clear()
        self.write("LIVES " + str(self.lives), font=("ARIAL", 18, "bold"))

    def update(self, x):
        self.lives += x
        if self.lives >= 0:
            self.clear()
            self.write("LIVES " + str(self.lives), font=("ARIAL", 18, "bold"))

lives_b = LivesBoard()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.penup()
        self.goto(200, 270)
        self.color("white")
        self.write("SCORE " + str(self.score), font=("ARIAL", 18, "bold"))
        self.hideturtle()

    def update(self, x):
        self.score += x
        self.clear()
        self.write("SCORE " + str(self.score), font=("ARIAL", 18, "bold"))

    def reset(self):
        self.score = 0
        self.clear()
        self.write("SCORE " + str(self.score), font=("ARIAL", 18, "bold"))

score_b = ScoreBoard()


class LevelsBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.goto(-80, 270)
        self.color("white")
        self.hideturtle()

    def update(self, x):
        self.clear()
        self.write("LEVEL " + str(x + 1) + " OF " + str(len(levels.levels)), font=("ARIAL", 18, "bold"))


class Brick(Turtle):
    def __init__(self, sc, sr, _):
        super().__init__()

        self.colors = ("red", "blue", "green", "yellow", "brown", "gray", "pink", "violet", "orange")
        self.penup()
        self.goto(sc + _ * 50, sr)
        self.shape("square")
        self.color(random.choice(self.colors))
        self.shapesize(1, 2)
        self.activate()

    def activate(self):
        self.active = True

    def deactiate(self):
        self.active = False
        self.hideturtle()
        del self

levels_b = LevelsBoard()

class Levels:
    def __init__(self):

        self.bricks = []

        self.current_level = 0

        self.levels = []

        self.levels.append("111111111111111"
                           "111111111111111"
                           "111111111111111"
                           "111111111111111"
                           "111111111111111")

        self.levels.append("111111111111111"
                           "000000011000000"
                           "000000111100000"
                           "000001111110000"
                           "000010111101000"
                           "111111111111111")

        self.levels.append("111111111111111"
                           "101010101010101"
                           "101010101010101"
                           "010101010101010"
                           "111000010000111"
                           "110000111000011"
                           "100000000000001")

        self.levels.append("110010101110010"
                           "101010100100101"
                           "111010100100111"
                           "100011100100101"
                           "000000000000000"
                           "111111111111111")

        self.levels.append("110000000000000"
                           "111100000000000"
                           "111111000000000"
                           "111111110000000"
                           "111111111100000"
                           "111111111111000"
                           "111111111111110")

        self.levels.append("011000110100110"
                           "100101000101001"
                           "100101110101001"
                           "111100010101111"
                           "100100010101001"
                           "100101100101001"
                           "000000000000000"
                           "101010101010101"
                           "010101010101010")

        self.levels.append("000111000111000"
                           "001111101111100"
                           "011111111111110"
                           "011111111111110"
                           "011111111111110"
                           "001111111111100"
                           "000111111111000"
                           "100011111110001"
                           "110001111100011"
                           "111000111000111"
                           "111100010001111"
                           "111000000000111")


    def show_level(self, level_no):

        self.current_level = level_no

        if self.current_level == 0:
            Countdown_screen()
            score_b.reset()
            lives_b.reset()

        winsound.PlaySound("nextlevel.wav", winsound.SND_ASYNC)

        Level_Screen(self.current_level)

        print("levels b update")
        levels_b.update(self.current_level)
        ball.reset_position()

        disabled_bricks_counter.reset()

        start_row = 220
        start_col = -356
        i = 0

        bullet.bullet_reset_position()

        # deaktywuje pozostałe cegły
        for br in self.bricks:
            br.deactiate()

        # usuwa pozostale obiekty bricków
        for _ in self.bricks:
             del _

        # czyści listę odnośników do obiektów
        self.bricks = []

        for _ in range(len(self.levels[level_no])):
            i += 1
            if _ % 15 == 0:
                start_row -= 30
                i = 0
            if self.levels[level_no][_] == '1':
                brick = Brick(start_col, start_row, i)
                self.bricks.append(brick)


    def all_bricks_disabled(self):
        if disabled_bricks_counter.d == self.levels[self.current_level].count("1"):
             return True
        else:
            return False

    def next_level(self):
        # IF LAST LEVEL -> LEVEL NUMBER = 0
        if self.current_level == len(self.levels) - 1:
            lives_b.reset()
            score_b.reset()
            bullet.bullet_reset_position()
            self.current_level = 0
        else:
            # NEXT LEVEL
            self.current_level += 1

        self.show_level(self.current_level)


class Bullet(Turtle):
    def __init__(self):
        super().__init__()

        self.color("red")
        self.penup()
        self.goto(0, - 1000)
        self.shape("arrow")
        self.setheading(90)
        self.ready()
        self.bullet_step = 6

    def busy(self):
        self.in_motion = True

    def ready(self):
        self.in_motion = False

    def bullet_movement(self):
        self.sety(self.ycor() + self.bullet_step)

    def bullet_reset_position(self):
        self.ready()
        self.goto(0, - 1000)


bullet = Bullet()

levels = Levels()
levels.show_level(levels.current_level)

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")

    def show_border(self, color):
        self.pensize(5)
        self.color(color)
        self.penup()
        self.goto(-395, -280)
        self.pendown()
        self.goto(-395, 265)
        self.goto(385, 265)
        self.goto(385, -280)
        self.hideturtle()


border = Border()
border.show_border("red")


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("white")
        self.shape("square")
        self.penup()
        self.setpos(0, -230)
        self.showturtle()
        self.shapesize(1, 5)
        self.paddle_step = 10
        self.paddle_l_max = -331
        self.paddle_r_max = 325

    def go_left(self):
        screen.onkeypress(None, "Left")
        screen.onkeypress(None, "Right")
        x, y = self.pos()
        if x >= self.paddle_l_max:
            self.goto(x - self.paddle_step, y)
        screen.onkeypress(self.go_left, "Left")
        screen.onkeypress(self.go_right, "Right")

    def go_right(self):
        screen.onkeypress(None, "Left")
        screen.onkeypress(None, "Right")
        x, y = self.pos()
        if x <= self.paddle_r_max:
            self.goto(x + self.paddle_step, y)
        screen.onkeypress(self.go_left, "Left")
        screen.onkeypress(self.go_right, "Right")


paddle = Paddle()

def fire():
    if not bullet.in_motion:
        bullet.busy()
        bullet.showturtle()
        bullet.goto(paddle.pos())

screen.listen()

screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")
screen.onkey(fire, "Up")
screen.onkey(lambda:levels.show_level(0), "Escape")
screen.onkey(levels.next_level, "Down")

while True:
    screen.update()
    ball.ball_movement()
    if bullet.in_motion:
        bullet.bullet_movement()

    # COLLISION BALL <-> BORDER
    if ball.xcor() > 370:
        ball.setx(370)
        ball.ball_dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() < -380:
        ball.setx(-380)
        ball.ball_dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() > 250:
        ball.sety(250)
        ball.ball_dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # OUT OF BORDER - BALL
    if ball.ycor() < -300:
        ball.reset_position()
        lives_b.update(-1)
        winsound.PlaySound("upsss.wav", winsound.SND_ASYNC)
        time.sleep(1)

    # COLLISION BALL <-> PADDLE
    if ball.ycor() < -210 and ball.xcor() > paddle.xcor() - 42 and ball.xcor() < paddle.xcor() + 42:
        ball.sety(-210)
        ball.ball_dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    for br in levels.bricks:
        # COLLISION BRICK <-> BALL
        if math.sqrt(math.pow(br.xcor() - ball.xcor(), 2) + math.pow(br.ycor() - ball.ycor(), 2)) < 25 and br.active:
            #ball.sety(br.ycor())
            ball.ball_dy *= -1
            score_b.update(abs(br.ycor()))
            br.deactiate()
            disabled_bricks_counter.add()
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # COLLISION BRICK <-> BULLET
        if math.sqrt(math.pow(br.xcor() - bullet.xcor(), 2) + math.pow(br.ycor() - bullet.ycor(), 2)) < 25 and br.active:
            bullet.ready()
            bullet.hideturtle()
            score_b.update(abs(br.ycor()))
            br.deactiate()
            disabled_bricks_counter.add()
            winsound.PlaySound("bullethit.wav", winsound.SND_ASYNC)

    # BULLET - OUT OF THE SCREEN
    if bullet.ycor() > 250:
        bullet.hideturtle()
        bullet.ready()

    # NEXT LEVEL
    if levels.all_bricks_disabled():
        levels.next_level()

    # GAME OVER
    if lives_b.lives < 0:
        Game_Over_Screen()

    time.sleep(1 / 60)

screen.mainloop()
