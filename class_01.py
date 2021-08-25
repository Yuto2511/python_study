#!/usr/bin/env python3

class Student:
    def __init__(self):
        self.name = ""

    def avg(self,math,english):
        print((math + english)/2)

a001 = Student()
a001.name = "sato"
print(a001.name)

a002 = Student()
a002.name = "kato"
print(a002.name)
