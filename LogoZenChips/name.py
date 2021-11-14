import turtle as t

def drawname():
  s = int(input("Enter Text Scale: "))
  
  t.penup()
  t.goto(0,(-2.2*s))
  t.pendown()
  t.pensize(3)
  t.fillcolor("white")
  t.begin_fill()
  t.forward(7*s)
  t.backward(14*s)
  t.right(90)
  t.forward(4.4*s)
  t.left(90)
  t.forward(14*s)
  t.left(90)
  t.forward(4.4*s)
  t.end_fill()
  t.pensize(2)
  
  
  
  c = str(input("Enter Text Color: "))

  t.penup()
  t.goto(0,(-1.7*s))
  t.pendown()
  t.color(c)
  t.write("ZenChips", align="center", font=("Comic Sans MS",2*s, "normal"))
  t.setheading(180)

