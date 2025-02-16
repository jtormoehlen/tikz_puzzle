import turtle


def draw_blossom():
    
    turtle.color('red')
    
    start_position = turtle.position()
    
    # Draw and fill circle
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

    # Reset position and pen
    turtle.penup()
    turtle.goto(start_position)
    turtle.pendown()
    turtle.color('black')


def draw_tree(branch_length, level):
    if level > 0:
        # Stem
        turtle.forward(branch_length)

        # Branch Right
        turtle.right(45)
        draw_tree(branch_length / 2, level - 1)

        # Branch Left
        turtle.left(90)
        draw_tree(branch_length / 2, level - 1)

        # Reset
        turtle.right(45)
        turtle.backward(branch_length)
    else:
        draw_blossom()


def main():
    # Initial position and direction
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()

    draw_tree(300, 7)

    turtle.getscreen().getcanvas().postscript(file='img/tree.eps')

    turtle.done()


if __name__ == "__main__":
    main()