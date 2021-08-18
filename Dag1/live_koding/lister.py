# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 08:15:21 2021

@author: Marie
"""

navn1 = "Marie"
navn2 = "Eina"
navn3 = "julie"

kule_kodere = ["Marie", "Eina", 
               "julie", "Pernilla"]

print(kule_kodere)
print(kule_kodere[-2])
kule_kodere[2] = "Julie"
print(kule_kodere)

kule_kodere.append("Wanda")
print(kule_kodere)

for navn in kule_kodere:
    print("Hei", navn)
print("Hade!")

for tall in range(100):
    print(tall)

