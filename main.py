#create color list
#import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random

stamp = Turtle()
stamp.penup()
stamp.hideturtle()
colormode(255)
color_list = [(226, 134, 70), (155, 97, 26), (18, 35, 56), (44, 106, 149), (224, 212, 2), (238, 80, 94), (237, 95, 36), (130, 215, 206), (149, 184, 220), (211, 154, 163), (165, 46, 135), (85, 182, 5), (51, 91, 85), (133, 217, 220), (219, 203, 108), (216, 131, 23), (139, 189, 163), (211, 184, 175), (230, 169, 182), (46, 75, 70), (91, 137, 158), (169, 190, 219), (25, 68, 106), (38, 59, 56), (106, 129, 151), (12, 77, 111)]

def random_color():
    return color_list[random.randint(0, len(color_list) - 1)]

def forward(number):
    for i in range(number - 1):
        stamp.dot(20, random_color())
        stamp.forward(50)

def right_end_flip():
    stamp.dot(20, random_color())
    stamp.left(90)
    stamp.forward(50)
    stamp.left(90)

def left_end_flip():
    stamp.dot(20, random_color())
    stamp.right(90)
    stamp.forward(50)
    stamp.right(90)

def create_hirst(length, height):
    rows_remaining = height
    while rows_remaining > 0:
        forward(length)
        right_end_flip()
        rows_remaining -= 1
        forward(length)
        left_end_flip()
        rows_remaining -= 1

create_hirst(10, 10)

screen = Screen()
screen.exitonclick()