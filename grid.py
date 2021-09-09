import turtle

count = -2

while (count <= 3):
    turtle.penup()
    turtle.goto(count*100, 300)
    turtle.pendown()
    turtle.goto(count*100, -200)
    count = count + 1

for count in [-2, -1, 0, 1, 2, 3]:
    turtle.penup()
    turtle.goto(-200, count*100)
    turtle.pendown()
    turtle.goto(300, count*100)
    count = count + 1

turtle.exitonclick()
    
