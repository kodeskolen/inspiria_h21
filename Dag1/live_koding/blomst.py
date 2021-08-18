# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 08:38:08 2021

@author: Marie
"""
from turtle import *

lengde = 100
color("#cc27bb")
farge_liste = ["#59023B", "#BF045B", "#BF3B91", "#F28DCF", "white"]
speed("fastest")
for farge in farge_liste:
    color(farge)
    for rotasjon in range(8):
        begin_fill()
        for side in range(4):
            forward(lengde)
            right(90)
        end_fill()
        right(45)
    lengde = lengde*0.8
    right(45*0.5)

done()
bye()