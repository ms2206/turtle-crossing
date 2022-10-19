import pdb
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from pdb import set_trace

list_of_cars = []

# GAME START
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True

# GAME LOGIC --START
# make cars
for car in range(1):
    list_of_cars.append(CarManager())

direction = True

# make cars move
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in list_of_cars:
        # pdb.set_trace()
        if direction:
            if car.xcor() > -300:
                car.move_car_forward()
                print('formward')
                print(car.xcor())

            else:
                direction = False

        elif car.xcor() < 300:
            car.move_car_backwards()
            print('backward')
            print(car.xcor())


        else:
            direction = True
            # print("😤")
            # print(car.xcor())







# GAME LOGIC --END

