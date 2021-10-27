#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)


legs = 6
leg_length = 60
angle_of_legs = 360 / legs
ladybug.pensize(5)
incrementing_counter = 0
angle_of_one_side_to_another=-55
#Draw legs
while (incrementing_counter < legs):  
  ladybug.goto(0,-30)
  ladybug.setheading(((angle_of_legs-20)*incrementing_counter)+angle_of_one_side_to_another)
  ladybug.forward(leg_length)
  incrementing_counter = incrementing_counter + 1
  if(incrementing_counter==3):
    angle_of_one_side_to_another+=90
ladybug.setheading(0)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()