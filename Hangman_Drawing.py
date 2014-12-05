import turtle

# Creation of the Turtle
Hangman = turtle.Turtle()
Hangman.pensize(10)

# Creation of the base
Hangman.up()
Hangman.goto(100, -200)
Hangman.down()
Hangman.forward(125)
Hangman.backward(250)
Hangman.goto(100, -200)
Hangman.left(90)
Hangman.forward(450)
Hangman.left(90)
Hangman.forward(175)
Hangman.left(90)
Hangman.forward(40)
Hangman.right(90)

# Creation of the Head
Hangman.circle(50, steps = 100)
Hangman.left(90)

# Creation of the body
Hangman.up()
Hangman.goto(-75, 110)
Hangman.down()
Hangman.forward(150)

# Creation of first leg
Hangman.left(30)
Hangman.forward(125)
Hangman.goto(-75, -40)

# Creation of second leg
Hangman.right(60)
Hangman.forward(125)

# Creation of first arm
Hangman.up()
Hangman.goto(-75, 70)
Hangman.down()
Hangman.left(80)
Hangman.forward(100)

# Creation of second arm
Hangman.goto(-75, 70)
Hangman.right(100)
Hangman.forward(100)
input()