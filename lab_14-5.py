# Author: JD 03/21/2022

import turtle
def move_forward():
    turtle5.forward(50)

def move_backward():
    turtle5.backward(50)

def turn_left():
    turtle5.left(90)

def turn_right():
    turtle5.right(90)
window = turtle.Screen()
turtle5 = turtle.Turtle()
window.onkey(move_forward, "Up")
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")
window.listen()
window.mainloop()