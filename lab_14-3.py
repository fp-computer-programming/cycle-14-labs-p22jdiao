# Author: JD 03/18/2022
import turtle
window = turtle.Screen()
window.setup(500, 500)
window.screensize(400, 400)
window.title("Lab 3")
window.bgcolor("gray")

turtle3 = turtle.Turtle()
turtle3.shape("turtle")
turtle3.pencolor("yellow")
for x in range(3):
    turtle3.backward(200)
    turtle3.right(120)
window.mainloop()

