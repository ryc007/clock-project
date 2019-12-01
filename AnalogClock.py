import time
import turtle
import datetime
from CoolComponents import *
from GlobalVariables import *

class AnalogClock:
    def __init__(self,wn):
        self.wn = wn
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.pensize(5)
        self.style = ('Courier', 30, 'italic')
        self.style2 = ('Courier', 10, 'italic')
        self.coolComponent = CoolComponents(self.pen)
        self.string = "clock"

    def computeTime(self):
        self.hour = float(time.strftime("%I"))
        self.minute = int(time.strftime("%M"))
        self.second = int(time.strftime("%S"))
        self.twentyfour_hour = float(time.strftime("%H"))

    def draw_analog(self):
        self.computeTime()
        self.wn.bgcolor("#99cccc")
        # draw the circle
        self.pen.pensize(5)
        self.pen.up()
        self.pen.goto(0, 120)
        self.pen.setheading(180)
        self.pen.color("#ffcdef")
        self.pen.pendown()
        self.pen.circle(120)

        self.pen.penup()
        self.pen.goto(0, 0)
        # pen.pendown()
        # pen.fd(2)
        # pen.penup()
        self.pen.setheading(90)

        for _ in range(12):
            self.pen.fd(100)
            self.pen.pendown()
            self.pen.fd(20)
            self.pen.penup()
            self.pen.goto(0, 0)
            self.pen.rt(30)

        # hour
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.color("#d7f2c8")
        self.pen.setheading(90)
        angle = (self.hour / 12) * 360 + self.minute / 2
        self.pen.rt(angle)
        self.pen.pensize(4)
        self.pen.pendown()
        self.pen.fd(60)

        # minute
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.color("#f5acae")
        self.pen.setheading(90)
        angle = (self.minute / 60) * 360 + self.second/10
        self.pen.rt(angle)
        self.pen.pensize(3)
        self.pen.pendown()
        self.pen.fd(90)

        # second
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.color("white")
        self.pen.setheading(90)
        angle = (self.second / 60) * 360
        self.pen.rt(angle)
        self.pen.pensize(3)
        self.pen.pendown()
        self.pen.fd(30)
        self.pen.hideturtle()

    def clear(self):
        self.pen.clear()

    def draw_digital(self):

        ht = (time.strftime("%I"))
        mt = (time.strftime("%M"))
        dt = (time.strftime("%p"))
        time_h_m = ht + ':' + mt
        time_s_d = dt
        self.pen.penup()
        self.pen.color("#ffffff")
        self.pen.goto(0,20)
        self.pen.write(time_h_m,font=self.style, align = 'center')
        self.pen.goto(0,10)
        self.pen.write(time_s_d, font = self.style2, align = 'center')
        self.pen.hideturtle()

    def draw_activity(self):
        self.pen.penup()
        self.pen.goto(0,-100)
        for activity, time_period in GlobalVariables.dictionary.items():
            print(activity)
            if (self.twentyfour_hour>=time_period.get_start() and self.twentyfour_hour<time_period.get_end()):
                self.pen.write(activity, font=self.style, align='center')
                break
        #if (self.twentyfour_hour == )

    def draw_Activity_Button(self):
        self.coolComponent.createButton(80,100,50,20,"Choose an Activity!",10)

    def clickTest(self, x, y):
        print(x, y)
        if (x>100 and x<150 and y>80 and y<120):

            self.string = "schedule"
            GlobalVariables.s = "schedule"
        else:
            self.string = "clock"
            GlobalVariables.s = "clock"

    def getMode(self):
        return self.string



    def draw_clock(self):
        self.draw_digital()
        self.draw_analog()
        self.draw_Activity_Button()
        self.draw_activity()
