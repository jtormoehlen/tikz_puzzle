import turtle


def draw_blossom():
    # Turtle initialisieren
    
    # Farbe setzen
    turtle.color('red')
    
    # Ausgangsposition speichern
    start_position = turtle.position()
    
    # Kreis zeichnen
    turtle.begin_fill()
    turtle.circle(5)  # Zeichnet einen Kreis mit einem Radius von 20
    turtle.end_fill()

    # Zurück zur Ausgangsposition
    turtle.penup()  # Stift anheben, um nichts zu zeichnen
    turtle.goto(start_position)  # Zurück zur Ausgangsposition
    turtle.pendown()  # Stift wieder absenken, falls man weiter zeichnen möchte
    turtle.color('black')


def draw_tree(branch_length, level):
    if level > 0:
        # Zeichne den Stamm
        turtle.forward(branch_length)

        # Rechts abzweigen
        turtle.right(45)
        draw_tree(branch_length / 2, level - 1)

        # Links abzweigen
        turtle.left(90)
        draw_tree(branch_length / 2, level - 1)

        # Zurück zum vorherigen Zustand
        turtle.right(45)
        # draw_tree(branch_length / 2, level - 1)

        turtle.backward(branch_length)
    else:
        draw_blossom()


def main():
    turtle.speed(0)  # Höchste Geschwindigkeit
    turtle.left(90)  # Stamm nach oben zeigen
    turtle.penup()
    turtle.goto(0, -200)  # Von unten nach oben zeichnen
    turtle.pendown()

    draw_tree(300, 7)  # Stamm Länge = 100, Rekursionstiefe = 5

    turtle.getscreen().getcanvas().postscript(file='img/tree.eps')

    turtle.done()


if __name__ == "__main__":
    main()