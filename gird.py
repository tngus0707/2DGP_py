import turtle
count = -3

while (count <= 2):
    turtle.penup()
    turtle.goto(count*100, 300)
    turtle.pendown()
    turtle.goto(count*100, -200)
    count = count + 1


for count in [-3, -2, -1, 0, 1, 2]:
    turtle.penup()
    turtle.goto(-300, count*100+100)
    turtle.pendown()
    turtle.goto(200, count*100+100)
    count = count + 1

turtle.exitonclick()
