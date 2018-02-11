from turtle import *
import random as r

speed(50000)
degrees()

for i in range(360):
		 
		 # Random length of each line
     n = r.randint(7,20)
     
		 # Choose a color for each part of eacg line and draw each one
     for i in range(n):
		 
          x = format(r.randint(0,255),"02x")
					
          color("#ff"+x+"00") # Red to Yellow
					color("#00"+x+"ff") # Blue to Cyan
					
          forward(20)
		 
		 # Replace turtle on the center to draw next line
     penup()
     left(1)
     setx(0)
     sety(0)
     pendown()
