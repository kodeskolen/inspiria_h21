# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:26:30 2021

@author: Marie
"""


import turtle

def tegn_stjerne(skilpadde, 
                 antall_stråler, 
                 strålelengde):
    
    for stråle in range(antall_stråler):
        skilpadde.forward(strålelengde)
        x, y = skilpadde.position()
        print(x, y)
        skilpadde.backward(strålelengde)
        skilpadde.right(360/antall_stråler)
        
        
per = turtle.Turtle()

tegn_stjerne(per, 8, 50)
per.penup()
per.goto(100, 100)
per.pendown()
tegn_stjerne(per, 10, 10)


turtle.done()
turtle.bye()
