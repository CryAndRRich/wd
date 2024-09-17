import math, time, turtle 
import colorsys as cs

pen = turtle.Turtle() 
screen = turtle.Screen()
pen.speed(0)
pen.hideturtle()

def draw_flower():
    screen.bgcolor("black")
    h = 0 
    for _ in range(9):
        for j in range(14):
            c = cs.hsv_to_rgb(h, 1, 1)
            pen.color(c)
            h += 0.005
            pen.rt(90)
            pen.circle(150 - j * 6, 90)
            pen.lt(90)
            pen.circle(150 - j * 6, 90)
            pen.rt(180)
        pen.circle(20, 360 / 9)
    pen.color('black')

def draw_H(x, y):
    pen.fillcolor('white')
    pen.pu()
    pen.goto(x, y)
    pen.pd()

    pen.begin_fill()
    for _ in range(2):
        pen.fd(30)
        pen.rt(90)
        pen.fd(50)
        pen.lt(90)
        pen.fd(30)
        pen.lt(90)
        pen.fd(50)
        pen.rt(90)
        pen.fd(30)
        pen.rt(90)
        pen.fd(120)
        pen.rt(90)
    pen.end_fill()

def draw_A(x, y):
    pen.fillcolor('white')
    pen.pu()
    pen.goto(x, y)
    pen.pd()

    pen.begin_fill()
    pen.goto(x + 30, y + 120)
    pen.fd(40)
    pen.goto(x + 100, y)
    pen.rt(180)
    pen.fd(30)
    pen.goto(x + 60, y + 50) 
    pen.fd(20)
    pen.goto(x + 30, y) 
    pen.fd(30)
    pen.end_fill()

    pen.fillcolor('black')
    pen.pu()
    pen.goto(x + 60, y + 70) 
    pen.pd()
    pen.begin_fill()
    pen.fd(20)
    pen.goto(x + 50, y + 100) 
    pen.goto(x + 60, y + 70) 
    pen.end_fill()
    pen.rt(180)

def draw_P(x, y):
    pen.fillcolor('white')
    pen.pu()
    pen.goto(x, y)
    pen.pd()

    pen.begin_fill()
    pen.fd(30)
    pen.lt(90)
    pen.fd(60)
    pen.rt(90)
    pen.fd(20)
    pen.circle(30, 180)
    pen.fd(50)
    pen.lt(90)
    pen.fd(120)
    pen.end_fill()

    pen.fillcolor('black')
    pen.pu()
    pen.goto(x + 30, y + 100)
    pen.pd()

    pen.begin_fill()
    pen.fd(20)
    pen.lt(90)
    pen.fd(10)
    pen.circle(10, 180)
    pen.fd(10)
    pen.rt(180)
    pen.end_fill()

def draw_Y(x, y):
    pen.fillcolor('white')
    pen.pu()
    pen.goto(x, y)
    pen.pd()

    pen.begin_fill()
    pen.fd(30)
    pen.lt(90)
    pen.fd(60)
    pen.goto(x + 60, y + 120)
    pen.lt(90)
    pen.fd(30)
    pen.goto(x + 15, y + 80)
    pen.goto(x, y + 120)
    pen.fd(30)
    pen.goto(x, y + 60)
    pen.lt(90)
    pen.fd(60)
    pen.end_fill()

def draw_B(x, y):
    pen.fillcolor('white')
    pen.pu()
    pen.goto(x, y) 
    pen.pd()

    pen.begin_fill()
    pen.fd(120)
    pen.lt(90)
    pen.fd(50)
    for i in range(2):
        pen.circle(35 - 10 * i, 180)
        pen.rt(180)
    pen.goto(x, y)
    pen.end_fill()

    for i in range(2):
        pen.fillcolor('black')
        pen.pu()
        pen.goto(x + 30, y - 35 - 65 * i)
        pen.pd()

        pen.begin_fill()
        pen.fd(10 + 5 * i)
        pen.circle(10 + 5 * i, 180)
        pen.fd(10 + 5 * i)
        pen.rt(180)
        pen.end_fill()

