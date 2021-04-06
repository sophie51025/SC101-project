"""
File: Python + Zentagle for guinea pig
Name:Sophie
----------------------
There's a guinea pig in the center of window telling people that Python is just like Zentangle
that even using same code/pattern, each work is impossible to be the same.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
import random


# This controls the pause time (in millisecond) for the animation
DELAY = 10

# global variable
window = GWindow(width=600, height=600, title='Zentangle = Python')

def main():
    """
    it shows the animation of a guinea pig with zentangle pattern, and a label will show on the top of window
    """
    #background

    background = GRect(600, 600)
    background.filled = True
    window.add(background)


    #zentangle

    for i in range(0,600,30):
        line = GLine(i,0,600,600)
        window.add(line)
        line.color = 'white'
        pause(10)

    for j in range(0,600,30):
        line = GLine(600,j,0,600)
        window.add(line)
        line.color = 'wheat'
        pause(10)

    for k in range(0, 600, 30):
        line = GLine(600-k, 600, 0, 0)
        window.add(line)
        line.color = 'whitesmoke'
        pause(10)

    for l in range(0, 600, 30):
        line = GLine(0, 600-l, 600, 0)
        window.add(line)
        line.color = 'grey'
        pause(10)



    for m in range(0,300, 10):
        circle = GOval(m, m, x=random.randrange(0, window.width), y=random.randrange(0, window.width))
        window.add(circle)
        circle.color = 'red'
        pause(10)

    for n in range(0, 200, 40):
        circle = GOval(n, n, x=random.randrange(0, window.width), y=random.randrange(0, window.width))
        window.add(circle)
        circle.color = 'orange'
        pause(10)

    for o in range(100,300, 35):
        circle = GOval(o, o, x=random.randrange(0, window.width), y=random.randrange(0, window.width))
        window.add(circle)
        circle.color = 'yellow'
        pause(10)

    for p in range(50,200, 25):
        circle = GOval(p, p, x=random.randrange(0, window.width), y=random.randrange(0, window.width))
        window.add(circle)
        circle.color = 'lime'
        pause(10)

    for q in range(0,100, 15):
        circle = GOval(q, q, x=random.randrange(0, window.width), y=random.randrange(0, window.width))
        window.add(circle)
        circle.color = 'lightblue'
        pause(10)

    for r in range(300, 500, 30):
        circle = GOval(r, r, x=random.randrange(0, window.width), y=random.randrange(0, window.width))
        window.add(circle)
        circle.color = 'navy'
        pause(10)

    for s in range(0, 400, 50):
        circle = GOval(s, s, x=random.randrange(0, window.width), y=random.randrange(0, window.width))
        window.add(circle)
        circle.color = 'purple'
        pause(10)


    #face
    face = GPolygon()
    face.add_vertex((255, 250))
    face.add_vertex((345, 250))
    face.add_vertex((355, 340))
    face.add_vertex((245, 340))

    forehead = GPolygon()
    forehead.add_vertex((270, 255))
    forehead.add_vertex((330, 255))
    forehead.add_vertex((335, 275))
    forehead.add_vertex((265, 275))

    l_chin = GPolygon()
    l_chin = GPolygon()
    l_chin.add_vertex((250, 310))
    l_chin.add_vertex((300, 305))
    l_chin.add_vertex((300, 340))
    l_chin.add_vertex((247, 340))

    r_chin = GPolygon()
    r_chin = GPolygon()
    r_chin.add_vertex((300, 305))
    r_chin.add_vertex((350, 310))
    r_chin.add_vertex((353, 340))
    r_chin.add_vertex((300, 340))

    nose = GOval(18, 35, x=292, y=290)

    l_eye = GOval(15, 17, x=280, y=285)
    r_eye = GOval(15, 17, x=310, y=285)

    l_foot = GOval(20, 30, x=233, y=315)
    r_foot = GOval(20, 30, x=348, y=315)

    l_ear = GOval(25, 15, x=230, y=265)
    r_ear = GOval(25, 15, x=345, y=265)

    mouse1 = GLine(300, 340, 300, 333)
    mouse2 = GLine(300, 333, 293, 323)
    mouse3 = GLine(300, 333, 307, 323)

    window.add(l_foot)
    l_foot.filled = True
    l_foot.fill_color = 'lightsalmon'
    l_foot.color = 'lightsalmon'

    window.add(r_foot)
    r_foot.filled = True
    r_foot.fill_color = 'lightsalmon'
    r_foot.color = 'lightsalmon'

    window.add(face)
    face.filled = True
    face.fill_color = 'goldenrod'
    face.color = 'goldenrod'

    window.add(forehead)
    forehead.filled = True
    forehead.fill_color = 'lightyellow'
    forehead.color = 'peachpuff'

    window.add(l_chin)
    l_chin.filled = True
    l_chin.fill_color = 'wheat'
    l_chin.color = 'wheat'

    window.add(r_chin)
    r_chin.filled = True
    r_chin.fill_color = 'wheat'
    r_chin.color = 'wheat'

    window.add(nose)
    nose.filled = True
    nose.fill_color = 'wheat'
    nose.color = 'wheat'

    window.add(mouse1)
    mouse1.color = 'brown'
    window.add(mouse2)
    mouse2.color = 'brown'
    window.add(mouse3)
    mouse3.color = 'brown'

    window.add(l_eye)
    l_eye.filled = True
    window.add(r_eye)
    r_eye.filled = True

    window.add(l_ear)
    l_ear.filled = True
    l_ear.fill_color = 'brown'
    l_ear.color = 'brown'
    window.add(r_ear)
    r_ear.filled = True
    r_ear.fill_color = 'brown'
    r_ear.color = 'brown'


    # words
    label = GLabel('Python is just like Zentangle - impossible to have the same works')
    label.font = 'Courier-10-italic'
    words_frame = GRect(530, 40, x=(window.width - label.width - 10) / 2, y=18)
    label.color = 'navy'

    window.add(words_frame)
    words_frame.filled = True
    words_frame.fill_color = 'lemonchiffon'
    words_frame.color = 'gold'
    window.add(label, x=(window.width - label.width) / 2, y=50)

    vx = 1
    while True:
        label.move(vx, 0)
        words_frame.move(vx, 0)
        if words_frame.x <= 0 or words_frame.x + words_frame.width >= window.width:
            vx = -vx
        pause(DELAY)




if __name__ == '__main__':
    main()
