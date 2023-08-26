from turtle import*
import math
color("red")
speed(0)
screensize(1400,750)

for i in range(1000000):
    forward(math.sqrt(i)*75)
    left(170)


mainloop()