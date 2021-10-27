# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
spot_color = "pink"
spot_fillcolor = "pink"
spot_shape="square"
import random as rand
#-----game configuration----

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shapesize(6)
spot.shape(spot_shape)
spot.color(spot_color)
spot.fillcolor(spot_fillcolor)

def change_position():
  new_xpos = rand.randint(-400,400)
  new_ypos = rand.randint(-300,300)
  spot.goto(new_xpos, new_ypos)


#-----game functions--------
def spot_clicked(x,y):
  spot.hideturtle()
  spot.penup()
  change_position()
  spot.showturtle()


#-----events----------------
wn = trtl.Screen()
spot.onclick(spot_clicked)
wn.mainloop()