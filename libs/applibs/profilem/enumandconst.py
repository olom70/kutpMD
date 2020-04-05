from enum import Enum

class ActivityFactor(Enum):
    SEDENTARY = 1
    LIGHTLYACTIVE = 2
    MODERATELYACTIVE = 3
    ACTIVE = 4
    VIGOROUS = 5
    VIGOROUSLYACTIVE = 6

class RmrDates(Enum):
    A1918 = 1918
    A1984 = 1984
    A1990 = 1990

class MetricChoice(Enum):
    ISO = 0
    IMPERIAL = 1

class Gender(Enum):
    FEMALE = 0
    MALE = 1
