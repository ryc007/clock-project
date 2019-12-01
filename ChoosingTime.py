from CoolComponents import *
from GlobalVariables import *
class ChoosingTime:
    def __init__(self,wn):
        self.wn = wn
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.coolComponent = CoolComponents(self.pen)



    def draw_Activity_Start_Screen(self):
        self.wn.bgcolor("#19aa4e")
        self.coolComponent.alterPen(6, "Red")
        self.coolComponent.createNumberButton(-90, 60, 60, 30, "1", 12)
        self.coolComponent.createNumberButton(-60, 60, 60, 30, "2", 12)
        self.coolComponent.createNumberButton(-30, 60, 60, 30, "3", 12)
        self.coolComponent.createNumberButton(0, 60, 60, 30, "4", 12)
        self.coolComponent.createNumberButton(30, 60, 60, 30, "5", 12)
        self.coolComponent.createNumberButton(60, 60, 60, 30, "6", 12)

        self.coolComponent.createButton(-160, 0,60,30,"When will this activity start?",12)

        self.coolComponent.createNumberButton(-90, -60, 60, 30, "7", 12)
        self.coolComponent.createNumberButton(-60, -60, 60, 30, "8", 12)
        self.coolComponent.createNumberButton(-30, -60, 60, 30, "9", 12)
        self.coolComponent.createNumberButton(0, -60, 60, 30, "10", 12)
        self.coolComponent.createNumberButton(30, -60, 60, 30, "11", 12)
        self.coolComponent.createNumberButton(60, -60, 60, 30, "12", 12)

    def draw_Activity_End_Screen(self):
        self.wn.bgcolor("#19aa4e")
        self.coolComponent.alterPen(6, "Purple")
        self.coolComponent.createNumberButton(-90, 60, 60, 30, "1", 12)
        self.coolComponent.createNumberButton(-60, 60, 60, 30, "2", 12)
        self.coolComponent.createNumberButton(-30, 60, 60, 30, "3", 12)
        self.coolComponent.createNumberButton(0, 60, 60, 30, "4", 12)
        self.coolComponent.createNumberButton(30, 60, 60, 30, "5", 12)
        self.coolComponent.createNumberButton(60, 60, 60, 30, "6", 12)

        self.coolComponent.createButton(-160, 0,60,30,"When will this activity End?",12)

        self.coolComponent.createNumberButton(-90, -60, 60, 30, "7", 12)
        self.coolComponent.createNumberButton(-60, -60, 60, 30, "8", 12)
        self.coolComponent.createNumberButton(-30, -60, 60, 30, "9", 12)
        self.coolComponent.createNumberButton(0, -60, 60, 30, "10", 12)
        self.coolComponent.createNumberButton(30, -60, 60, 30, "11", 12)
        self.coolComponent.createNumberButton(60, -60, 60, 30, "12", 12)

    def draw_AM_or_PM(self):
        self.coolComponent.createButton(-90, 60, 60, 30, " AM ", 12)

        self.coolComponent.createButton(-100, 0,60,30,"AM or PM?",12)

        self.coolComponent.createButton(-90, -60, 60, 30, " PM ", 12)

    def clear(self):
        self.pen.clear()

    def clickTest(self, x, y):
        print("HI")
        if (GlobalVariables.s == "choosingStartTime"):
            GlobalVariables.start_or_end = "start"
            if (x > -90 and x < -60 and y > 60 and y < 90):
                print("SLEPP")
                GlobalVariables.temporal_start = 1
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > -60 and x < -30 and y > 60 and y < 90):
                GlobalVariables.temporal_start = 2
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > -30 and x < 0 and y > 60 and y < 90):
                GlobalVariables.temporal_start = 3
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 0 and x < 30  and y > 60 and y < 90):
                GlobalVariables.temporal_start = 4
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 30 and x < 60 and y > 60 and y < 90):
                GlobalVariables.temporal_start = 5
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 60 and x < 90 and y > 60 and y < 90):
                GlobalVariables.temporal_start = 6
                GlobalVariables.s = "draw_AM_or_PM"

            if (x > -90 and x < -60 and y > -60 and y < -30):
                print("SLEPP")
                GlobalVariables.temporal_start = 7
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > -60 and x < -30 and y > -60 and y < -30):
                GlobalVariables.temporal_start = 8
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > -30 and x < 0 and y > -60 and y < -30):
                GlobalVariables.temporal_start = 9
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 0 and x < 30  and y > -60 and y < -30):
                GlobalVariables.temporal_start = 10
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 30 and x < 60 and y > -60 and y < -30):
                GlobalVariables.temporal_start = 11
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 60 and x < 90 and y > -60 and y < -30):
                GlobalVariables.temporal_start = 12
                GlobalVariables.s = "draw_AM_or_PM"

        elif(GlobalVariables.s =="draw_AM_or_PM" and GlobalVariables.start_or_end == "start"):
            print("was on the AM fool")
            if (x > -90 and x < -60 and y > 60 and y < 90):
                print("SLEPP")
                GlobalVariables.start_am = True
                GlobalVariables.s = "draw_Activity_End_Screen"
            if (x > -90 and x < -60 and y > -60 and y < -30):
                GlobalVariables.start_am = False
                GlobalVariables.s = "draw_Activity_End_Screen"

        elif (GlobalVariables.s == "draw_Activity_End_Screen"):
            GlobalVariables.start_or_end = "end"
            if (x > -90 and x < -60 and y > 60 and y < 90):
                print("SLEPP")
                GlobalVariables.temporal_end = 1
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > -60 and x < -30 and y > 60 and y < 90):
                GlobalVariables.temporal_end = 2
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > -30 and x < 0 and y > 60 and y < 90):
                GlobalVariables.temporal_end = 3
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 0 and x < 30  and y > 60 and y < 90):
                GlobalVariables.temporal_end = 4
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 30 and x < 60 and y > 60 and y < 90):
                GlobalVariables.temporal_end = 5
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 60 and x < 90 and y > 60 and y < 90):
                GlobalVariables.temporal_end = 6
                GlobalVariables.s = "draw_AM_or_PM"

            if (x > -90 and x < -60 and y > -60 and y < -30):
                print("SLEPP")
                GlobalVariables.temporal_end = 7
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > -60 and x < -30 and y > -60 and y < -30):
                GlobalVariables.temporal_end = 8
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > -30 and x < 0 and y > -60 and y < -30):
                GlobalVariables.temporal_end = 9
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 0 and x < 30  and y > -60 and y < -30):
                GlobalVariables.temporal_end = 10
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 30 and x < 60 and y > -60 and y < -30):
                GlobalVariables.temporal_end = 11
                GlobalVariables.s = "draw_AM_or_PM"
            if (x > 60 and x < 90 and y > -60 and y < -30):
                GlobalVariables.temporal_end = 12
                GlobalVariables.s = "draw_AM_or_PM"

        elif(GlobalVariables.s =="draw_AM_or_PM" and GlobalVariables.start_or_end == "end"):
            print("was on the PM fool")
            if (x > -90 and x < -60 and y > 60 and y < 90):
                print("SLEPP")
                GlobalVariables.end_am = True
                GlobalVariables.s = "clock"
                self.time_to_dict()
            if (x > -90 and x < -60 and y > -60 and y < -30):
                GlobalVariables.end_am = False
                GlobalVariables.s = "clock"
                self.time_to_dict()


    def time_to_dict(self):
        event = GlobalVariables.dictionary[GlobalVariables.activity_choosing_for]
        event.set_start(GlobalVariables.temporal_start)
        event.set_end(GlobalVariables.temporal_end)
        if (not GlobalVariables.start_am):
            event.set_start(GlobalVariables.temporal_start+12)

        if (not GlobalVariables.end_am):
            event.set_end(GlobalVariables.temporal_end+12)
    #Make a consolidate method thing