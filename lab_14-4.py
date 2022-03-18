# Author: JD 03/18/2022
import turtle
window = turtle.Screen()
window.title("Lab 4")
window.bgcolor("gray")

turtle4 = turtle.Turtle()
turtle4.shape("turtle")
turtle4.pencolor("yellow")
turtle4.color("red")

turtle4.stamp()
turtle4.speed(10)
turtle4.penup()
turtle4.setposition(100,100)
turtle4.pendown()
turtle4.goto(200,100)
turtle4.goto(200,0)
turtle4.goto(100,0)
turtle4.goto(100,100)

window.mainloop()