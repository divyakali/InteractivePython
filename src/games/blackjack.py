# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
busted= False
stand_flag=False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards=[]   # create Hand object

    def __str__(self):
        # return a string representation of a hand
        messages =[]
        for card in self.cards:
            messages.append(str(card)+" ")
        return "Hand contains "+"".join(messages)
              

    def add_card(self, card):
        self.cards.append(card) # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        aces =[]
        number_of_aces = 0
        for card in self.cards:
            if card.rank!= "A":
                hand_value += VALUES[card.rank]
            else:
                aces.append(card)
        for card in aces:
            if(len(aces)==2) and hand_value<=9:
                return hand_value+12
            elif(len(aces)==2) and hand_value>9:
                return hand_value+2
            elif hand_value+11 <= 21:
                hand_value+=11
            else:
                hand_value+=1
        return hand_value
            
   
    def draw(self, canvas, pos):
        pass    # draw a hand on the canvas, use the draw method for cards

     
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards=[]
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop(0)    # deal a card object from the deck
    
    def __str__(self):
            # return a string representing the deck
        messages =[]
        for card in self.cards:
            messages.append(str(card)+" ")
        return "Deck contains "+"".join(messages)

dealer_hand= Hand()
player_hand= Hand()
deck = Deck()

#define event handlers for buttons
def deal():
    global outcome, in_play, dealer_hand,player_hand
    dealer_hand= Hand()
    player_hand= Hand()
    deck = Deck()
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    print "Dealer hand:"
    print dealer_hand
    print dealer_hand.get_value()
    print "Player Hand:"
    print player_hand
    print player_hand.get_value()
    
    in_play = True

def hit():
    global player_hand,dealer_hand,in_play,busted,stand_flag 
    # if the hand is in play, hit the player
    
    if not stand_flag:
        if player_hand.get_value()<=21:
            player_hand.add_card(deck.deal_card())
            print "Player score is"
            print player_hand
            print player_hand.get_value()
        if player_hand.get_value()>21:
            print "Player is busted"
            in_play=False
    else:
        if dealer_hand.get_value()<=21:
            dealer_hand.add_card(deck.deal_card())
            if dealer_hand.get_value()>=17:
                if ( dealer_hand.get_value()>21):
                    print "Dealer Busted. Player wins!"                   
                elif( dealer_hand.get_value() > player_hand.get_value() or \
                dealer_hand.get_value() == player_hand.get_value()):
                    print "Dealer wins"
                else:
                    print "player wins"    
        else:
            print "Dealer is busted . Player wins"
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global stand_flag
    print dealer_hand.get_value()
    stand_flag = True
    if  not in_play:
        print "Player got busted"
    while(in_play and dealer_hand.get_value<=17):
        print dealer_hand
        hit()
    
        
        
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
        # test to make sure that card.draw works, replace with your code below
    global dealer_hand, player_hand
    canvas.draw_text("BlackJack",[20,50], 40 ,'Black')
    canvas.draw_text("Score",[350,50], 30 ,'Black')
    canvas.draw_text("Dealer",[20,200], 30 ,'Black')
    canvas.draw_text("Result",[150,200], 30 ,'Black')
    canvas.draw_text("Player",[20,450],30,'Black')
    canvas.draw_text("Hit or Stand",[150,450],30,'Black')
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric