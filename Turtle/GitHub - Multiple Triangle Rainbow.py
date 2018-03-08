from turtle import *
import random as r
from math import *

speed(50000)
#degrees()

#Plot of triangle
x = 0
r = 0
while x <=255*5:

     if r==0: #Rouge - Jaune
          color("#ff"+format(x,"02x")+"00")
          #print("#ff"+format(x,"02x")+"00",r)
     if r==0 and x==254:
          x+=1
          r=1

     if r==1: #Jaune - Vert
          color("#"+format(255-x%255,"02x")+"ff00")
          #print("#"+format(255-x%255,"02x")+"ff00",r)
     if r==1 and x%255==254:
          x+=1
          r=2

     if r==2: #Vert - Cyan
          color("#00ff"+format(x%255,"02x"))
          #print("#00ff"+format(x%255,"02x"),r)
     if r==2 and x%255==254:
          x+=1
          r=3

     if r==3: #Cyan - Bleu
          color("#00"+format(255-x%255,"02x")+"ff")
          #print("#00"+format(255-x%255,"02x")+"ff",r)
     if r==3 and x%255==254:
          x+=1
          r=4

     if r==4: #Bleu - Violet
          color("#"+format(x%255,"02x")+"00ff")
          #print("#"+format(x%255,"02x")+"00ff",r)

     x+=2

     fd(50+(floor(x/4)+1)*1.7)
     rt(119.5)

ht()
