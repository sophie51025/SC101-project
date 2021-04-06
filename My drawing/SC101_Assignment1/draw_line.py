"""
File: draw a line
Name:Sophie
-------------------------
TODO:when user click two different point in the window, they will be connected by a line
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
import random

# constant
SIZE = 5  # This represents diameter of point when  click the first point of a line.

# global variable
window = GWindow()
first_point_x = 0
first_point_y = 0
first_hole = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)

def draw_line(point):
    global first_point_x, first_point_y, first_hole
    if first_point_x == 0 & first_point_y == 0:
        first_hole = GOval(SIZE, SIZE, x=point.x - SIZE/2, y=point.y - SIZE/2)  #圈圈在中間
        window.add(first_hole)
        first_point_x = point.x
        first_point_y = point.y
    else:
        line = GLine(first_point_x,first_point_y,point.x,point.y)
        window.add(line)
        line.color = random_color()
        window.remove(first_hole)
        first_point_x = 0
        first_point_y = 0


###
# def draw_line(mouse):
#     global num
#     num +=1
#     if num % 2 == 1:
#         window.add(oval, mouse.x-SIZE/2, mouse.y-SIZE/2)
#     else:
#         line = GLine(oval.x+SIZE/2, oval.y+SIZE/2, mouse.x, mouse.y)
#         window.add(line)
#         window.remove(oval)

def random_color():
    num = random.choice(range(15))
    if num == 0:
        return "pink"
    elif num == 1:
        return "orange"
    elif num == 2:
        return "yellow"
    elif num == 3:
        return "green"
    elif num == 4:
        return "blue"
    elif num == 5:
        return "navy"
    elif num == 6:
        return "purple"
    elif num == 7:
        return"red"
    elif num == 8:
        return"maroon"
    elif num == 9:
        return"magenta"
    elif num == 10:
        return"violet"
    elif num == 11:
        return"aqua"
    elif num == 12:
        return"brown"
    elif num == 13:
        return"azure"
    elif num == 14:
        return"darkgoldenrod"
















if __name__ == "__main__":
    main()
