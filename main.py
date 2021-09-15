import turtle

def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.goto(50, 50)
    turtle.down()
    turtle.home()
    turtle.circle(50)
    input()

def draw_star():
    turtle.color('red', 'orange')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
    if abs() (turtle.pos()) < 1:
            turtle.end_fill()

def main():
    #test_drive()
    draw_star()

main()
