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
player = None
dealer = None
deck = None

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


class Card:
    """Define card class"""
    def __init__(self, suit, rank):
        # create Card object
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        # return a string representation of a card
        return self.suit + self.rank

    def get_suit(self):
        # get card's suit
        return self.suit

    def get_rank(self):
        # get card's rank
        return self.rank

    def draw(self, canvas, pos):
        # draw card on screen
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)


class Hand:
    """Define hand class"""
    def __init__(self):
        # create Hand object
        self.hand_cards = []

    def __str__(self):
        # return a string representation of a hand
        lst = ""
        for i in range(len(self.hand_cards)):
            lst += str(self.hand_cards[i]) + " "
        return "Hand contains " + lst

    def add_card(self, card):
        # add a card object to a hand
        self.hand_cards.append(card)


    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        count_A = 0
        for card in self.hand_cards:
            value += VALUES.get(card.rank)
            if card.rank == "A":
                count_A += 1
        if count_A > 0 and (value + 10) <= 21:
            value += 10
        return value


    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for card
        for card in self.hand_cards:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(card.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(card.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE,
                              [pos[0] + CARD_CENTER[0] + 73 * self.hand_cards.index(card), pos[1] + CARD_CENTER[1]], CARD_SIZE)


# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_cards = [Card(s, r) for s in SUITS for r in RANKS]

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck_cards)

    def deal_card(self):
        # deal a card object from the deck
        card = self.deck_cards.pop()
        return card

    def __str__(self):
        # return a string representing the deck
        lst = ""
        for i in range(len(self.deck_cards)):
            lst += str(self.deck_cards[i]) + " "
        return "Deck contains " + lst


#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, score
    if in_play:
        score -= 1
    # create Deck instance
    deck = Deck()
    # shuffle cards
    deck.shuffle()
    # create Hand instance for player
    player = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
     # create Hand instance for dealer
    dealer = Hand()
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome = 'Hit or stand?'
    in_play = True


def hit():
    global outcome, in_play, score
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    if in_play:
        player.add_card(deck.deal_card())
        if player.get_value() <= 21:
            outcome =  "Hit or stand?"
        else:
            outcome =  "You have busted. New deal?"
            in_play = False
            score -= 1


def stand():
    global outcome, score, in_play
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    if in_play:
        if player.get_value() > 21:
            outcome =  "You have busted. New deal?"
            score -= 1
        else:
            while dealer.get_value() <= 17:
                dealer.add_card(deck.deal_card())
            if dealer.get_value() > 21:
                outcome = "Dealer has busted. New deal?"
                score += 1
            elif dealer.get_value() >= player.get_value():
                outcome = "Dealer win ties! New deal?"
                score -= 1
            else:
                outcome = "You win! New deal?"
                score += 1
    in_play = False


def draw(canvas):
    """Draw handler"""
    # test to make sure that card.draw works, replace with your code below
    dealer.draw(canvas, [0, 150])
    player.draw(canvas, [0, 300])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [0 + CARD_BACK_CENTER[0], 150 + CARD_BACK_CENTER[1]], CARD_SIZE)
    canvas.draw_text("Blackjack", (420, 60), 40, "Black")
    canvas.draw_text(outcome, (20, 40 ), 25, "Black")
    canvas.draw_text("Score = " + str(score), (20, 80), 25, "Black")
    canvas.draw_line((0, 100), (600, 100), 3, "Red")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 450)
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

