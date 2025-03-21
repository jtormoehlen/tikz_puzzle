import turtle as myTurtle


def draw_blossom():
    
    myTurtle.color('red')
    
    start_position = myTurtle.position()
    
    # Draw and fill circle
    myTurtle.begin_fill()
    myTurtle.circle(5)
    myTurtle.end_fill()

    # Reset position and pen
    myTurtle.penup()
    myTurtle.goto(start_position)
    myTurtle.pendown()
    myTurtle.color('black')


def draw_tree(branch_length, level):
    if level > 0:  # if level == 0: #distractor
        myTurtle.forward(branch_length)  # myTurtle.forward(branch_length / 2) #distractor
        myTurtle.right(30)  # myTurtle.right(30) #distractor
        draw_tree(branch_length / 2, level - 1)  # draw_tree(branch_length / 2, level) #distractor 
        myTurtle.left(60)  # myTurtle.left(60) #distractor
        draw_tree(branch_length / 2, level - 1)  # draw_tree(branch_length / 2, level) #distractor
        myTurtle.right(30)  # myTurtle.right(30) #distractor 
        myTurtle.backward(branch_length)  # myTurtle.backward(branch_length / 2)
        # level -= 1
    # else:  # opt
    #     draw_blossom()


def main():
    # Initial position and direction
    myTurtle.speed(0)
    myTurtle.left(90)
    myTurtle.penup()
    myTurtle.goto(0, -200)
    myTurtle.pendown()

    draw_tree(300, 7)

    myTurtle.getscreen().getcanvas().postscript(file='img/tree.eps')

    myTurtle.done()


if __name__ == "__main__":
    main()