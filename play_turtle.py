import turtle


turtle.color('red', 'yellow')
turtle.begin_fill()
for _ in range(5):
    turtle.forward(100)
    turtle.right(360 / 5 * 2)
turtle.end_fill()
turtle.done()