def draw_I(x, y):
    pen.fillcolor('white')
    pen.pu()
    pen.goto(x, y)
    pen.pd()

    pen.begin_fill()
    for _ in range(2):
        pen.fd(30)
        pen.rt(90)
        pen.fd(120)
        pen.rt(90)
    pen.end_fill()

def draw_R(x, y):
    pen.fillcolor('white')
    pen.pu()
    pen.goto(x, y)
    pen.pd()

    pen.begin_fill()
    pen.fd(30)
    pen.lt(90)
    pen.fd(60)
    pen.rt(90)
    pen.goto(x + 50, y)
    pen.fd(30)
    pen.goto(x + 60, y + 60)
    pen.circle(30, 180)
    pen.fd(61)
    pen.lt(90)
    pen.fd(120)
    pen.end_fill()

    pen.fillcolor('black')
    pen.pu()
    pen.goto(x + 30, y + 100)
    pen.pd()

    pen.begin_fill()
    pen.fd(20)
    pen.lt(90)
    pen.fd(10)
    pen.circle(10, 180)
    pen.fd(10)
    pen.rt(180)
    pen.end_fill()

def draw_T(x, y):
    pen.fillcolor('white')
    pen.pu()
    pen.goto(x, y)
    pen.pd()

    pen.begin_fill()
    pen.fd(90)
    pen.rt(90)
    pen.fd(30)
    pen.rt(90)
    pen.fd(30)
    pen.lt(90)
    pen.fd(90)
    pen.rt(90)
    pen.fd(30)
    pen.rt(90)
    pen.fd(90)
    pen.lt(90)
    pen.fd(30)
    pen.rt(90)
    pen.fd(30)
    pen.end_fill()
    pen.rt(90)

def draw_D(x, y):
    pen.color('white')
    pen.pu()
    pen.goto(x, y)
    pen.pd()

    pen.begin_fill()
    pen.fd(30)
    pen.circle(60, 180)
    pen.fd(30)
    pen.rt(90)
    pen.goto(x, y)
    pen.end_fill()

    pen.color('black')
    pen.pu()
    pen.goto(x + 30, y + 30)
    pen.pd()

    pen.begin_fill()
    pen.fd(60)
    pen.rt(90)
    pen.circle(-30, 180)
    pen.end_fill()
    pen.rt(180)

def draw_exclamation(x, y):
    pen.fillcolor('white')
    pen.pu()
    pen.goto(x, y)
    pen.rt(90)
    pen.pd()

    pen.begin_fill()
    for _ in range(2):
        pen.fd(30)
        pen.rt(90)
        pen.fd(120)
        pen.rt(90)
    pen.end_fill()
    
    pen.fillcolor('black')
    pen.pu()
    pen.goto(x, y + 40)
    pen.lt(90)
    pen.pd()

    pen.begin_fill()
    for _ in range(2):
        pen.fd(20)
        pen.rt(90)
        pen.fd(30)
        pen.rt(90)
    pen.end_fill()

def draw_heart():
    def heart_a(k):
        return 15*math.sin(k)**3
    def heart_b(k):
        return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)
    screen.bgcolor("black")
    for i in range(6000):
        pen.goto(heart_a(i) * 20,heart_b(i) * 20 + 45)
        for _ in range(5):
            pen.color("red")
        pen.goto(0,0)

if __name__ == '__main__':
    draw_flower()
    time.sleep(1)
    draw_H(-270, 220)
    draw_A(-153, 100)
    draw_P(-30, 100)
    draw_P(70, 100)
    draw_Y(190, 100)
    draw_B(-260, 60)
    draw_I(-143, 60)
    draw_R(-75, -60)
    draw_T(30, 60)
    draw_H(150, 60)
    draw_D(-170, -225)
    draw_A(-70, -225)
    draw_Y(60, -225)
    draw_exclamation(160, -225)
    time.sleep(2)
    screen.clear()
    draw_heart()

turtle.done() 
