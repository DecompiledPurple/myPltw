import turtle
import math
import time

screen = turtle.Screen()
screen.tracer(0)
cannon = turtle.Turtle(shape="square")
projectiles = []

processing = False


#initialize
cannon.penup()
cannon.color("gray10")
cannon.shapesize(stretch_wid=0.7,stretch_len=1.5)
cannon.goto(0, -250)

screen.update()

#functions
def launch(_x,_y):
    global processing
    newProjectile = turtle.Turtle(shape="circle")
    newProjectile.goto(cannon.position())
    newProjectile.setheading(cannon.heading())
    projectiles.append(newProjectile)



    # processing the movement of all live projectiles
    if not processing: 
        processing = True
        maxProcess = 1000 #temporary for control
        while processing:
           
            #loop through all projectiles, move each, then refresh the frame, simulating simoultaneous movement
            if maxProcess > 0:
                for projectile in projectiles:
                        maxProcess -= 1
                        projectile.forward(10)
                screen.update()
            else: 
                processing = False
                for projectile in projectiles:
                    projectiles.remove(projectile)
                    projectile.hideturtle()
                    del projectile
                screen.update()
            time.sleep(0.01)
                           
        



def aim(event):
    #offset the position down to the middle of the screen
    x = event.x - screen.window_width() / 2
    y = screen.window_height() / 2 - event.y

    #get cannon position so we can get the mouse position relative to it
    cannonX, cannonY = cannon.position()

    #get angles from our mouse position
    radians = math.atan2(y - cannonY, x - cannonX)
    angle = math.degrees(radians)

    cannon.setheading(angle)
    screen.update()

#listeners

screen.getcanvas().bind('<Motion>', aim)

screen.onscreenclick(launch)

screen.mainloop()
