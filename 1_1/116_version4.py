#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
#Create a spider body
spider.pensize(40)
spider.circle(20)
#Configure spider legs
legs = 8
leg_length = 70
angle_of_legs = 360 / legs
spider.pensize(5)
incrementing_counter = 0
angle_of_one_side_to_another=0
#Draw legs
while (incrementing_counter < legs):  
  spider.goto(0,20)
  spider.setheading(((angle_of_legs-20)*incrementing_counter)+angle_of_one_side_to_another)
  spider.forward(leg_length)
  incrementing_counter = incrementing_counter + 1
  if(incrementing_counter==4):
    angle_of_one_side_to_another+=90
spider.goto(0,0)
spider.pensize(10)
spider.pencolor("white")
spider.circle(8)
spider.penup()
spider.goto(12,12)
spider.pendown()
spider.circle(8)
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()