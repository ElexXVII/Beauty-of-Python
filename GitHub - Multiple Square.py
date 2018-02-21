from turtle import *
import random as r

speed(50000)
degrees()

#Placer la turtle pour avoir un carré centré
penup()
setx(-100)
sety(100)
pendown()

#Création des carrés
x = 0
while x <=255:

     #Rouge-Jaune
     color("#ff"+format(x,"02x")+"00")

     #Bleu-Cyan
     #color("#0"+format(x,"02x")+"ff")
     
     fd(200+x*1.2)
     rt(91)
     x+=1

#Rendre la Turtle invisible
ht()
