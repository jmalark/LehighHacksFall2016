import turtle
import sys
def map(p):
    p.hideturtle()
    p.speed(9)
    p.up()
    p.goto(-300,-100)
    p.down()
    p.showturtle()
    p.left(90)
    for i in range (8):
        p.color("black")
        p.forward(200)
        p.right(45)
        color=""
        if i==0:
            color="yellow"
        elif i==1:
            color="pink"
        elif i==2:
            color="blue"
        elif i==3:
            color="green"
        elif i==4:
            color="orange"
        elif i==5:
            color="purple"
        elif i==6:
            color="brown"
        elif i==7:
            color="red"
        elif i==8:
            color="magenta"
        p.color(color)
        p.begin_fill()
        p.circle(10)
        p.end_fill()

def move(p,place):
    stop=0
    p.showturtle()
    p.color("black")
    #p.speed(1)
    p.up()
    #p.goto(-300, -100)
    while stop<place:
        p.speed(1)
        p.forward(200)
        p.right(45)
        stop+=1
    #p.showturtle()
    return stop
def back(p,steps):
    p.speed(9)
    for i in range (steps):
        p.hideturtle()
        p.left(45)
        p.backward(200)


