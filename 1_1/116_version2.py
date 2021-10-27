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
angle_of_legs = 380 / legs
spider.pensize(5)
incrementing_counter = 0
#Draw legs
while (incrementing_counter < legs):
  spider.goto(0,0)
  spider.setheading(angle_of_legs*incrementing_counter)
  spider.forward(leg_length)
  incrementing_counter = incrementing_counter + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()