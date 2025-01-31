#   a123_apple_1.py
import turtle as trtl
import random

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

appleA = trtl.Turtle()
appleC = trtl.Turtle()
appleL = trtl.Turtle()
appleR = trtl.Turtle()

currentApple = appleA

#----Constants------
KEYS = ["a","c","l","r"]
FONT1 = ("Arial", 55, "bold")

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  x = random.randint(-150, 150)
  y = random.randint(10, 150)
  active_apple.shape(apple_image)
  active_apple.penup()
  active_apple.goto(x,y)
  wn.update()

def write_heading(letter, apple):
  wn.tracer(False)
  apple.write("letter", FONT1)
  wn.tracer(True)


def drop_apple(apple):
  apple.clear()
  apple.goto(apple.xcor(), -150)
  apple.hideturtle()

def return_apple(apple):
    currentApple.hideturtle()


#-----function calls-----
draw_apple(appleA)
draw_apple(appleC)
draw_apple(appleL)
draw_apple(appleR)
#write_heading()

#-----listeners------

wn.onkeypress(drop_apple, "a")


wn.listen()
wn.mainloop()