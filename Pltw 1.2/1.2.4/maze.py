import turtle

screen = turtle.Screen()
mazePainter = turtle.Turtle()
mazePainter.width(5)

MAZE_SIZE = 15
MAZE_WIDTH = 35
DOOR_SIZE = 35

def makeDoor(index):
    mazePainter.forward(MAZE_WIDTH/2 * index)
    mazePainter.penup()
    mazePainter.forward(DOOR_SIZE)
    mazePainter.pendown()
    mazePainter.forward((MAZE_WIDTH/2 * index) - DOOR_SIZE)

def makeBarrier(index):
    mazePainter.penup()
    mazePainter.backward((MAZE_WIDTH/2 * index) + 35)
    mazePainter.right(90)
    mazePainter.backward(MAZE_WIDTH)
    mazePainter.pendown()
    mazePainter.forward(MAZE_WIDTH)
    mazePainter.left(90)
    mazePainter.penup()
    mazePainter.forward((MAZE_WIDTH/2 * index) + 35)
    mazePainter.pendown()


def makeMaze():
    for i in range(MAZE_SIZE):
        mazePainter.forward(MAZE_WIDTH * i)
        makeBarrier(i)
        mazePainter.left(90)
        mazePainter.forward(MAZE_WIDTH * i)
        makeBarrier(i)
        mazePainter.left(90)

makeMaze()

screen.mainloop()