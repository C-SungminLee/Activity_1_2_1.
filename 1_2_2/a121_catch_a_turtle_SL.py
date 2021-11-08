# a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl
import random as rand

import leaderboard as lb

wn = trtl.Screen()
wn.addshape("star.gif")

def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard("a122_leaderboard.txt", leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard("a122_leaderboard.txt", leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)


#-----game configuration----


user_input = wn.textinput("Menu", "Do you want to play?")
if user_input != "no":
  user_input = True
else: 
  user_input = False
if user_input == True:

  leader_names_list = []
  leader_scores_list = []
  player_name =(wn.textinput("Menu", "What is your name?"))

  spot_shape = "star.gif"
  spot_color = "white" 
  spot_size = 100
  score = 0

  font_setup = ("Arial", 20, "normal")

  timer = int(wn.textinput("Menu", "How much time for you game? Enter here"))

  counter_interval = 1000   #1000 represents 1 second
  timer_up = False

  coordinate_list = []
  color = ["White", "Yellow", "Orange", "Gold", "Light Yellow"]
  sizes =[0.5,1,1,1,1,1,1,2,2,2,2,2,2,5]


  #-----initialize turtle-----
  counter =  trtl.Turtle()
  spot = trtl.Turtle()
  score_writer = trtl.Turtle()
  t = trtl.Turtle
  counter.color("white")
  score_writer.color("white")

  #-----game functions--------
  def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
      counter.write("Time's Up", font=font_setup)
      timer_up = True
      manage_leaderboard()
      trtl.bye
    else:
      counter.write("Timer: " + str(timer), font=font_setup)
      timer -= 1
      counter.getscreen().ontimer(countdown, counter_interval) 

  def spot_clicked(x,y):
    global timer
    if timer != 0:
      spot.color("red")
      spot.color(spot_color)

      spot.penup()
      spot_s = spot.clone()
      spot_s.turtlesize(rand.choice(sizes))
      spot_s.shape("circle")
      spot_s.color(rand.choice(color))
      spot_s.stamp()
      spot.hideturtle
      change_position()
      update_score()

      spot.showturtle
    else: 
      spot.hideturtle


  def change_position():
    new_xpos = rand.randint(-350,350) 
    new_ypos = rand.randint(-150,150)
    spot.speed(5)
    spot.goto( new_xpos,new_ypos )
    spot.speed(0)


  def update_score():
    score_writer.clear()
    global score
    score += 1
    score_writer.write("Score: " + str(score), font=font_setup)

  score = -1
  update_score()

  def start_game():
    counter.penup()
    counter.hideturtle()
    counter.goto(-200,200)
    counter.pendown()    


    score_writer.penup()
    score_writer.hideturtle()
    score_writer.goto(-200,175)
    score_writer.pendown()

    spot.shape(spot_shape)
    spot.color(spot_color)
    spot.pensize(spot_size)

    font_setup = ("Arial", 20, "normal")


    score = -1
    update_score()

  start_game()

  #-----events----------------

  spot.onclick(spot_clicked)

  wn.ontimer(countdown, counter_interval) 
  wn.bgcolor("black")
  wn.mainloop()

else:
  trtl.bye
wn.mainloop()