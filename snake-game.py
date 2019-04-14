import turtle
import time
import random

#Screen
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

#snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("gray")
food.penup()
food.goto(100,0)

#variables
delay = 0.1
segments = []


def move_up():
    head.direction = "up"

def move_down():
    head.direction = "down"


def move_left():
    head.direction = "left"


def move_right():
    head.direction = "right"


def move():
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)


    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)


    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)


wn.listen()
wn.onkeypress(move_up,"Up")
wn.onkeypress(move_down,"Down")
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")

while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction ='stop'
        
        for s in segments:
            s.goto(1000,1000)
        
        segments.clear()

    if head.distance(food) < 20 :
        food.goto(
            random.randint(-300,300),
            random.randint(-300,300)
        )       

        new_seg = turtle.Turtle()
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.speed(0)
        new_seg.penup()
        segments.append(new_seg)
    
    #for last segment to follow previous segment
    for index in range(len(segments)-1,0,-1):
        segments[index].goto(
            segments[index-1].xcor(),
            segments[index-1].ycor()
        )

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    

    move()

    time.sleep(delay)



wn.mainloop()
