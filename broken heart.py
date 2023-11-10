import turtle
import time

turtle.Screen().bgcolor("black")

t = turtle.Pen()

t.pencolor("red")
t.pensize(5)
t.fillcolor("red")
t.speed(1)
t.begin_fill()
t.seth(45)
t.forward(200)
t.circle(90,170)

t.seth(-125)
t.forward(45)
t.seth(-55)
t.forward(60)
t.seth(-120)
t.forward(80)
t.seth(-70)
t.forward(40)
t.seth(130)
t.forward(50)
t.seth(70)
t.forward(70)
t.seth(130)
t.forward(60)
t.seth(60)
t.forward(40)

t.seth(135)
t.circle(90,180)
t.forward(201)
t.end_fill()

t.hideturtle()

# Menambahkan kata-kata
t.penup()
t.goto(-30, -150) 
t.pendown()
t.pencolor("red")
t.write("Terkadang Melepas Payung Tidak Seburuk itu,\n            Nikmati saja Hujan dan Badainya\n                 Nanti juga akan reda Sendiri\n                                   - H1k", font=("Times New Roman", 20, "bold"), align="center") 

time.sleep(2) 
turtle.done()
