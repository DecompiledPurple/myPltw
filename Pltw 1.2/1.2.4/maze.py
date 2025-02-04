import turtle
import random

screen = turtle.Screen()
mazePainter = turtle.Turtle()
mazePainter.width(5)
mazePainter.speed(5)

MAZE_SIZE = 15
MAZE_WIDTH = 35
DOOR_SIZE = 35

def makeWall(index):
    mazePainter.forward(MAZE_WIDTH * index)

def makeDoor(index):
    position = random.randint(-MAZE_WIDTH, MAZE_WIDTH) * index /2.1
    splitWallSize = MAZE_WIDTH/2 * index - DOOR_SIZE/2


    mazePainter.forward(splitWallSize + position) #make part of wall
    mazePainter.penup()
    mazePainter.forward(DOOR_SIZE) #make the door
    mazePainter.pendown()
    mazePainter.forward(splitWallSize - position) #make other part of wall

def makeBarrier(index, withDoor):
    if withDoor:
        makeDoor(index)
    else:    
        makeWall(index)
    
    position = random.randint(5, MAZE_WIDTH - 5) * index 
    print(position)

    mazePainter.penup()
    mazePainter.backward(position) 
    mazePainter.right(90)
    mazePainter.backward(MAZE_WIDTH)
    mazePainter.pendown()
    mazePainter.forward(MAZE_WIDTH)
    mazePainter.left(90)
    mazePainter.penup()
    mazePainter.forward(position) 
    mazePainter.pendown()


def makeMaze():
    for i in range(MAZE_SIZE):
        makeBarrier(i, True)
        mazePainter.left(90)
        makeBarrier(i, True)
        mazePainter.left(90)

makeMaze()

screen.mainloop()