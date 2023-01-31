from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.penup()
        self.speed("fastest")
        # setting initial position:
        random_x_position = random.randint(-280, 280)
        random_y_position = random.randint(-280, 280)
        self.goto(random_x_position, random_y_position)

    def new_location(self):
        """ Move the food icon to a new random location """
        random_x_position = random.randint(-280, 280)
        random_y_position = random.randint(-280, 280)
        self.goto(random_x_position, random_y_position)