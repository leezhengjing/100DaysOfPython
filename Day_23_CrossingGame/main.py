import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, 'w')


game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    car_manager.remove_car()
    car_manager.add_car((330, random.randint(-260, 290)))
    car_manager.move()

    # Detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 29 and player.ycor() + 25 >= car.ycor():
            scoreboard.game_over()
            game_is_on = False

    # Detect finish line
    if player.ycor() >= 280:
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.level_up()


screen.exitonclick()