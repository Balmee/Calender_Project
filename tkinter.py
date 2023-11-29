import tkinter as tk
from tkinter import *




# PRACTICE
import turtle 
wn = turtle.Screen() 
# method to perform action 
def fxn(x, y): 
  turtle.goto(x, y) 
  turtle.write(str(x)+","+str(y)) 
# onclick action  
wn.onclick(fxn) 
wn.mainloop()








turtle.onclick(fxn, btn=1, add=None)





# import package 
import turtle 
  
  
# method to action 
def fxn(x,y): 
      
    # some motion 
    turtle.right(90) 
    turtle.forward(100) 
  
# turtle speed to slowest 
turtle.speed(1) 
  
# motion 
turtle.fd(100) 
  
# allow user to click  
# for some action 
turtle.onclick(fxn)



turtle.ondrag(turtle.goto)






