from random import choice, randint
from turtle import Turtle

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 100
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cords = [x for x in range(-280, 280, 30)]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(choice(COLORS))
        self.shape("square")
        self.shapesize(1,2)
        self.setx(250)
        self.sety(choice(y_cords))


    def move_car_forward(self):
        self.setheading(180)
        self.forward(MOVE_INCREMENT)


    def move_car_backwards(self):
        self.backward(MOVE_INCREMENT)

#TODO: add function to control speed