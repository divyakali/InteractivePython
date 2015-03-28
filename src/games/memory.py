# implementation of card game - Memory

import simplegui
import random
deck = []
pos_init = [80,0]
exposed =[]
# helper function to initialize globals
def new_game():
    global deck
    global exposed
    deck = range(8)
    deck += deck
    exposed=[True]*len(deck)
    exposed[3]=False
    exposed[9]=False
    random.shuffle(deck)
    print exposed

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck
    
    for key in range(len(deck)):
        if key==0:
            txt_pos = 10
        else:
            txt_pos = key
        if(exposed[key]):
            canvas.draw_text(str(deck[key]), [30+((key)*pos_init[0]),50], 40, 'Red')
        else:
            canvas.draw_polygon([[key*pos_init[0],0],\
                                 [key*pos_init[0],100],\
                                 [(key+1)*pos_init[0],100],\
                                 [(key+1)*pos_init[0],0]], 3,"black", "Green")
    
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 1200, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric