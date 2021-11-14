import turtle as t
import math



def gridvertical(r,d,h):

  for y in range(20):
    dif = r-((h)*y)
    t.penup()
    t.forward(h)
    t.pendown()
    length = 2*math.sqrt((r**2)-(dif**2));
    
    t.left(90)
    
    t.forward(length/2)
    t.right(180)
    t.forward(length)
    t.left(180)
    t.forward(length/2)
    t.right(90)