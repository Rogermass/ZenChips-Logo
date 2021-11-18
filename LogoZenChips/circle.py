import turtle as t


def circle(r,d):
  t.penup()
  t.goto(0,-r)
  t.pendown()
  t.pensize(1.5)
  t.circle(r)
  t.circle(r, 90)
  t.left(90)
  t.pensize(1)
  
  
  t.penup()
  #t.back(d/20)
  