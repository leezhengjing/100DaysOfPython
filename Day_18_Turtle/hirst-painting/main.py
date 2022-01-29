# import colorgram as c
#
# colors = c.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     color_rgb = color.rgb
#     r = color_rgb[0]
#     g = color_rgb[1]
#     b = color_rgb[2]
#     color_tuple = (r, g, b)
#     rgb_colors.append(color_tuple)
#
# print(rgb_colors)
import turtle as t
import random
from color_list import color_list


def dot_row():
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)


def raise_height():
    tim.setx(0)
    tim.sety(50)

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setposition(-200, -200)

for _ in range(10):
    dot_row()
    tim.setx(-200)
    tim.sety(tim.ycor() + 50)

tim.home()


screen.exitonclick()
