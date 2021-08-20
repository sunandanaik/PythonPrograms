import turtle
import time
import random

delay=0.1
#Simple Snake Game
#set up the screen
wn=turtle.Screen()
wn.title("Snake Game Turtle")
wn.bgcolor("orange")
wn.setup(width=600,height=600)
wn.tracer(0) # turns off the animation on screen

#Snake head
head=turtle.Turtle()
head.speed(0) # animation speed of turtle module
head.shape("square")
head.color("black")
head.penup() # so it doesnt draw anything
head.goto(0,0)
head.direction="stop"

#Snake Food
food=turtle.Turtle()
food.speed(0) # animation speed of turtle module
food.shape("circle")
food.color("red")
food.penup() # so it doesnt draw anything
food.goto(0,100)

#when head touched food, we add segments
segments=[]

#Score Variables 
score =0
high_score=0

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0  High Score : 0", align="center", font=("Courier",24,"normal"))

#Functions
#to control snake movement on keypress
def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction!="up":
        head.direction="down"

def go_left():
    if head.direction!="right":
        head.direction="left"

def go_right():
    if head.direction!="left":
        head.direction="right"

#to move snake
def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y + 20) #it moves up 20px each time
    if head.direction == "down":
        y=head.ycor()
        head.sety(y - 20) #it moves down 20px each time
    if head.direction == "left":
        x=head.xcor()
        head.setx(x - 20) #it moves left 20px each time
    if head.direction == "right":
        x=head.xcor()
        head.setx(x + 20) #it moves right 20px each time

#keyboard bindings(to connect key press with particular event)
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"z")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"s")


#Main Game Loop
#it repeats over and over again
while True:
    # everytime in loop it updates the screen
    wn.update()

    #Check for 4 border collision
    if head.xcor() >290 or head.xcor() <-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #hide the segments
        for seg in segments:
            seg.goto(1000,1000)
        
        #Clear the segments list
        segments.clear()

        #Reset delay
        delay=0.1
        
        #Reset the score display
        score=0
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score, high_score),align="center",font=("Courier",24))



    #Check for a collision with the food
    if head.distance(food) < 20:
        #to move food to random position
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #create a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -= 0.01

        #Increase the Score
        score +=10
        if score > high_score:
            high_score=score
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score, high_score),align="center",font=("Courier",24))

    #Move the end segments first in reverse order
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)
    
    #Move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)


    #function calling
    move()

    #Check for head collision with the body segments
    for seg in segments:
        if seg.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #hide the segments
            for seg in segments:
                seg.goto(1000,1000)
            
            #Clear the segments list
            segments.clear()
            #Reset delay
            delay=0.1
            #Reset the score display
            score=0
            pen.clear()
            pen.write("Score : {} High Score : {}".format(score, high_score),align="center",font=("Courier",24))


    time.sleep(delay)

wn.mainloop() # keeps the window open for us