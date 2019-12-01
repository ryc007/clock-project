import time
import turtle
from AnalogClock import *
from ChoosingActivityMode import *
from Schedule import *
from ChoosingTime import *
from GlobalVariables import *

#This is a string that will signify the 'MODE' the screen will show
s = "clock"



wn=turtle.Screen()
wn.bgcolor("#99cccc")
wn.setup(width = 400, height = 320)
wn.title("Team 22's clock!")
wn.tracer(0)

analogClock = AnalogClock(wn)
activityMode = ChoosingActivity(wn)
choosingTime = ChoosingTime(wn)
#print(time.time())
#pen withour ink

#The pen that will draw the clock


#Our text styles
#style = ('Courier', 30, 'italic')


def clickTest(x,y):
    print(x,y)
    global s
    print(s)
    s = "schedule"



#_______________________
#-----This will be the schedule screen stuff
#________________________________________________________



schedule = Schedule()

while True:
    if GlobalVariables.s=="clock":
        analogClock.draw_clock()
        turtle.onscreenclick(analogClock.clickTest)
        turtle.listen()
        s = analogClock.getMode()
        wn.update()
        time.sleep(1)
        analogClock.clear()
        print(GlobalVariables.s)
        print(GlobalVariables.dictionary["Sleep"].get_end())

    if GlobalVariables.s=="schedule":
        activityMode.draw_Scedule_Screen()
        wn.update()
        time.sleep(1)
        activityMode.clear()
        turtle.onscreenclick(activityMode.clickTest)
        schedule.laughingOnTheOutside()

    if GlobalVariables.s=="choosingStartTime":
        print("CHOOSINGTIME!")
        choosingTime.draw_Activity_Start_Screen()
        wn.update()
        time.sleep(1)
        choosingTime.clear()
        turtle.onscreenclick(choosingTime.clickTest)
        schedule.laughingOnTheOutside()

    if GlobalVariables.s=="draw_AM_or_PM":
        print("draw_AM_or_PM!")
        choosingTime.draw_AM_or_PM()
        wn.update()
        time.sleep(1)
        choosingTime.clear()
        turtle.onscreenclick(choosingTime.clickTest)
        schedule.laughingOnTheOutside()

    if GlobalVariables.s=="draw_Activity_End_Screen":
        print("CHOOSINGTIME!")
        choosingTime.draw_Activity_End_Screen()
        wn.update()
        time.sleep(1)
        choosingTime.clear()
        turtle.onscreenclick(choosingTime.clickTest)
        schedule.laughingOnTheOutside()


wn.mainloop()

