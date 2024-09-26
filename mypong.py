import turtle
import os
import sys

# Função para tocar sons
def play_sound(file):
    os.system(f"aplay {file}&")

# Configuração da tela
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Linha central
linha = turtle.Turtle()
linha.shape("square")
linha.color("white")
linha.shapesize(stretch_wid=20, stretch_len=0.10)
linha.penup()
linha.goto(0, 0)

# Função para criar raquete
def criar_raquete(pos_x):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(pos_x, 0)
    return paddle

paddle_1 = criar_raquete(-350)
paddle_2 = criar_raquete(350)

# Criação da bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Variáveis de pontuação
score_1 = 0
score_2 = 0

# Função para criar HUD de pontuação
def criar_hud():
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 260)
    hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))
    return hud

hud = criar_hud()

# Função de tela de vitória
def mostrar_vitoria(player):
    telav = turtle.Turtle()
    telav.speed(0)
    telav.shape("square")
    telav.color("white")
    telav.shapesize(stretch_wid=5, stretch_len=1)
    telav.penup()
    telav.goto(0, 0)
    telav.hideturtle()
    telav.write(f"VITÓRIA PLAYER {player}", align="center", font=("Press Start 2P", 24, "normal"))

# Tela inicial com "Press Any Button to Start"
def mostrar_menu_inicial():
    tela_menu = turtle.Turtle()
    tela_menu.speed(0)
    tela_menu.shape("square")
    tela_menu.color("white")
    tela_menu.penup()
    tela_menu.hideturtle()
    tela_menu.goto(0, 0)
    tela_menu.write("          My Pong  \n\n\n\n  Press SPACE to Start", align="center", font=("Press Start 2P", 24, "normal"))
    return tela_menu

# Mostrar HUD durante o menu
def mostrar_hud_inicial():
    hud.clear()
    hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

tela_menu = mostrar_menu_inicial()
mostrar_hud_inicial()

# Iniciar o jogo ao pressionar qualquer tecla
def iniciar_jogo():
    tela_menu.clear()
    jogar()

screen.listen()
screen.onkeypress(iniciar_jogo, "space")  # Pode ser substituído por qualquer tecla, aqui usei 'space'

# Função para mover raquetes
def mover_raquete(raquete, direcao):
    y = raquete.ycor()
    y = max(min(y + direcao, 250), -250)
    raquete.sety(y)

# Movimentação das raquetes
def paddle_1_up():
    mover_raquete(paddle_1, 20)

def paddle_1_down():
    mover_raquete(paddle_1, -20)

def paddle_2_up():
    mover_raquete(paddle_2, 20)

def paddle_2_down():
    mover_raquete(paddle_2, -20)

# Mapeando as teclas
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")

# Se não houver argumento, ativar controles para o player 2
if len(sys.argv) == 1:
    screen.onkeypress(paddle_2_up, "Up")
    screen.onkeypress(paddle_2_down, "Down")

# Função principal do jogo
def jogar():
    global score_1, score_2

    while True:
        screen.update()

        # Movimentação da bola
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Colisões com as paredes
        if ball.ycor() > 290:
            play_sound("bounce.wav")
            ball.sety(290)
            ball.dy *= -1
        elif ball.ycor() < -280:
            play_sound("bounce.wav")
            ball.sety(-280)
            ball.dy *= -1

        # Pontuação
        if ball.xcor() < -390:
            score_2 += 1
            hud.clear()
            hud.write(f"{score_1} : {score_2}", align="center", font=("Press Start 2P", 24, "normal"))
            play_sound("258020__kodack__arcade-bleep-sound.wav")
            ball.goto(0, 0)
            ball.dx *= -1
        elif ball.xcor() > 390:
            score_1 += 1
            hud.clear()
            hud.write(f"{score_1} : {score_2}", align="center", font=("Press Start 2P", 24, "normal"))
            play_sound("258020__kodack__arcade-bleep-sound.wav")
            ball.goto(0, 0)
            ball.dx *= -1

        # Colisões com as raquetes
        if (-330 > ball.xcor() > -340) and paddle_1.ycor() - 50 < ball.ycor() < paddle_1.ycor() + 50:
            ball.setx(-330)
            ball.dx *= -1
            play_sound("bounce.wav")
        elif (330 < ball.xcor() < 340) and paddle_2.ycor() - 50 < ball.ycor() < paddle_2.ycor() + 50:
            ball.setx(330)
            ball.dx *= -1
            play_sound("bounce.wav")

        # Verificar se algum jogador venceu
        if score_1 == 5 or score_2 == 5:
            ball.goto(0, 0)
            mostrar_vitoria(1 if score_1 == 5 else 2)
            break

        # Modo single player
        if len(sys.argv) == 2 and sys.argv[1] == "-1":
            paddle_2.sety(ball.ycor())

# Aguarda o jogador pressionar qualquer tecla para começar
screen.mainloop()
