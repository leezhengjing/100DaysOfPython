import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("gainsboro")
# Challenge 1
# for number in range(4):
#     tim.forward(100)
#     tim.right(90)

# Challenge 2
# for number in range(50):
#     if number % 2 == 0:
#         tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 3
# for number in range(3, 20):
#     interior_angle = ((number - 2) * 180) / number
#     for side in range(number):
#         tim.forward(100)
#         tim.right(180 - interior_angle)


# turtle_colors = [
#     'turquoise',
#     'dark turquoise',
#     'cyan',
#     'medium turquoise',
#     'aquamarine',
#     'sea green',
#     'lime',
#     'deep pink',
#     'red',
#     'dark magenta',
# ]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range (3, 11):
#     tim.color(random.choice(turtle_colors))
#     draw_shape(shape_side_n)
directions = [
    0,
    90,
    180,
    270,
]

turtle_colors = [
    'turquoise',
    'dark turquoise',
    'cyan',
    'medium turquoise',
    'aquamarine',
    'sea green',
    'lime',
    'deep pink',
    'red',
    'dark magenta',
]


def random_walk(num_steps):
    for step in range(num_steps):
        tim.color(random_color())
        tim.setheading(random.choice(directions))
        tim.forward(30)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



tim.speed("fastest")
tim.pensize(3)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


# def make_spirograph(radius):
#     for angle in range(36):
#         tim.color(random_color())
#         tim.setheading(angle * 10)
#         tim.circle(radius)
#
#
# make_spirograph(300)

screen = t.Screen()
screen.exitonclick()

