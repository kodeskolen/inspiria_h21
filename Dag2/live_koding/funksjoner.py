# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:01:51 2021

@author: Marie
"""


print("Hei")

def f(x):
    y = x**2 + x - 1
    return y

print(f(3))
tall = 10
print(f(tall))

def hils_på(navn):
    print("Hei", navn)
    print("Hvordan går det?")
    
hils_på("Eina")    

for navn in ["Marie", "Eina"]:
    hils_på(navn)
hils_på(["Marie", "Eina"])
print(hils_på("Marie"))