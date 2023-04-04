# import programs
import turtle 
import time 
import random 

score = 0 
high_score = 0
delay = 0.1
 
# creating a window screen 
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
# width & height set
wn.setup(width = 600, height = 600)
wn.tracer(0)

# snakehead
head = turtle.Turtle()
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

# food 
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))

# assigning key directions 
def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

# asssigning keyboard (wasd)
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []


# gameplay 
while True:
    wn.update()

    #check collision with border 
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        food.shape("square")
        food.color("red")
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
 
        # adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
        
        # 50 message 
        if high_score == 50:
            pen.clear()
            pen.color("deep pink")
            pen.write ("Score : 50! Happy Birthday Char!".format(score, high_score),
            align = "center", font=("candara", 26, "bold"))
            time.sleep(3)

            #re-setter
            pen.clear()
            pen.color("white")
            pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

        # 100 message 
        if high_score == 100:
            pen.clear()
            pen.color("deep pink")
            pen.write ("Score : 100! You're 22 now..".format(score, high_score),
            align = "center", font=("candara", 26, "bold"))
            time.sleep(3)

            #re-setter
            pen.clear()
            pen.color("white")
            pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

        # 150 message 
        if high_score == 150:
            pen.clear()
            pen.color("deep pink")
            pen.write ("How disgustingly old..".format(score, high_score),
            align = "center", font=("candara", 28, "bold"))
            time.sleep(3)

            #re-setter
            pen.clear()
            pen.color("white")
            pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

        # 200 message 
        if high_score == 200:
            pen.clear()
            pen.color("deep pink")
            pen.write ("Eww.. kinda gross..".format(score, high_score),
            align = "center", font=("candara", 30, "bold"))
            time.sleep(3)

            #re-setter
            pen.clear()
            pen.color("white")
            pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

        # 250 message 
        if high_score == 250:
            pen.clear()
            pen.color("red")
            pen.write ("Jk, love you - HBD <3 ".format (score, high_score),
            align = "center", font=("candara", 26, "bold"))
            time.sleep(10)

            #re-setter
            pen.clear()
            pen.color("white")
            pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

        # easter egg message
        if high_score == 420:
            wn.bgcolor("white")
            pen.clear()
            pen.color("green")
            pen.write ("Score : Spark it up birthday girl!".format (
                score, high_score), align ="center", font=("candara", 26, "bold"))
            new_segment.color("green") 
            head.color("green")


    # checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            head.colors = "blue"
            head.shapes = "square"
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
 
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
 
wn.mainloop()
