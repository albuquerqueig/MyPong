# Import biblioteca turtle
import turtle

# Create screen (Criar tela onde será vizualizado o jogo)
sc = turtle.Screen()
sc.title("Pong by albuquerqueig")
sc.bgcolor("black")
sc.setup(width=800, height=600)

# Left paddle será a var = a_pad
a_pad = turtle.Turtle()
a_pad.speed(0)
a_pad.shape("square")
a_pad.color("white")
a_pad.shapesize(stretch_wid=5, stretch_len=1)
a_pad.penup()
a_pad.goto(-350, 0)

# Right paddle será a var = b_pad
b_pad = turtle.Turtle()
b_pad.speed(0)
b_pad.shape("square")
b_pad.color("white")
b_pad.shapesize(stretch_wid=5, stretch_len=1)
b_pad.penup()
b_pad.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# Initialize the score = Placar inicial
left_player = 0
right_player = 0

# Layouts score = Layout do placar
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("green")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0 Right_player: 0", align="center", font=("Courier", 24, "normal"))


# Functions to move paddle vertically = Funções de movimento dos paddles no eixo y
def paddleaup():
    y = a_pad.ycor()
    y += 20
    a_pad.sety(y)

def paddleadown():
    y = a_pad.ycor()
    y -= 20
    a_pad.sety(y)

def paddlebup():
    y = b_pad.ycor()
    y += 20
    b_pad.sety(y)

def paddlebdown():
    y = b_pad.ycor()
    y -= 20
    b_pad.sety(y)

# Keyboard bindings = Atributos de das teclas para movimentação
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

# Fazer looping do jogo
while True:
    sc.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checking borders = Bordas limites
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {} Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {} Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

# Paddle ball collision = Paddle rebatendo ball
    if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < b_pad.ycor() + 40 and ball.ycor() > b_pad.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < a_pad.ycor() + 40 and ball.ycor() > a_pad.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1

# when some player score 10, finish the game (tenho como ideia finalizar o jogo quando chegar em uma pontuação x,
# vou verificar como fazer