from turtle import *
import random as r

speed(50000)
degrees()

x = 0
while x <=255:
     color("#00"+format(x,"02x")+"ff")
     fd(100+x*2)
     rt(122)
     x+=1

ht()