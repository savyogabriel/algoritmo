""
import turtle

# Exercício 4.5: Desenhar uma espiral
def spiral(t, n, length=3, a=0.1, b=0.0002):
    theta = 0.0
    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)
        t.lt(dtheta)
        theta += dtheta

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
spiral(t, n=1000)  # Espiral com 1000 segmentos
turtle.done()
