import turtle

def draw_farn(length):
    if length > 2:
        turtle.forward(length)
        turtle.left(25)
        draw_farn(0.5 * length)
        turtle.right(35)
        draw_farn(0.7 * length)
        turtle.right(25)
        draw_farn(0.4 * length)
        turtle.left(35)
        turtle.forward(-length)
    else:
        turtle.forward(length)
        turtle.forward(-length)


def main():
    turtle.speed(0)  # Höchste Geschwindigkeit
    turtle.left(90)  # Stamm nach oben zeigen
    turtle.penup()
    turtle.goto(0, -200)  # Von unten nach oben zeichnen
    turtle.pendown()

    draw_farn(80)  # Stamm Länge = 100, Rekursionstiefe = 5

    turtle.getscreen().getcanvas().postscript(file='img/farn.eps')

    turtle.done()


if __name__ == "__main__":
    main()
