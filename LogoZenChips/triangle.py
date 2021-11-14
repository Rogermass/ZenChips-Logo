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

  x = m.floor(a/b)
  for i in range(1,x):
    if i % 2 != 0:

      t.left(120)
      t.forward(b)
      t.left(60)
      t.backward((m.sin(30) * (a-(i*b))))
    
    else: 

      t.right(120)
      t.forward(b)
      t.right(60)
      t.backward((m.sin(30) * (a-(i*b))))

def triangle2(a,b,c):
  t.penup()
  t.goto(a/2,((c * 30) / 100))
  t.pendown()
  t.color("black")
  t.left(120)
  t.forward(a)
  t.left(120)
  t.forward(a)
  t.left(120)
  t.forward(a)
  

  z = m.floor(a/b)

  for i in range(1, z):
    if i % 2 != 0: 
      t.left(120)
      t.forward(b)
      t.left(60)
      t.backward((m.sin(30) * (a-(i*b))))
      
    else: 
        t.right(120)
        t.forward(b)
        t.right(60)
        t.backward((m.sin(30) * (a-(i*b))))
        