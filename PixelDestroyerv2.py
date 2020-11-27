import turtle
import math
import time
import random


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Pixel Destroyer")

border_pen      = turtle.Turtle()
player_one      = turtle.Turtle()
player_two      = turtle.Turtle()
bullet_plyone   = turtle.Turtle()
bullet_plytwo   = turtle.Turtle()
enemy           = turtle.Turtle()
ghost           = turtle.Turtle()#this is a object that must walk on the map for game not to crush
                                 #the walk code is in the while True section and it needs to be there


turtle.register_shape("playertwo.gif")
turtle.register_shape("playerone.gif")


ghost.setposition(0,0)
ghost.shape("circle")
ghost.color("green")
ghost.penup()
ghost.hideturtle()


border_pen.setposition(-300, -300)
border_pen.color("white")
border_pen.penup()
border_pen.speed(2)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


player_one.setposition(0, 250)
player_one.shape("playerone.gif")
player_one.penup()


player_two.setposition(0, -250)
player_two.shape("playertwo.gif")
player_two.penup()


bullet_plyone.color("green")
bullet_plyone.speed(0)
bullet_plyone.penup()
bullet_plyone.pensize(3)
bullet_plyone.setheading(270)
bullet_plyone.hideturtle()
bullet_plyone.setposition(0, 250)


bullet_plytwo.color("red")
bullet_plytwo.speed(0)
bullet_plytwo.penup()
bullet_plytwo.pensize(3)
bullet_plytwo.setheading(90)
bullet_plytwo.hideturtle()
bullet_plytwo.setposition(0, -250 )


player_one_speed     = 15
player_two_speed     = 15
bullet_plyone_speed  = 30
bullet_plytwo_speed  = 30
ghost_speed          = 2

number_of_enemies = 30
enemies = []


for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    y=random.randint(-200,200)
    x=random.randint(-279,279)
    enemy.setposition(x,y)
    enemy.shape("circle")
    enemy.color("gray")
    enemy.penup()


bullet_plyone_state = "ready"
bullet_plytwo_state = "ready"


def move_plyone_left():
    x = player_one.xcor()
    x -= player_one_speed
    if x < - 280:
        x = -280
    player_one.setx(x)
def move_plyone_right():
    x = player_one.xcor()
    x += player_one_speed
    if x > 280:
        x = 280
    player_one.setx(x)
def move_plytwo_left():
    x = player_two.xcor()
    x -= player_two_speed
    if x < -280:
       x = -280
    player_two.setx(x)
def move_plytwo_right():
    x = player_two.xcor()
    x += player_two_speed
    if x > 280:
       x = 280
    player_two.setx(x)
def fire_plyone():
    global bullet_plyone_state
    if bullet_plyone_state == "ready":
     bullet_plyone_state = "fire"
     x = player_one.xcor()
     y = player_one.ycor() - 10
     bullet_plyone.setposition(x,y)
     bullet_plyone.showturtle()
def fire_plytwo():
   global bullet_plytwo_state
   if bullet_plytwo_state == "ready":
       bullet_plytwo_state = "fire"
       x = player_two.xcor()
       y = player_two.ycor() +10
       bullet_plytwo.setposition(x, y)
       bullet_plytwo.showturtle()
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


turtle.listen()
turtle.onkey(fire_plyone, "s")
turtle.onkey(move_plyone_left, "a")
turtle.onkey(move_plyone_right, "d")
turtle.onkey(move_plytwo_left, "Left")
turtle.onkey(move_plytwo_right, "Right")
turtle.onkey(fire_plytwo,"Down")




while True:

   x = ghost.xcor()
   x += ghost_speed
   ghost.setx(x)
   if x > 280:
        ghost_speed *= -1
   if x < -280:
        ghost_speed *= -1


   if isCollision(bullet_plyone, player_two):
       player_two.hideturtle()
       player_two.setposition(1000, 1000)
       enemy.hideturtle()
       turtle.color("magenta")
       turtle.hideturtle()
       turtle.write("Game Over",  move=False, align="Center", font=("Arial", 30, "bold"))
       time.sleep(2)
       turtle.clear()
       turtle.write("Player One Winner", move=False, align="Center", font=("Arial", 30, "bold"))


   if isCollision(bullet_plytwo, player_one):
       player_one.hideturtle()
       player_one.setposition(1000, 1000)
       enemy.hideturtle()
       turtle.color("magenta")
       turtle.hideturtle()
       turtle.write("Game Over", move=False, align="Center", font=("Arial", 30, "bold"))
       time.sleep(2)
       turtle.clear()
       turtle.write("Player Two Winner", move=False, align="Center", font=("Arial", 30, "bold"))


   if bullet_plyone_state == "fire":
       y = bullet_plyone.ycor()
       y -= bullet_plyone_speed
       bullet_plyone.sety(y)

   if bullet_plyone.ycor() < -300:
      bullet_plyone.hideturtle()
      bullet_plyone_state = "ready"

   if bullet_plytwo_state == "fire":
       y = bullet_plytwo.ycor()
       y += bullet_plytwo_speed
       bullet_plytwo.sety(y)
   if bullet_plytwo.ycor() > 300:
       bullet_plytwo.hideturtle()
       bullet_plytwo_state = "ready"


   for enemy in enemies:
       if isCollision(bullet_plyone, enemy):
           if enemy.isvisible():
               a = 1
               b = 1
               c = a + b
               bullet_plyone.hideturtle()
               bullet_plyone.setposition(300, 300)
           enemy.hideturtle()

       if isCollision(bullet_plytwo, enemy):
            if enemy.isvisible():
                a = 1
                b = 1
                c = a + b
                bullet_plyone.hideturtle()
                bullet_plytwo.setposition(300, 300)
            enemy.hideturtle()
       if isCollision(bullet_plyone,player_two):
            enemy.hideturtle()
       if isCollision(bullet_plytwo,player_one):
            enemy.hideturtle()


turtle.mainloop()

