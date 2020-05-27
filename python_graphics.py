## This is just a fun little program I made using the
## graphics.py library. All you do is run it and it'll
## create a cool symmetrical pattern with random colors.
## Play around with the dimensions to get different patterns.

from graphics import *
import time, random

win = GraphWin("CyberTrane's Visionary Window", 500, 500)
win.yUp()

a = 5
b = 3
c = 498
d = 495
rect = Rectangle(Point(a, b), Point(c, d))
rect.draw(win)

for x in range(10):

    for y in range(10):
        
        e = x * 25
        f = y * 25

        r = random.randrange(256)
        bb = random.randrange(256)
        g = random.randrange(256)
        color = color_rgb(r, g, bb)

        r1 = random.randrange(256)
        b1 = random.randrange(256)
        g1 = random.randrange(256)
        color1 = color_rgb(r1, g1, b1)
        
        rect1 = Rectangle(Point(a + e, b + f), Point(c - e, d - f))
        rect1.setWidth(5) ## change the width to get different patterns
        rect1.setOutline(color)
        rect1.setFill(color1)
        rect1.draw(win)

rect2 = Rectangle(Point(90, 490), Point(410, 512))
rect2.setFill('black')
rect2.draw(win)
txt = Text(Point(250, 500), 'Welcome Weary Traveler')
txt.setSize(18)
txt.setFill('white')
txt.setStyle('bold italic')
txt.setFace('courier')
txt.draw(win)
    
for i in range(50):
    txt.move(0, -5)
    rect2.move(0, -5)
    time.sleep(.005)

win.getMouse()
win.close()
