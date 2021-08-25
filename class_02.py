#!/usr/bin/env python3

class Student:
    def __init__(self,name):
        self.name = name

    def calculateAvg(self,math,japanese,english,science,society):
        self.avg = (math + japanese + english + science + society)/5
        print(self.avg)

    def judge(self):
        if self.avg >= 60:
            print("passed")
        else:
            print("failed")

a001 = Student("sato")
a001.calculateAvg(60,70,80,50,50)
a001.judge()
