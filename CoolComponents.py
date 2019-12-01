import time
import turtle

class CoolComponents:
    def __init__(self, pen):
        self.pen = pen
        self.pen.hideturtle()


    def createButton(self, x, y, width, height, text, textSize):
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.setheading(0)
        self.pen.down()
        actualWidth = len(text)*13
        for i in range(2):
            self.pen.forward(actualWidth)
            self.pen.left(90)
            self.pen.forward(height)
            self.pen.left(90)

        self.pen.up()
        self.pen.goto(x + 5, y + 3)
        self.pen.down()
        self.pen.write(text, font=('Courier', textSize, 'italic'))

    def createNumberButton(self, x, y, width, height, text, textSize):
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.setheading(0)
        self.pen.down()
        actualWidth = len(text)*13
        for i in range(2):
            self.pen.forward(26)
            self.pen.left(90)
            self.pen.forward(height)
            self.pen.left(90)

        self.pen.up()
        self.pen.goto(x + 5, y + 3)
        self.pen.down()
        self.pen.write(text, font=('Courier', textSize, 'italic'))

    def alterPen(self, size, color):
        self.pen.pensize(size)
        self.pen.color(color)

    def clear(self):
        self.pen.clear()