import turtle

# window=turtle.Screen()
# pen=turtle.Turtle()
# 
# pen.forward(200)  #drawing a line with the pen
# turtle.done()

# window=turtle.Screen()
# pen=turtle.Turtle()
# 
# for i in range(4):
#     pen.forward(400)
#     pen.right(90)  # or pen.left(90) to draw a square
# turtle.done()

# window=turtle.Screen()
# pen=turtle.Turtle()
# 
# for i in range(3):
#     pen.forward(400)
#     if i!=2:      #if you dont want to change the direction of pen arrow.
#        pen.left(120)  # to draw a triangle
# turtle.done()

# window=turtle.Screen()
# pen=turtle.Turtle()
# 
# for i in range(6):
#     pen.forward(200)
#     
#     pen.right(144)  # to draw a star
# turtle.done()

window=turtle.Screen()
pen=turtle.Turtle()
length=200
for i in range(40):
    pen.forward(length)
    pen.left(90) # to draw square spiral pattern
    length-=5
turtle.done()



