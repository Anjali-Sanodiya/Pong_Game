import turtle as t

# Initialize scores
playerAscore = 0
playerBscore = 0

# Set up the screen
window = t.Screen()
window.title("Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# Create left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Create right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Create ball
ball = t.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ballxdirection = 0.2
ballydirection = 0.2

# Create pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=('Arial', 24, 'normal'))

# Define paddle movements
def leftpaddleup():
    y = leftpaddle.ycor()
    y += 20
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    y -= 20
    leftpaddle.sety(y)

def rightpaddleup():
    y = rightpaddle.ycor()
    y += 20
    rightpaddle.sety(y)

def rightpaddledown():
    y = rightpaddle.ycor()
    y -= 20
    rightpaddle.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerAscore += 1
        pen.clear()
        pen.write(f"Player A: {playerAscore}  Player B: {playerBscore}", align="center", font=('Arial', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerBscore += 1
        pen.clear()
        pen.write(f"Player A: {playerAscore}  Player B: {playerBscore}", align="center", font=('Arial', 24, 'normal'))

    # Paddle and ball collisions
    if ((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 50 and ball.ycor() > leftpaddle.ycor() - 50)):
        ball.setx(-340)
        ballxdirection *= -1

    if ((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 50 and ball.ycor() > rightpaddle.ycor() - 50)):
        ball.setx(340)
        ballxdirection *= -1