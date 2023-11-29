import turtle
t = turtle.Turtle()

t.reset()
t.speed(0)

x= 1
month = 1
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]


t.penup()             # Setting original start
t.goto(-550, 300)
t.pendown()


for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)



while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)


t.penup()            # Moving point
t.forward(270)
t.pendown()






x= 1
month = 2
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]



for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)

while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)


t.penup()            # Moving point
t.forward(270)
t.pendown()






x= 1
month = 3
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]




for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)

while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)


t.penup()            # Moving point
t.forward(270)
t.pendown()



x= 1
month = 4
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]




for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)

while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)








# SECOND ROW




t.penup()             # Setting original start
t.goto(-550, 300)
t.right(90)
t.forward(250)
t.left(90)
t.pendown()


x= 1
month = 5
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]




for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)

while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)


t.penup()            # Moving point
t.forward(270)
t.pendown()






x= 1
month = 6
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]



for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)

while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)


t.penup()            # Moving point
t.forward(270)
t.pendown()






x= 1
month = 7
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]




for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)

while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)


t.penup()            # Moving point
t.forward(270)
t.pendown()



x= 1
month = 8
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]




for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)

while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)






# ROW THREE



t.penup()             # Setting original start
t.goto(-550, 300)
t.right(90)
t.forward(500)
t.left(90)
t.pendown()


x= 1
month = 9
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]




for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)

while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)


t.penup()            # Moving point
t.forward(270)
t.pendown()






x= 1
month = 10
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]



for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)

while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)


t.penup()            # Moving point
t.forward(270)
t.pendown()






x= 1
month = 11
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]




for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)

while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)


t.penup()            # Moving point
t.forward(270)
t.pendown()



x= 1
month = 12
day = 1
const = 20
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]




for i in range(2):           # Used to make the Month name/ the title
    t.forward(const*7)
    t.right(90)
    t.forward(20)
    t.right(90)
t.setheading(90)
t.backward(const)
t.setheading(0)
t.forward(10)
t.write(monthname[month])
t.backward(10)

while(day < 8):              # Has the month only creating 7 colomns in row with the title of the month
    for i in range (2):
        t.forward(const)
        t.right(90)
    t.forward(const-2)
    t.right(90)
    t.write(weekdays[day])
    t.setheading(180)
    t.forward(2)
    t.setheading(90)
    t.forward(const)
    t.setheading(0)
    t.forward(const)
    day += 1               # Allows the name for days to change

t.backward(const*7)
t.right(90)
t.forward(const)
t.left(90)



for i in range(6):
    for j in range(7):
        for k in range(2):
            t.forward(const)
            t.right(90)
            t.forward(const)
            t.right(90)
            
        t.forward(const)
    t.setheading(270)
    t.forward(const)
    t.setheading(0)
    t.backward(const*7)
t.penup()
t.left(90)
t.forward(160)
t.right(90)






















