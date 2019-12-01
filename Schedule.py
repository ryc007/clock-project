from TimeToTime import *
from CoolComponents import *
class Schedule:

    def __init__(self):
        self.pen = turtle.Turtle()
        self.coolComponent = CoolComponents(self.pen)
        self.dictionary = {"Dying": TimeToTime(0, 0), "Sleep":TimeToTime(0,0), "Study":TimeToTime(0,0), "Socialize":TimeToTime(0,0), "Relax!":TimeToTime(0,0), "Exercise":TimeToTime(0,0)}

    def laughingOnTheOutside(self):
        print(self.dictionary["Dying"].get_end())

