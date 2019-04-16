import turtle
import time
import random

#variables
delay = 0.1
segments = []
score = 0
high_score = 0

# init functions

def init_screen(wn):
    wn.title("Snake")
    wn.bgcolor("black")
    wn.setup(width=600,height=600)
    wn.tracer(0)

def init_head(head):
    head.speed(0)
    head.shape("circle")
    head.color("white")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

def init_food(food):
    food.speed(0)
    food.shape("square")
    food.color("gray")
    food.penup()
    food.goto(100,0)

def init_keyboard_listener(wn):
    wn.listen()
    wn.onkeypress(move_up,"Up")
    wn.onkeypress(move_down,"Down")
    wn.onkeypress(move_left,"Left")
    wn.onkeypress(move_right,"Right")

def create_new_segment():
    new_seg = turtle.Turtle()
    new_seg.shape("square")
    new_seg.color("grey")
    new_seg.speed(0)
    new_seg.penup()
    return new_seg

## move functions

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"


def move_left():
    if head.direction != "right":
        head.direction = "left"


def move_right():
    if head.direction != "left":
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

def attach_head_to_segments(head, segments):
    for index in range(len(segments)-1,0,-1):
            segments[index].goto(
                segments[index-1].xcor(),
                segments[index-1].ycor()
            )

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

### reset functions

def reset(segments):
    time.sleep(1)
    head.goto(0,0)
    head.direction ='stop'
    
    for s in segments:
        s.goto(1000,1000)
    
    segments.clear()
    
def reset_score():
    return 0

def reset_game(segments, pen, score, high_score, delay):
    reset(segments)
    score = reset_score()
    write_score(pen, score, high_score)
    delay = 0.1
    return score, delay

#### write score functions

def write_score(pen, score, high_score): 
    pen.speed(0)
    pen.shape('square')
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.clear()
    pen.write("Score: {}  Highscore: {}".format(score, high_score), align="center", font=('Courier', 24, "normal" ))

##### Main

wn = turtle.Screen()
init_screen(wn)

head = turtle.Turtle()
init_head(head)

food = turtle.Turtle()
init_food(food)

pen = turtle.Turtle()
write_score(pen, score , high_score)

init_keyboard_listener(wn)


while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        score, delay = reset_game(segments, pen, score, high_score, delay)

    for segment in segments:
        if segment.distance(head) < 20:
           score, delay = reset_game(segments, pen, score, high_score, delay)


    if head.distance(food) < 20 :
        food.goto(
            random.randint(-300,300),
            random.randint(-300,300)
        )       

        segments.append(create_new_segment())

        score += 10
        if score > high_score:
            high_score = score
        write_score(pen, score, high_score)
        delay -= 0.001
        
    attach_head_to_segments(head, segments)   
    move()
    time.sleep(delay)

wn.mainloop()
