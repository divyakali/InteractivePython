# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True
# create a list to hold ball position
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
paddle1_pos = [0,80]
paddle2_pos = [599,80]
paddle1_vel = 0
paddle2_vel=0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    #Randomize the velocity
    horizontal_vel = random.randrange(120, 240)/60
    vertical_vel = random.randrange(60, 180)/60
    #Spawn the ball the direction chosen
    if (direction == "LEFT"):
        ball_vel = [-horizontal_vel, -vertical_vel]
    if (direction == "RIGHT"):
        ball_vel = [horizontal_vel, -vertical_vel]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball("LEFT")

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel,paddle2_vel,score1,score2
    #Code to make the ball bounce off the gutters and upper/lower walls
    if (ball_pos[1]>(HEIGHT-1)-BALL_RADIUS) or (ball_pos[1]< BALL_RADIUS) :
        ball_vel[1] *= -1
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]        
    
    # draw ball
    canvas.draw_circle( ball_pos , BALL_RADIUS, 2,"White","yellow")
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos[1] + PAD_HEIGHT + paddle1_vel< HEIGHT-1)\
    and (paddle1_pos[1] + paddle1_vel > 0 ):
        paddle1_pos[1] += paddle1_vel
    if (paddle2_pos[1] + PAD_HEIGHT + paddle2_vel< HEIGHT-1)\
    and (paddle2_pos[1] + paddle2_vel > 0 ):    
        paddle2_pos[1] += paddle2_vel
    
    
    # draw paddles
    canvas.draw_line(paddle1_pos,[paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT], PAD_WIDTH, "Silver")
    canvas.draw_line(paddle2_pos,[paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT], PAD_WIDTH, "Silver")
    
    
    # determine whether paddle and ball collide 
    # increase the velocity of the ball when ball hits the paddle
    # determine scores and spawn a new ball if the ball misses a paddle
    if ((ball_pos[0]>(WIDTH-1-PAD_WIDTH)-BALL_RADIUS)\
    and ((ball_pos[1]<=paddle2_pos[1] + PAD_HEIGHT and ball_pos[1]>paddle2_pos[1]))) \
    or ((ball_pos[0]< BALL_RADIUS+PAD_WIDTH) \
    and (ball_pos[1]<=paddle1_pos[1] + PAD_HEIGHT and ball_pos[1]>paddle1_pos[1])):
        ball_vel[0] *= -1.1
        ball_vel[1] *= -1.1
    elif (ball_pos[0]>(WIDTH-1-PAD_WIDTH)-BALL_RADIUS):
        spawn_ball("LEFT")
        score1 += 1
    elif (ball_pos[0]< BALL_RADIUS+PAD_WIDTH):
        spawn_ball("RIGHT")
        score2 += 1
    
    # draw scores
    canvas.draw_text(str(score1), [150, 30], 40, 'White')
    canvas.draw_text(str(score2), [450, 30], 40, 'White')    

def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
   

def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = 0
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = acc


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button( "Reset", new_game, 50)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_canvas_background("Green")


# start frame
new_game()
frame.start()
