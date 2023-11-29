import turtle

import calendar


def draw_month(t, year, month, start_x, start_y, const):

   # Get the first weekday of the month and number of days in the month

   first_weekday, num_days = calendar.monthrange(year, month)


   # Drawing the month name/title

   t.penup()

   t.goto(start_x, start_y)

   t.pendown()

   for i in range(2):

       t.forward(const * 7)

       t.right(90)

       t.forward(const)

       t.right(90)

   t.penup()

   t.goto(start_x + 10, start_y - 15)  # Adjust the position for month title

   t.pendown()

   t.write(monthname[month], font=("Arial", 10, "normal"))

   t.penup()


   # Drawing the weekdays headers

   t.goto(start_x, start_y - const)

   for day in weekdays[1:]:

       t.pendown()

       t.forward(const)

       t.penup()

       t.backward(const)

       t.right(90)

       t.forward(const)

       t.write(day, align="center", font=("Arial", 8, "normal"))

       t.backward(const)

       t.left(90)

       t.forward(const)


   # Drawing the grid for the days and placing day numbers

   day_num = 1

   for i in range(6):

       for j in range(7):

           t.goto(start_x + j*const, start_y - const*(i+2))

           t.setheading(0)

           t.pendown()

           for k in range(4):

               t.forward(const)

               t.right(90)

           t.penup()

           if i == 0 and j < first_weekday:

               continue

           elif day_num <= num_days:

               # Move the turtle to the top-left corner of the cell to write the day number

               t.goto(start_x + j*const + 3, start_y - const*(i+2) - 15)

               t.write(day_num, font=("Arial", 8, "normal"))

               day_num += 1


# Constants

year = 2023  # Example year

const = 20  # Size of each day's box

monthname = ["", "January", "February", "March", "April", "May", "June",

            "July", "August", "September", "October", "November", "December"]

weekdays = ["", "M", "T", "W", "T", "F", "S", "S"]  # Weekdays starting with Monday


# Initializing the Turtle

t = turtle.Turtle()

t.speed(0)


# Adjust the screen size if needed

screen = turtle.Screen()

screen.setup(width=1500, height=1000)


# Drawing each month

horizontal_spacing = 300

vertical_spacing = 220

for month in range(1, 13):

   draw_month(t, year, month, -500 + horizontal_spacing * ((month - 1) % 4), 300 - vertical_spacing * ((month - 1) // 4), const)


# Hide the turtle and complete

t.hideturtle()

turtle.done()