# Author: JD 03/21/2022

import turtle
window = turtle.Screen()

def change_color(color):
    turtle6.color(color)
def change_size(size):
    turtle6.shapesize(size)
def create_square():
    turtle6.begin_fill()
    for x in range(4):
        turtle6.forward(100)
        turtle6.right(90)
    turtle6.end_fill()

turtle6 = turtle.Turtle()

change_color(window.textinput("color","Enter the color: "))
change_size(window.numinput("size", "Enter the size: ", default=1, minval=1,maxval=5))
window.onclick(create_square(),btn=1)
window.listen()
window.mainloop()