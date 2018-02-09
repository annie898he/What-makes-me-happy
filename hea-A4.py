# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:27:12 2016

@author: hea
"""
#Created by Annie He
#Acknowledgment: Jan Pearce
#Objective: Shows the use of the turtles library and loops
#Assignment: A4

import turtle
import random 
wn = turtle.Screen()
wn.bgcolor("black")
nt = turtle.Turtle()

for i in range(181):            #range gives a list of 181 numbers from 0-180
    nt.speed(30)                #makes the speed of the turtle to 30
    nt.forward(50)              #moves the turtle along
    nt.left(40)                 #rotates the turtle
    nt.forward(30)
    nt.right(80)                #rotates the turtle
    nt.forward(50)
    nt.left(60)
    nt.forward(40)
    nt.right(90)
    nt.forward(20)
    nt.right(90)
    nt.right(20)

#if the range is greater than 70, then it will choose from grey78, grey73, gray51, grey87, steelblue3, steelblue2, and orange
    if i >60:
        nt.color(random.choice(["grey78", "grey73", "gray51", "grey87", "steelblue3", "steelblue2", "orange" ]))
#if the range is less than 70, then it will choose from gray57, grey83, gray96, orchid2, and orchid3
    else:
        nt.color(random.choice(["gray57", "grey83", "gray96", "orchid2", "orchid3" ]))

    nt.penup()                  #lifts up the turtle
    nt.setposition(0, 0)        #this is to make the turtle return to the starting position
    nt.pendown()                #places the turtle back down
    
    nt.left(2)                  #this is so the loop changes degrees instead of repeating the same ones
    

wn.exitonclick()