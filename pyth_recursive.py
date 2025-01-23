import turtle

def draw_pyth(length):
    if (length > 4):
      turtle.forward(length)
      turtle.left(150)
      # Großes Katheten-Quadrat zeichnen
      k1 = length * 0.5 * 3 ** 0.5
      turtle.forward(k1)
      turtle.right(90)
      turtle.forward(k1)
      turtle.right(90)
      draw_pyth(k1)
      turtle.right(90)
      turtle.forward(k1)
      turtle.right(90)
      turtle.forward(k1)
      turtle.left(90)
      # Kleines Katheten-Quadrat zeichnen
      k2 = length * 0.5
      turtle.forward(k2)
      turtle.right(90)
      turtle.forward(k2)
      turtle.right(90)
      draw_pyth(k2)
      turtle.right(90)
      turtle.forward(k2)
      turtle.right(90)
      turtle.forward(k2)
      # Nochmal(!) Hypothenuse zeichnen !!
      turtle.left(120)
      turtle.forward(length)
    else:
      turtle.forward(length)


def main():
    turtle.speed(0)  # Höchste Geschwindigkeit
    turtle.left(90)  # Stamm nach oben zeigen
    turtle.penup()
    turtle.goto(0, -200)  # Von unten nach oben zeichnen
    turtle.pendown()

    draw_pyth(50)  # Stamm Länge = 100, Rekursionstiefe = 5

    turtle.getscreen().getcanvas().postscript(file='img/pyth.eps')

    turtle.done()


if __name__ == "__main__":
    main()
