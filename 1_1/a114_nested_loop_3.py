import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

painter.speed(0)

x=-200
y=200
t=0

while (x < 200):
  y=200
  while (y > -200):
    painter.goto(x,y)
    painter.color("orange")
    if (t==0):
      painter.color("purple")
    painter.stamp()
    y = y - 50
  x=x+50
  t=t+1

wn = trtl.Screen()
wn.mainloop()