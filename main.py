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

def turtle_state():
    x = turtle.isdown()
    print ("Turtle pen state", x)
    y = turtle.heading()
    print ("Turtle heading is", y)
    print ("xcor:",turtle.xcor(),"ycor:",turtle.ycor())

def draw_square(side,color):
    turtle.setheading(50)
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.end_fill()


def main():
    #test_drive()
    draw_square(50,"red")
    draw_square(100,"yellow")
    draw_square(150,"orange")


    input("hit anything to exit")
    turtle_state()

main()
