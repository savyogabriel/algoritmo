""
import turtle

# Exercício 4.6: Desenhar gráfico de torta
def pie(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(90)
        t.circle(length, angle)
        t.lt(90)
        t.fd(length)
        t.lt(180)

t = turtle.Turtle()
t.speed(1)
pie(t, 8, 100)  # Gráfico com 8 fatias
turtle.done()
