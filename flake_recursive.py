import turtle

def draw_koch(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        draw_koch(length / 3, level - 1)
        turtle.left(45)
        draw_koch(length / 3, level - 1)
        turtle.right(90)
        draw_koch(length / 3, level - 1)
        turtle.left(45)
        draw_koch(length / 3, level - 1)

def draw_flake(length, level):
    draw_koch(length, level)
    turtle.right(120)
    draw_koch(length, level)
    turtle.right(120)
    draw_koch(length, level)

def main():
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()

    draw_flake(300, 3)

    turtle.getscreen().getcanvas().postscript(file='img/tree.eps')

    turtle.done()

if __name__ == "__main__":
    main()
