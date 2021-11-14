import grid, circle, name, triangle

import turtle as t 

t.speed(12)

print("-----Recommended: Radius value = 100, Text Scale = 10, Triangles = 60-----")
print("")

r = int(input("Enter Circle Radius: "))
d = r*2
h = d/20

circle.circle(r,d)
grid.gridvertical(r,d,h)


name.drawname()

s1 = int(input("Enter First Triangle Side Length: "))
triangle.triangle(s1, h, r)

s2 = int(input("Enter Second Triangle Side Length: "))
triangle.triangle2(s2, h, r)

t.hideturtle()

