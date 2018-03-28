from turtle import *
import random as r
from math import *

#Speed of the turtle
speed(50000)

#Stop drawing
penup()
pensize(20)

#Save each point of each step
p=[[0,-300]]
q=[]

n = 7
m = 3

#Execute n times
for i in range(1,n):
     #Color variation
     color("#ff"+format(int(i/n*255),"02x")+"00")
		 
     #for each point of the list
     for j in p:
		 
          #Go to this point
          goto(j[0],j[1])
					
          #Draw m times a branch
          for k in range(3):
               
	       #Set a centered random angle
               seth(0)
               seth(r.randint(0,180))
							 
	       #Draw the branch
               pendown()
               pensize(20/i)
               fd(200/i)
               penup()
							 
	       #Add the point we left to continue drawing on the next step
               q.append([xcor(),ycor()])
							 
	       #Back to the center to draw a new branch
               bk(200/i)
							 
     #Set the next points where we will start as the list we filled
     p=list(q)
     #Clear the list we filled to fill it with the new points for the new step
     q.clear()


