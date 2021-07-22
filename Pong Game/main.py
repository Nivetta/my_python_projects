from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

# setting up and customising screen
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG GAME")

# Turn off animation
screen.tracer(0)

# creating objects of Paddle class
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

# Listens to key presses
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    score.update_score()
    # sleeps after each iteration
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()
        
    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor()< -320:
        ball.bounce_x()
            
    # Detect when ball goes out of bounds
    # Detects when right paddle misses
    if ball.xcor() > 380:
        time.sleep(0.1)
        score.l_score()
        ball.refresh()
    
    # Detects when right paddle misses    
    if ball.xcor() < -380:
        time.sleep(0.1)
        score.r_score()
        ball.refresh()
        

screen.exitonclick()