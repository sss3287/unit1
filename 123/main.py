import turtle
X_MAX=200
X_MIN=-X_MAX
Y_MAX=200
Y_MIN=-Y_MAX

def rectangle_will_fit(x,y,length,height):
    if x >X_MIN and x <X_MAX :
        print ("Yes")
    elif  y > -Y_MIN and y < Y_MAX:
        print ("Yes")
    else:
        print ("No")

def test_rectangle_will_fit():
    rectangle_will_fit(100,150,50,60)

def main():
    rectangle_will_fit(100,150,50,60)

    main()
