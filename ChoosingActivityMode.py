from CoolComponents import *
from GlobalVariables import *
class ChoosingActivity:
    def __init__(self,wn):
        self.wn = wn
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.coolComponent = CoolComponents(self.pen)



    def draw_Scedule_Screen(self):
        self.wn.bgcolor("#59cde2")
        self.coolComponent.alterPen(6, "Blue")
        self.coolComponent.createButton(-130, 90, 60, 30, "What would you like to do?", 12)
        self.coolComponent.createButton(-130, 50, 60, 30, "Sleep", 12)
        self.coolComponent.createButton(-30, 50, 60, 30, "Study", 12)
        self.coolComponent.createButton(-50, -10, 60, 30, "Socialize", 12)
        self.coolComponent.createButton(-130, -80, 70, 30, "Relax!", 12)
        self.coolComponent.createButton(-30, -80, 100, 30, "Exercise", 12)


    def clear(self):
        self.pen.clear()

    def how_wide_boxes(self,stringgy):
        return len(stringgy)*13

    def clickTest(self, x, y):
        print("HEY")
        if (x>-130 and x<-65 and y>50 and y<80):
            print("SLEPP")
            GlobalVariables.s = "choosingStartTime"
            GlobalVariables.activity_choosing_for = "Sleep"
        if (x>-30 and x<(-30+self.how_wide_boxes("Study")) and y>50 and y<80):
            GlobalVariables.s = "choosingStartTime"
            GlobalVariables.activity_choosing_for = "Study"
        if (x>-50 and x<-50+self.how_wide_boxes("Socialize") and y>-10 and y<20):
            GlobalVariables.s = "choosingStartTime"
            GlobalVariables.activity_choosing_for = "Socialize"
        if (x>-130 and x<-130+self.how_wide_boxes("Relax!") and y>-80 and y<-50):
            GlobalVariables.s = "choosingStartTime"
            GlobalVariables.activity_choosing_for = "Relax!"
        if (x>-30 and x<-30+self.how_wide_boxes("Exercise") and y>-80 and y<-50):
            GlobalVariables.s = "choosingStartTime"
            GlobalVariables.activity_choosing_for = "Exercise"
        print (GlobalVariables.s)
        print (self.how_wide_boxes("Sleep"))
        print(x,y)
