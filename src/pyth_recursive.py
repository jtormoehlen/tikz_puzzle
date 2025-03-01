import turtle

def draw_pyth(length):
    if (length > 4):
      turtle.forward(length)
      turtle.left(150)

      # Great leg square
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

      # Small leg square
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

      # Hypotenuse again (!)
      turtle.left(120)
      turtle.forward(length)
    else:
      turtle.forward(length)


def main():
    # Initial position and direction
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()

    draw_pyth(50)

    turtle.getscreen().getcanvas().postscript(file='img/pyth.eps')

    turtle.done()


if __name__ == "__main__":
    main()
