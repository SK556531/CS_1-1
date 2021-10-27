#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0

1="blue"
2="black"
3="gray"
# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  t = floor % 3
  if (t==1):
    painter.color(1)
  if (t==2):
    painter.color(2)
  if (t==0):
    painter.color(3)
  y = y + 5 # location of next floor
  floor = floor + 1
   
  #draw the floor
  painter.pendown()
  painter.forward(50)
  s = floor % 63
  if (s==21):
    x=-50
    y=-150
    1="red"
    2="yellow"
    3="green"
  if (s==42):
    x=50
    y=-150


wn = trtl.Screen()
wn.mainloop()