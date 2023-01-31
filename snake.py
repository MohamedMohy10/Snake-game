from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    # snake setup:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        """ Create the snake with initial length"""
        for position in INITIAL_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """ Add a snake segment """
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.setpos(position)
        self.snake_segments.append(segment)

    def extend(self):
        """ Increase the snake length by extending tail """
        self.add_segment(self.snake_segments[-1].position())

    def tail_bite(self):
        """ Detects biting tail scenarios """
        for segment in self.snake_segments[1:]:
            if self.head.distance(segment) < 10:
                return True

    # snake movement:
    def move(self):
        for seg in range(len(self.snake_segments) - 1, 0, -1):
            new_pos = self.snake_segments[seg - 1].position()
            self.snake_segments[seg].goto(new_pos)
        self.head.forward(MOVE_STEP)

    # snake directions:
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
