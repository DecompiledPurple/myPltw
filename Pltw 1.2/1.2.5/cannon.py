import turtle
import math

screen = turtle.Screen()
screen.tracer(0)
cannon = turtle.Turtle(shape="square")
projectile = []

#initialize
cannon.penup()
cannon.color("gray10")
cannon.shapesize(stretch_wid=0.7,stretch_len=1.5)
cannon.goto(0, -250)
screen.update()

#functions
def launch(_x,_y):


    print("fire")

def aim(event):
     #offset the position down to the middle of the screen
    x = event.x - screen.window_width() / 2
    y = screen.window_height() / 2 - event.y

    #get cannon position so we can get the mouse position relative to it
    cannonX, cannonY = cannon.position()

    #get angles from our mouse
    radians = math.atan2(y - cannonY, x - cannonX)
    angle = math.degrees(radians)
    print(radians, angle)

    cannon.setheading(angle)
    screen.update()

#listeners

screen.getcanvas().bind('<Motion>', aim)

screen.onscreenclick(launch)

screen.mainloop()