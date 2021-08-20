# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:42:30 2021

@author: Marie
"""


import matplotlib.pyplot as plt

mnd = ["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"]
tmp = [-10, -5.5, 0.3, 4.4, 10.4, 12.8, 16.2, 15.3, 10.1, 8.7, 4.2, -1.3]

print(mnd)
print(tmp)
plt.figure(figsize=(13, 6))
plt.plot(mnd, tmp, "--o", color="red")
print("hei")
plt.xlabel("Tid i måneder")
plt.ylabel("Temperatur i celcius")
plt.savefig("f.png")
plt.savefig("f.pdf")
plt.show()