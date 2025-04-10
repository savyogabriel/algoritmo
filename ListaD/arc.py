
import turtle

def arc(t, r, angle):
    arc_length = 2 * 3.1416 * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

t = turtle.Turtle()
t.speed(1)
arc(t, 100, 90)
turtle.done()
