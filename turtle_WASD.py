import turtle

def W_move():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def A_move():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def S_move():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def D_move():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()
    
turtle.shape('turtle')

turtle.onkey(W_move, 'w')
turtle.onkey(A_move, 'a')
turtle.onkey(S_move, 's')
turtle.onkey(D_move, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
