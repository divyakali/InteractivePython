# implementation of card game - Memory

import simplegui
import random
card = 0
deck = []
CARD_WIDTH = 80
exposed =[]
CANVAS_WIDTH = 1280 
CANVAS_HEIGHT = 100
state = 0
turns=0
exposed_card_numbers =[]

# helper function to initialize globals
def new_game():
    global deck,exposed,state,turns
    state =0
    turns =0
    deck = range(8)
    deck += deck
    exposed=[False]*len(deck)
    random.shuffle(deck)

# define event handlers
def mouseclick(pos):
    global state,exposed_card_numbers,turns
    card = (pos[0]//CARD_WIDTH)
    if (not exposed[card]):
        exposed[card]=True
        #use the state of the game to decide next step
        if (state == 0):
            state = 1
            turns +=1
            label.set_text("Turns="+str(turns))
            exposed_card_numbers.append(card)
        elif (state==1):
            state = 2
            exposed_card_numbers.append(card)
        elif (state==2):
            state = 1
            if (deck[exposed_card_numbers[1]] != deck[exposed_card_numbers[0]]):
                exposed[exposed_card_numbers[1]] = False
                exposed[exposed_card_numbers[0]] = False
            exposed_card_numbers=[]
            exposed_card_numbers.append(card)
            turns +=1
            label.set_text("Turns="+str(turns))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck
    
    for key in range(len(deck)):
        if key==0:
            txt_pos = 10
        else:
            txt_pos = key
        if(exposed[key]):
            canvas.draw_text(str(deck[key]), [30+((key)*CARD_WIDTH),CANVAS_HEIGHT/2], 40, "White")
        else:
            canvas.draw_polygon([[key*CARD_WIDTH,0],\
                                 [key*CARD_WIDTH,CANVAS_HEIGHT],\
                                 [(key+1)*CARD_WIDTH,CANVAS_HEIGHT],\
                                 [(key+1)*CARD_WIDTH,0]], 3,"Black", "Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CANVAS_WIDTH, CANVAS_HEIGHT )
frame.add_button("Reset", new_game)
label = frame.add_label("Turns="+str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


