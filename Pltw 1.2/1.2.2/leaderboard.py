
bronzeScore = 15
silverScore = 20
goldScore = 25

# return names in the leaderboard file
def getNames(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this

  # use a for loop to iterate through the content of the file, one line at a time
  # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"

  names = []
  for line in leaderboard_file:
    leader_name = ""
    index = 0

    # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
    while (line[index] != ","):
        leader_name = leader_name + line[index] 
        index = index + 1   
   
    # TODO 2: add the player name to the names list
    names.append(leader_name)

  leaderboard_file.close()

  #  TODO 6: return the names list in place of the empty list
  return names

  
# return scores from the leaderboard file
def getScores(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this

  scores = []
  for line in leaderboard_file:
    leader_score = ""    
    #index = 0
    skipped = False
    # TODO 3: use a while loop to index beyond the comma, skipping the player's name
    for character in line: #used for loop instead
      if skipped:
        leader_score = leader_score + character
      elif character == ",":
        skipped = True
        
    # TODO 4: use a while loop to get the score

    # TODO 5: add the player score to the scores list
    scores.append(int(leader_score))

  leaderboard_file.close()
  # TODO 7: return the scores in place of the empty list
  return scores


# update leaderboard by inserting the current player and score to the list at the correct position
def updateLeaderboard(file_name, leader_names, leader_scores, player_name, player_score):

  index = 0
  # TODO 8: loop through all the scores in the existing leaderboard list
  for score in leader_scores:
    # TODO 9: check if this is the position to insert new score at
    if (player_score > score):
      break
    else:
      index = index + 1

  
  # TODO 10: insert new player and score
  leader_names.insert(index, player_name)
  leader_scores.insert(index, player_score)
  # TODO 11: keep both lists at 5 elements only (top 5 players)
  while len(leader_names) > 5:
    leader_names.pop()
  while len(leader_scores) > 5:
    leader_scores.pop()
  # TODO 12: store the latest leaderboard back in the file
  
  
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
 
  # TODO 13 loop through all the leaderboard elements and write them to the the file
  for i in range(len(leader_scores)):
    leaderboard_file.write(leader_names[i] + "," + str(leader_scores[i]) + "\n")

  leaderboard_file.close()
  

# draw leaderboard and display a message to player
def drawLeaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()

  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  for index in range(len(leader_names)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.down()
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()

  # TODO 14: display message about player making/not making leaderboard
  '''
    turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
    turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)
  '''

  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  # TODO 15: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
  '''
    turtle_object.write("You earned a gold medal!", font=font_setup)
    turtle_object.write("You earned a silver medal!", font=font_setup)
    turtle_object.write("You earned a bronze medal!", font=font_setup)
  '''