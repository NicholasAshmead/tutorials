import turtle as t
import random as r
import argparse as arg

parser = arg.ArgumentParser(description="Turtle drawing program")
parser.add_argument("-o", "--option", type=int, help="The option to use")
parser.add_argument("-p", "--hide", type=bool, help="Hide the turtle")
args = parser.parse_args()

t.bgcolor("black")
t.colormode(255)

john = t.Turtle()
john.speed(0)
john.color("white")

if args.hide == False: pass
else: john.hideturtle()

if args.option == None: option = 4
else: option = args.option

def nSidedShape(sides, length):
    john.penup()
    john.goto(0, 250)
    john.pendown()
    for i in range(sides):
        john.forward(length)
        john.right(360/sides)

if option == 1:
    for i in range(10000):
        john.color(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
        john.right(r.randint(1, 359))
        distance = r.randint(0, 300)
        john.forward(distance)
        john.right(180)
        john.forward(distance)
        john.right(180)

elif option == 2:
    for i in range(10000):
        john.color(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
        john.right(r.randint(1, 359))
        distance = r.randint(3, 19)
        john.forward(distance)

elif option == 3:
    john.penup()
    john.goto(0, 200)
    john.pendown()
    # draw a rainbow
    for i in range(32):
        for j in range(32):
            for k in range(32):
                john.color(i*8, j*8, k*8)
                john.forward(2)
                john.right(1)
            john.right(90)
            john.forward(5)
            john.left(90)

elif option == 4:
    for i in range(1,15):
        nSidedShape(i, 20)


t.mainloop()