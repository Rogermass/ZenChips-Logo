import turtle as t
import math as m

def triangle(a,b,c):
  t.penup()
  t.goto(-(a/2),(-(c * 30) / 100))
  t.pendown()
  t.color("black")
  t.right(60)
  t.backward(a)
  t.left(120)
  t.backward(a)
  t.right(60)
  t.forward(a)
  
  z = ((b/m.sin(m.radians(60))))
  x = m.floor(a/z)
  for i in range(1,x+1):
    if i % 2 != 0:

      t.left(120)
      t.forward(z)
      t.left(60)
      t.backward((m.sin(30)) * (a-(i*z)))
    
    else: 

      t.right(120)
      t.forward(z)
      t.right(60)
      t.backward((m.sin(30) * (a-(i*z))))

def triangle2(a,b,c):
  t.penup()
  t.goto(a/2,((c * 30) / 100))
  t.pendown()
  t.setheading(0)
  t.color("black")
  t.left(120)
  t.forward(a)
  t.left(120)
  t.forward(a)
  t.left(120)
  t.forward(a)
  

  z = ((b/m.sin(m.radians(60))))
  x = m.floor(a/z)

  for i in range(1, x+1):
    if i % 2 != 0: 
      t.left(120)
      t.forward(z)
      t.left(60)
      t.backward((m.sin(30) * (a-(i*z))))
      
    else: 
        t.right(120)
        t.forward(z)
        t.right(60)
        t.backward((m.sin(30) * (a-(i*z))))
        