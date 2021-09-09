#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Lyndan Wall
September 2nd, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.begin_fill()
Traceback (most recent call last):

  File "<ipython-input-1-9be2516e7133>", line 1, in <module>
    turtle.begin_fill()

NameError: name 'turtle' is not defined


turtle.forward(100)
Traceback (most recent call last):

  File "<ipython-input-2-585bbd158605>", line 1, in <module>
    turtle.forward(100)

NameError: name 'turtle' is not defined


runfile('/Users/lyndanwall/Desktop/ATLS 1300/pc02-graffiti-section12-LyndanWall-master/Turtle_start.py', wdir='/Users/lyndanwall/Desktop/ATLS 1300/pc02-graffiti-section12-LyndanWall-master')

turtle.begin_fill()

turtle.forward(100)

turtle.right(90)

turtle.forward(200)

turtle.right(90)

turtle.forward(100)

turtle.right(90)

turtle.forward(200)

turtle.end_fill()

turtle.home()

turtle.dot(3,pink)
Traceback (most recent call last):

  File "<ipython-input-14-48bf8841a586>", line 1, in <module>
    turtle.dot(3,pink)

NameError: name 'pink' is not defined


turtle.dot(3,*pink)
Traceback (most recent call last):

  File "<ipython-input-15-b88240726298>", line 1, in <module>
    turtle.dot(3,*pink)

NameError: name 'pink' is not defined


turtle.dot(3,deeppink)
Traceback (most recent call last):

  File "<ipython-input-16-223a17308984>", line 1, in <module>
    turtle.dot(3,deeppink)

NameError: name 'deeppink' is not defined


turtle.dot(3,DeepPink)
Traceback (most recent call last):

  File "<ipython-input-17-fbd57b4b2d45>", line 1, in <module>
    turtle.dot(3,DeepPink)

NameError: name 'DeepPink' is not defined


turtle.up
Out[18]: <function turtle.up()>

turtle.up()

turtle.color("DeepPink")

turtle.circle(100)

turtle.down()

turtle.circle(100)

turtle.end_fill()

turtle.begin_fill()

turtle.circle(100)

turtle.end_fill()

turtle.stamp()
Out[28]: 9

turtle.home
Out[29]: <function turtle.home()>

turtle.dot(4,"DeepPink4")



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
