import turtle
import calendar
import pygame     # used -3 -m pip install pygame /to get use of package



# Setting the background image
def setup_background():
    win = turtle.Screen()
    win.setup(width=800, height=400)
    win.bgpic('triassic-banner with gif format.gif')



# Function to play music for Calender being drawn
# Initialize pygame mixer, load and play the sound file when the window opens
def setup_playsound():
    pygame.mixer.init() 
    pygame.mixer.music.load("20_-_metal_gear_solid_main_theme_(1997_e3_edit).mp3")
    pygame.mixer.music.play()



# Drawing the Calendar
def draw_month(p, year, month, start_x, start_y, const, monthname, weekdays):
    first_weekday, num_days = calendar.monthrange(year, month)
    p.penup()
    p.goto(start_x, start_y)
    p.pendown()

    for i in range(2):
        p.forward(const * 7)
        p.right(90)
        p.forward(const)
        p.right(90)

    # Drawing the month name/title
    p.penup()
    p.goto(start_x + 10, start_y - 22)
    p.pendown()
    p.pencolor("#FF00FF")
    p.write(monthname[month], font=("Arial", 14, "bold"))
    p.pencolor("black")
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
        p.pencolor("#FFFF00")
        p.write(day, align="center", font=("Arial", 11, "bold"))
        p.pencolor("black")
        p.backward(const)
        p.left(90)
        p.forward(const)

    # Drawing the grid for the days and placing day numbers
    day_num = 1
    for i in range(6):
        for j in range(7):
            p.goto(start_x + j * const, start_y - const * (i + 2))
            p.setheading(0)
            p.pendown()
            for k in range(4):
                p.forward(const)
                p.right(90)
            p.penup()
            if i == 0 and j < first_weekday:
                continue
            elif day_num <= num_days:
                p.goto(start_x + j * const + 3, start_y - const * (i + 2) - 19)
                p.pencolor("#0000FF")
                p.write(day_num, font=("Arial", 9, "bold"))
                p.pencolor("black")
                day_num += 1



# Initializing and drawing calendar
def setup_calendar():
    year = 2024
    const = 23
    monthname = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    weekdays = ["", "M", "T", "W", "T", "F", "S", "S"]

    p = turtle.Turtle()
    p.speed("fastest")
    screen = turtle.Screen()
    screen.setup(width=1500, height=1000)
    p.width(3)

    horizontal_spacing = 350
    vertical_spacing = 230
    for month in range(1, 13):
        draw_month(p, year, month, -625 + horizontal_spacing * ((month - 1) % 4), 440 - vertical_spacing * ((month - 1) // 4), const, monthname, weekdays)

    p.hideturtle()



# Handling mouse interactions
def setup_mouse_interactions():
    t = turtle.Turtle("turtle")
    t.pencolor("#00FF00")
    screen = turtle.Screen()

    def dragging(x, y):
        t.penup()
        t.ondrag(None)
        t.setheading(t.towards(x, y))
        t.goto(x, y)
        t.ondrag(dragging)

    def dinosaurs(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pencolor("red")    
        t.write("🐉", align="center", font=("Arial", 14, "normal"))
        t.penup()
        t.pencolor("#00FF00")

    turtle.listen()
    t.ondrag(dragging)
    screen.onscreenclick(dinosaurs, 3)
    screen.mainloop()



# Main function to run the program
def main():
    setup_background()
    setup_playsound()
    setup_calendar()
    setup_mouse_interactions()

if __name__ == "__main__":
    main()