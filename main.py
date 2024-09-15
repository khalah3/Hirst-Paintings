import turtle
from turtle import Turtle,Screen
import random
import colorgram as t


my_Turtle = Turtle()

turtle.colormode(255)
my_Turtle.speed('fastest')

all_colors=[]
colors = t.extract('hirst_image.jpg', 100)



for color in colors:
   x = color.rgb
   r=x[0]
   g=x[1]
   b=x[2]
   my_tuple=(r,g,b)
   y = all_colors.append(my_tuple)

print(all_colors)

def turtle_color_choice():
   my_Turtle.width(10)
   colorchoice=random.choice(all_colors)
   my_Turtle.color(colorchoice)

new_Turtle=[]


def turtle_horizental_movement():
    for i in range(10):
        turtle_color_choice()
        my_Turtle.dot(20,random.choice(all_colors))
        my_Turtle.penup()
        my_Turtle.forward(50)



def turtle_full_movement():
   y=-200

   for i in range(10):
      z=y
      my_Turtle.penup()
      my_Turtle.setpos(-200,z)
      y=z+50
      turtle_horizental_movement()


turtle_full_movement()
my_Turtle.hideturtle()


screen=Screen()
screen.exitonclick()
