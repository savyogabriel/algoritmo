""
import turtle

# Exercício 4.3: Desenhar polígonos regulares
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

t = turtle.Turtle()
t.speed(1)
polygon(t, 6, 100)  # Hexágono com lados de 100 pixels
turtle.done()
