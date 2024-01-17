import turtle
t = turtle.Turtle()
def click(x,y):
  print("\N{crocodile}")

def main():
  s = t.Screen()
  s.onclick(click)

  s.mainloop()

main()

## Colour change Background

import turtle 
import random 
  
# global colors 
col = ['red', 'yellow', 'green', 'blue', 
       'white', 'black', 'orange', 'pink'] 
  
# method to call on screen click 
  
  
def fxn(x, y): 
    global col 
    ind = random.randint(0, 7) 
      
    # set screen color randomly 
    sc.bgcolor(col[ind]) 
  
# set screen 
sc = turtle.Screen() 
sc.setup(400, 300) 
  
# call method on screen click 
turtle.onscreenclick(fxn)






## Draw

# import package 
import turtle 
  
  
# screen object 
wn = turtle.Screen() 
  
# method to perform action 
def fxn(x, y): 
  turtle.goto(x, y) 
  turtle.write(str(x)+","+str(y)) 
  
# onclick action  
wn.onclick(fxn) 
wn.mainloop()


## Working BG Image

import turtle

# You first create the screen
win = turtle.Screen()

# Set the screen dimensions (only if you want)
win.setup(width=800, height=600)

# Set the background
win.bgpic("triassic-banner with gif format.gif")

# Continue with your turtle drawing or just keep the window open
turtle.mainloop()



## NOW FOR MOUSE ACTION
## tkinter used for mouse use in calender
import tkinter as tk
from tkinter import *
from turtle import Screen, Turtle

screen = Screen()
T = Turtle("turtle")
T.speed(-1)

def dragging(x, y):  # These parameters will be the mouse position
    T.penup()
    T.ondrag(None)
    T.setheading(t.towards(x, y))
    T.goto(x, y)
    T.ondrag(dragging)

def clickRight():
    t.clear()

def main():  # This will run the program
    turtle.listen()
    
    T.ondrag(dragging)  # When we drag the turtle object call dragging
    turtle.onscreenclick(clickRight, 3)

    screen.mainloop()  # This will continue running main() 

main()