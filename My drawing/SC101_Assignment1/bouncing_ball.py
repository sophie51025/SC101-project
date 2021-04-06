"""
File: Bouncing ball
Name:Sophie
-------------------------
TODO:Stimulate ball's bouncing track
"""

from campy.graphics.gobjects import GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
LIFE = 3  # this constant decides how many time ball can bounce

#global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
label = GLabel('Remaining life:' + str(LIFE), 650, 30)

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball)
    window.add(label)
    label.font = 'Courier-10-italic'
    label.color = 'navy'
    onmouseclicked(ball_start_to_bounce)


def ball_start_to_bounce(point):
    """
    This function control the start of bouncing process
    """
    global LIFE, label
    vy = 0
    ball_original_position = window.get_object_at(START_X+SIZE/2, START_Y+SIZE/2)
    if LIFE != 0 and ball_original_position is ball:
        while True:
            if ball.x + SIZE <= window.width and ball.y + SIZE <= window.height and vy >= 0:
                ball.move(VX, vy)
                vy += GRAVITY
                # while ball.x + SIZE <= window.width and ball.y + SIZE <= window.height:
                #     ball.move(VX, vy)
                #     vy += GRAVITY
                pause(DELAY)
            elif ball.x + SIZE <= window.width and ball.y + SIZE >= window.height:
                vy *= -REDUCE
                ball.move(VX, vy)
                pause(DELAY)
                while ball.x + SIZE <= window.width and vy <= 0:
                    vy += GRAVITY
                    ball.move(VX, vy)
                    pause(DELAY)
            elif ball.x + SIZE >= window.width:
                window.add(ball, x=START_X, y=START_Y)
                LIFE -= 1
                label.text = 'Remaining life:' + str(LIFE)
                break


# def ball_start_to_bounce(point):
#     global LIFE, label
#     vy = 0
#     ball_original_position = window.get_object_at(START_X+SIZE/2, START_Y+SIZE/2)
#     if LIFE != 0 and ball_original_position is ball:
#         while True:
#             pause(DELAY)
#             ball.move(VX,vy)
#             vy += GRAVITY
#             pause(DELAY)
#             if ball.x + SIZE >=window.height:
#                 vy *= -REDUCE
#             if ball.x + SIZE >= window.width:
#                 window.add(ball, x=START_X, y=START_Y)
#                 LIFE -= 1
#                 label.text = 'Remaining life:' + str(LIFE)
#                     break






if __name__ == "__main__":
    main()
