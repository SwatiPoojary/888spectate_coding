from enum import Enum


class Active(Enum):
    True_value = "TRUE"
    False_value = "FALSE"


class Event_Type(Enum):
    Preplay = "Preplay"
    Inplay = "Inplay"


class Status(Enum):
    Pending = "Pending"
    Started = "Started"
    Ended = "Ended"
    Cancelled = "Cancelled"


class Outcome(Enum):
    Unsettled = "Unsettled"
    Void = "Void"
    Lose = "Lose"
    Win = "Win"
