import turtle
import random

screen = turtle.Screen()
screen.bgcolor("#777764")
screen.title("Catch The Turtle")
grid_size = 10
turtle_list = []
game_over = False
#Score
score_turtle = turtle.Turtle()
score = 0

#countdown
countdown_turtle = turtle.Turtle()
def setup_score_turtle():

    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.color("dark blue")
    #score_turtle.setposition(0,200)
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setposition(0,y)
    score_turtle.write("Score: 0 ", font=("Arial", 16, "normal"))

def make_turtle(x,y):
    turtle_instance = turtle.Turtle()

    def handle_click(x,y):
        global score
        score +=1
        score_turtle.clear() #ekrandaki score değerini sil
        score_turtle.write("Score: {} ".format(score), font=("Arial", 16, "normal")) #yeni score değerini yaz

    turtle_instance.onclick(handle_click)
    turtle_instance.penup()
    turtle_instance.shape("turtle") #turtle şekli kaplumbağa olsun
    turtle_instance.shapesize(2,2) #ekrandaki kaplumbağa boyutu
    turtle_instance.goto(x * grid_size,y * grid_size)
    turtle_list.append(turtle_instance)

'''
make_turtle(-20,20)
make_turtle(-10,20)
make_turtle(0,20)
make_turtle(10,20)
make_turtle(20,20)

make_turtle(-20,10)
make_turtle(-10,10)
make_turtle(0,10)
make_turtle(10,10)
make_turtle(20,10)

make_turtle(-20,0)
make_turtle(-10,0)
make_turtle(0,0)
make_turtle(10,0)
make_turtle(20,0)

make_turtle(-20,-10)
make_turtle(-10,-10)
make_turtle(0,-10)
make_turtle(10,-10)
make_turtle(20,-10)
'''
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]
def setup_turtles():
    for x in x_coordinates:
     for y in y_coordinates:
         make_turtle(x,y)

def hide_turtles():
    for turtle_instance in turtle_list:
        turtle_instance.hideturtle()

def show_turtles_randomly():
    if not game_over: #game_over false ise bunları yap, true ise buraya hiç girmez.
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500) #recursive fonksiyon-kendisi içinde çağırılma


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.color("dark blue")
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setposition(0, y-30)

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write("Time: {} ".format(time), font=("Arial", 16, "normal"))
        screen.ontimer(lambda: countdown(time-1),1000) #lambda şeklinde kullanmasanda hata vermez

    else:
        game_over =True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!",move=False, align="center",font=("Arial", 16, "normal"))

turtle.tracer(0) #turtle takip etmeyi bırakır.

setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
countdown(10)

turtle.tracer(1) #takip etmeyi başlatır.

turtle.mainloop()
