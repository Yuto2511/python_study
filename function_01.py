#!/usr/bin/env python3

def say_hello():
    print("hello,world!")

def say_hello_02(greeting):
    print(greeting)

def add(num01,num02):
    print(num01 + num02)

def add_02(num01,num02):
    return(num01 + num02)

def average(num01,num02,num03):
    return(num01 + num02 + num03) / 3

say_hello()

say_hello_02("hello,world")
hello = say_hello_02
hello("Good Morning")

add(1,2)

print(add(1,2))

add_result =add(1,2)
print(add_result)

print(average(9,4,2))
