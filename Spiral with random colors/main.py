from turtle import * 
t = Turtle()
import random
screen = t.getscreen()
t.color("blue")
t.width(2)
t.speed(0)
colors = ["red","green","blue","yellow","purple","violet","orange"]

for i in range(75):
    t.color(random.choice(colors))
    t.right(20 +i)
    t.forward(1+(i*5))
    t.right(40 +i)

screen.exitonclick()
