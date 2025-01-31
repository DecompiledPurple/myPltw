# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random
import leaderboard as lb

#-----variables-------------
wn = turtle.Screen()
spot = turtle.Turtle()
scoreWriter = turtle.Turtle()
timeWriter = turtle.Turtle()
messageWriter = turtle.Turtle()

#-----game configuration----
leaderboardFileName = "a122_leaderboard.txt"
lb.getNames(leaderboardFileName)
lb.getScores(leaderboardFileName)
playerName = input("Enter username")

score = 0
timer = 10
timerUp = False
gameStarted = False

TIMER_INTERVAL = 1000
FONT_SETUP = ("Arial", 20, "normal")
RANGE = (400, 300) # x,y 
TURTLE_SHAPE = "circle"
TURTLE_SIZE = 3
TURTLE_COLOR = "darkblue"
SPOT_COLOR = "pink"

#-----initialize turtle-----
spot.shape(TURTLE_SHAPE)
spot.shapesize(TURTLE_SIZE)
spot.color(TURTLE_COLOR)
spot.penup()
scoreWriter.penup()
scoreWriter.goto(-60, 150)
scoreWriter.hideturtle()
timeWriter.penup()
timeWriter.goto(-60, 200)
timeWriter.hideturtle()
messageWriter.penup()
messageWriter.goto(-130, 100)
messageWriter.hideturtle()

messageWriter.write("Click me to start game", font=FONT_SETUP)

#-----game functions--------
def manageLeaderboard():

    global score
    global spot

    leaderNamesList = lb.getNames(leaderboardFileName)
    leaderScoresList = lb.getScores(leaderboardFileName)

    if (len(leaderScoresList) < 5 or score >= leaderScoresList[4]):
         lb.updateLeaderboard(leaderboardFileName, leaderNamesList, leaderScoresList, playerName, score)
         lb.drawLeaderboard(True, leaderNamesList, leaderScoresList, spot, score)

    else:
         lb.drawLeaderboard(False, leaderNamesList, leaderScoresList, spot, score)

def countdown():
    global timer, timerUp
  
    timeWriter.clear()
    timer -= 1

    if timer < 0 and not timerUp:
        timerUp = True
        timeWriter.write("Time's up!", font=FONT_SETUP)
        spot.hideturtle()
        manageLeaderboard()
    else:
        timeWriter.write("Time: " + str(timer), font=FONT_SETUP)
        timeWriter.getscreen().ontimer(countdown, TIMER_INTERVAL)
    

def updateScore():
    global score
    score += 1
    scoreWriter.clear()
    scoreWriter.write("Score: " + str(score), font=FONT_SETUP)

def changePosition():
    newX = random.randint(-RANGE[0], RANGE[0])
    newY = random.randint(-RANGE[1], RANGE[1])
    spot.goto(newX, newY)

def spotClicked(_x,_y):
   global gameStarted
   if not gameStarted:
        gameStarted = True
        messageWriter.clear()
        wn.ontimer(countdown, TIMER_INTERVAL)
        updateScore()
   else:
        if timerUp: return
        changePosition()
        updateScore()

#-----events----------------
spot.onclick(spotClicked)

wn.mainloop()