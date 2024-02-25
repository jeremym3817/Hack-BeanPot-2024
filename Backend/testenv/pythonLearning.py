from datetime import datetime
import math
import json
from abc import ABC, abstractclassmethod
# specialized constructors
class Utils:
    def __init__ (self):
        pass 
    def numberChecker(given, min, max):
            if min <= given <= max:
                return given
            else: 
                raise ValueError(f"{given} is not in the range: [{min}, {max}]")
    def yearRecom(classNameNumber):
            parts = classNameNumber.split()
            numeric_part = None 
            for part in parts: 
                if part.isdigit():
                    numeric_part = int(part)
                    break 
                #func value beings here: 
                 #year: 1 should only take req classes up to x <= 2800 
                if numeric_part <= 2800:
                    1 
                #year: 2 should only take req classes from 2800 <= x <= 3501
                elif 2800 <= numeric_part <= 3501:
                    2
                #year: 3 should only take req classes 3501 <= x <= 4501
                elif 3501 <= numeric_part <= 4501:
                    3
                #year: 4 should only take req classes 4501 <= x
                elif 4501 <= numeric_part:
                    4
    #basic class size estimator, needs API for specific values 
    def classSizeEst(currentYear):
            if currentYear == 1:
                "up to 150"
            elif currentYear == 2:
                "up to 100"
            elif currentYear == 3:
                "up to 30"
            elif currentYear == 4:
                "up to 20"
# main class on class information 
class AClass(ABC):
    def __init__(self, prof, difficulty, currYear, classNameNumber, start, end):
        self.prof = prof
        self.difficulty = Utils.numberChecker(difficulty, 0, 10)
        self.currYear = Utils.numberChecker(currYear, 1, 4)
        self.classNameNumber = classNameNumber
        self.start = start 
        self.end = end
    def classOverlap(start1, end1, start2, end2):
     #three different instances of a class overlapping another
     return (start1 <= start2 <= end1) or (start1 <= end2 <= end1) or (start2 <= start1 <= end2)
# requisite classes 
class ClassReq(AClass):
    def __init__ (self, prof, difficulty, currYear, classNameNumber, start, end):
        super().__init__(self, prof, difficulty, currYear, classNameNumber, start, end)
        self.yearRec = Utils.yearRecom(classNameNumber) 
        self.classSize = Utils.classSizeEst(currYear)
# elective classes
class ClassElec(AClass): 
    def __init__ (self, prof, difficulty, currYear, classNameNumber, start, end):
        super().__init__(self, prof, difficulty, currYear, classNameNumber, start, end)
        self.classSize = Utils.classSizeEst(currYear)
        #does not have a year recomended specialized constructor 
        '''
        time conflict in military time abs value of time1 - time2 cannot be 0 
        less diffculut  return less difficult class 
        10:30-12:00 
        '''
