import turtle
import math
import time

screen = turtle.Screen()
screen.tracer(0)
cannon = turtle.Turtle(shape="square")
projectiles = []

processing = False
fireAngle = 90

GRAVITY = 1
STRENGTH = 25


#initialize
cannon.penup()
cannon.color("gray10")
cannon.shapesize(stretch_wid=0.7,stretch_len=1.5)
cannon.goto(0, -250)

screen.update()
#class
class createProjectile():
     def __init__(self, turtle, xForce, yForce):
          self.turtle = turtle
          self.xForce = xForce
          self.yForce = yForce


#functions

def launch(_x,_y):
    global processing

    # create new projectile
    newProjectile = turtle.Turtle(shape="circle")
    newProjectile.goto(cannon.position())
    newProjectile.setheading(cannon.heading())
    angleInRadians = math.radians(fireAngle)
    # calculate angle to set a trajectory to our individual projectile 
    yPower = math.sin(angleInRadians) * STRENGTH
    xPower = math.cos(angleInRadians) * STRENGTH    
    createdProjectile = createProjectile(newProjectile, xPower, yPower)
    projectiles.append(createdProjectile)


    # processing the movement of all live projectiles
    if not processing: 
        processing = True
        maxProcess = 1000 #temporary for control
        while processing:     
            #loop through all projectiles, move each, then refresh the frame, simulating simoultaneous movement
            if maxProcess > 0:
                for projectile in projectiles:
                        projectile.yForce = projectile.yForce - GRAVITY
                        x,y = projectile.turtle.position()

                        projectile.turtle.goto(x + projectile.xForce, y + projectile.yForce)

                        maxProcess -= 1
                        
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

    global fireAngle
    fireAngle = angle
    cannon.setheading(angle)
    screen.update()

#listeners

screen.getcanvas().bind('<Motion>', aim)

screen.onscreenclick(launch)

screen.mainloop()
