from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# Creating game objects
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()  # listening to user inputs
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect eating food by comparing distance then updating the snake length and score
    if snake.head.distance(food) < 15:
        snake.extend()
        food.new_location()
        score.update_score()

    # Detect hitting border
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_on = False
        score.game_over()

    # Detect tail bite
    if snake.tail_bite():
        game_on = False
        score.game_over()

screen.exitonclick()
