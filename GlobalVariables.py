from TimeToTime import *
from CoolComponents import *

class GlobalVariables:
    s ="clock"
    dictionary = {"Dying": TimeToTime(0, 0), "Sleep":TimeToTime(0,0), "Study":TimeToTime(0,0), "Socialize":TimeToTime(0,0), "Relax!":TimeToTime(0,0), "Exercise":TimeToTime(0,0)}
    activity_choosing_for = "Dying"
    temporal_start = 0
    temporal_end = 0
    start_or_end = ""
    start_am = True
    end_am = True