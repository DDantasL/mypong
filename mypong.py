import tkinter
import turtle
import os
import time
import sys

# desenhar tela
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# linha

linha = turtle.Turtle()
linha.shape("square")
linha.color("white")
linha.shapesize(stretch_wid=20, stretch_len=0.10)
linha.penup()
linha.goto(0, 0)

tela = turtle.Turtle()
tela.speed(0)
tela.shape("square")
tela.color("white")
tela.shapesize(stretch_wid=5, stretch_len=1)
tela.penup()
tela.goto(0, 0)
tela.write("   Menu  \n\n\n My Pong  \n\n\n\n  >1VS1", align="center",
           font=("Press Start 2P", 24, "normal"))
tela.hideturtle()
time.sleep(3)
tela.clear()

# desenhar raquete 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# desenhar raquete 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# desenhar bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# pontuação
score_1 = 0
score_2 = 0

# head-up display da pontuação
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

# mover raquete 1


def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_2.sety(y)

# mapeando as teclas
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
if len(sys.argv) == 1:
    screen.onkeypress(paddle_2_up, "Up")
    screen.onkeypress(paddle_2_down, "Down")


while True:
    screen.update()

    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # colisão com parede superior
    if ball.ycor() > 290:
        os.system("aplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1

    # colisão com parede inferior
    if ball.ycor() < -280:
        os.system("aplay bounce.wav&")
        ball.sety(-280)
        ball.dy *= -1

    # colisão com parede esquerda
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center",
                  font=("Press Start 2P", 24, "normal"))
        os.system("aplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1

    # colisão com parede direita
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center",
                  font=("Press Start 2P", 24, "normal"))
        os.system("aplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1

    # colisão com raquete 1
    if (ball.xcor() < -330 and ball.ycor() < paddle_1.ycor() +
            50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    #  colisão com raquete 2
    if (ball.xcor() > 330 and ball.ycor() < paddle_2.ycor() +
            50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.dx *= -1
        ball.setx(330)
        os.system("aplay bounce.wav&")

    # score

    if score_1 == 5 or score_2 == 5:
        ball.setx(0)
        ball.sety(0)

    # modo 1sp
    if len(sys.argv) == 2:
        if sys.argv[1] == "-1":
            paddle_2.sety(ball.ycor())
