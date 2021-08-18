# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:35:36 2021

@author: Marie
"""

import turtle
from random import randint

x = 100
y = 100
steg = 10
turtle.tracer(0)

penn = turtle.Turtle()
for y in range(-300, 300, steg):
    for x in range(-300, 300, steg):
        mynt = randint(0, 1)
        
        penn.penup()
        if mynt == 0:
            penn.goto(x, y)
            penn.pendown()
            penn.goto(x+steg, y+steg)
        else:
            penn.goto(x, y+steg)
            penn.pendown()
            penn.goto(x+steg, y)
ts = turtle.getscreen()
ts.getcanvas().postscript(file="10print.eps")            
            
turtle.update()
turtle.done()
turtle.bye()
