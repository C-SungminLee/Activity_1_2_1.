# a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl
import random as rand
wn = trtl.Screen()
wn.addshape('star.gif')

#-----game configuration----

spot_shape = "star.gif"
spot_color = "white" 
spot_size = 100
score = 0

font_setup = ("Arial", 20, "normal")
user_input = wn.textinput("Menu", "Do you want to play?")

timer = wn.textinput("Menu", "How much time for you game? Enter here")

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
  coordinate_list.append(str(new_xpos)) and (str(new_ypos))
  print(coordinate_list)
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
if user_input == "yes":
  start_game()
else:
  wn.textinput("Menu", "Okay, goodbye!")
  trtl.bye()
#-----events----------------

spot.onclick(spot_clicked)

wn.ontimer(countdown, counter_interval) 
wn.bgcolor("black")
wn.mainloop()
