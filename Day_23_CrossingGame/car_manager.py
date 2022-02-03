from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.cars = []
        self.move_speed = 0.1
        self.initial_cars()

    def initial_cars(self):
        for _ in range(15):
            self.add_car((random.randint(-300, 300), random.randint(-250, 250)))

    def remove_car(self):
        for car in self.cars:
            if car.xcor() < -330:
                self.cars.remove(car)

    def add_car(self, coordinates):
        if len(self.cars) < 15:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(coordinates)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        self.move_speed *= 0.7

    def reset_cars(self):
        self.move_speed = 0.1
        self.initial_cars()
