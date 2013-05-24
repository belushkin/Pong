# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

score1 = 0
score2 = 0
paddle1_pos = 0
paddle1_vel = 0
paddle2_pos = 0
paddle2_vel = 0

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if right == True:
        ball_vel = [5,-4]
    else:
        ball_vel = [-5,-4]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints

    score1 = 0
    score2 = 0
    paddle1_pos = 0
    paddle2_pos = 0
    paddle1_vel = 0
    paddle2_vel = 0
    ball_init(random.choice([True, False]))

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel

    if (paddle1_pos < 0):
        paddle1_pos -= paddle1_vel
    if (paddle1_pos >= (HEIGHT - PAD_HEIGHT)):
        paddle1_pos -= paddle1_vel

    if (paddle2_pos < 0):
        paddle2_pos -= paddle2_vel
    if (paddle2_pos >= (HEIGHT - PAD_HEIGHT)):
        paddle2_pos -= paddle2_vel

    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # draw paddles
    c.draw_polygon([(0, paddle1_pos), (0, PAD_HEIGHT + paddle1_pos), (PAD_WIDTH, PAD_HEIGHT + paddle1_pos), (PAD_WIDTH, paddle1_pos)], 3, "White", "White")
    c.draw_polygon([((WIDTH - PAD_WIDTH - 1), paddle2_pos), ((WIDTH - PAD_WIDTH - 1), PAD_HEIGHT + paddle2_pos), (WIDTH, PAD_HEIGHT + paddle2_pos), (WIDTH, paddle2_pos)], 3, "White", "White")
     
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[0] >= (WIDTH - 1 - PAD_WIDTH) - BALL_RADIUS:
        ball_vel[0] = -ball_vel[0]

    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        ball_vel[0] = -ball_vel[0]

    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    c.draw_text(str(score1), (220, 70), 52, "White")
    c.draw_text(str(score2), (350, 70), 52, "White")

def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 2
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = 2
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel -= acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel -= acc

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)

# start frame
frame.start()

