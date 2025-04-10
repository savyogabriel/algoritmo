""
import turtle

# Exercício 4.4: Desenhar uma flor
def petal(t, r, angle):
    for i in range(2):
        t.circle(r, angle)
        t.left(180 - angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.left(360 / n)

t = turtle.Turtle()
t.speed(0)
flower(t, 7, 100, 60)  # Flor com 7 pétalas
turtle.done()
