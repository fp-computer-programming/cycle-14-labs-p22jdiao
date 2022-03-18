import turtle
window = turtle.Screen()
window.setup(1000, 1000)
window.screensize(800, 800)
window.title("Lab 1")

n = int(input("n: "))
turtle1 = turtle.Turtle()
x =(n-2)*180/n
y= 0
while y <= n:

    turtle1.forward(50)
    turtle1.right(x)
    y+=1
window.mainloop()