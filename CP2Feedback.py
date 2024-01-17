## To make sure the program runs properly, clear terminal history so all code works at once

import turtle

## THIS IS FOR THE BACKGROUND TO BECOME VISIBLE AS AN IMAGE: remember tpo convert into a GIF format via msPaint to be used

# You first create the screen
win = turtle.Screen()

# Set the screen dimensions (only if you want)
win.setup(width=800, height=600)

# Set the background
win.bgpic("triassic-banner with gif format.gif")






## MAIN CALENDER BODY, TO PRODUCE THE CALENDER OVERLAY

import calendar

def draw_month(p, year, month, start_x, start_y, const):

   # Get the first weekday of the month and number of days in the month

   first_weekday, num_days = calendar.monthrange(year, month)


   # Drawing the month name/title

   p.penup()
   
   p.goto(start_x, start_y)

   p.pendown()

   for i in range(2):

       p.forward(const * 7)

       p.right(90)

       p.forward(const)

       p.right(90)

   p.penup()

   p.goto(start_x + 10, start_y - 15)  # Adjust the position for month title

   p.pendown()

   p.write(monthname[month], font=("Arial", 10, "bold"))

   p.penup()


   # Drawing the weekdays headers

   p.goto(start_x, start_y - const)

   for day in weekdays[1:]:

       p.pendown()

       p.forward(const)

       p.penup()

       p.backward(const)

       p.right(90)

       p.forward(const)

       p.write(day, align="center", font=("Arial", 9, "bold"))

       p.backward(const)

       p.left(90)

       p.forward(const)


   # Drawing the grid for the days and placing day numbers

   day_num = 1

   for i in range(6):

       for j in range(7):

           p.goto(start_x + j*const, start_y - const*(i+2))

           p.setheading(0)

           p.pendown()

           for k in range(4):

               p.forward(const)

               p.right(90)

           p.penup()

           if i == 0 and j < first_weekday:

               continue

           elif day_num <= num_days:

               # Move the turtle to the top-left corner of the cell to write the day number

               p.goto(start_x + j*const + 3, start_y - const*(i+2) - 15)

               p.write(day_num, font=("Arial", 8, "bold"))

               day_num += 1


# CONSTANTS (what will always stay the same)

year = 2024  # Year

const = 20  # Size of each day's box

monthname = ["", "January", "February", "March", "April", "May", "June",

            "July", "August", "September", "October", "November", "December"]

weekdays = ["", "M", "T", "W", "T", "F", "S", "S"]  # Weekdays starting with Monday


# Initializing the Turtle

p = turtle.Turtle()

p.speed("fastest")


# Adjust the screen size if needed

screen = turtle.Screen()

screen.setup(width=1500, height=1000)


# Drawing each month

p.width(3)

horizontal_spacing = 350

vertical_spacing = 180

for month in range(1, 13):

   draw_month(p, year, month, -625 + horizontal_spacing * ((month - 1) % 4), 450 - vertical_spacing * ((month - 1) // 4), const)   # Controls the placement of month grids


# Hide the turtle and complete

p.hideturtle()

turtle.done()