# implementation of card game - Memory

import simplegui
import random

# game options and global values
WIDTH=50
HEIGHT=100
num_list = []
exposed_list = []
state = 0
idx_1 = 0
idx_2 = 0
count = 0


def new_game():
    """Helper function to initialize globals"""
    global num_list, exposed_list, state, idx_1, idx_2, count
    # initialize list with mixing nums
    num_list = range(0, 8)
    num_list.extend(range(0,8))
    random.shuffle(num_list)
    # list that help to indicate exposed nums
    exposed_list = [False for i in range(len(num_list))]
    # global values
    state = 0
    idx_1 = 0
    idx_2 = 0
    count = 0
    # set text with number of turns
    label.set_text("Turns = " + str(count))


def mouseclick(pos):
    """Define event handlers"""
    global num_list, exposed_list, state, idx_1, idx_2, count
    # game state logic
    idx = int(pos[0]/WIDTH)
    exposed_list[idx] = True
    if state == 0:
        idx_1 = idx
        state = 1
    elif state == 1:
        idx_2 = idx
        if idx_1 != idx_2:
            state = 2
            count += 1
            label.set_text("Turns = " + str(count))
    elif state == 2:
        if idx != idx_1 and idx != idx_2:
            if idx_1 != idx_2:
                if num_list[idx_1] != num_list[idx_2]:
                    exposed_list[idx_1] = False
                    exposed_list[idx_2] = False
            state = 1
            idx_1 = idx
    print state


# cards are logically 50x100 pixels in size
def draw(canvas):
    """Draw the graphics"""
    global num_list, exposed_list
    for idx in range((len(num_list))):
        # draw nums
        if exposed_list[idx] == True:
            canvas.draw_text(str(num_list[idx]), ((WIDTH)*(0.5 +idx)-15, 70), 50,
                            'Yellow', "monospace")
        # draw cards
        if exposed_list[idx] == False:
            canvas.draw_polygon([[WIDTH*idx, 0],[WIDTH*(idx+1), 0],
                                [WIDTH*(idx+1), HEIGHT],[WIDTH*(idx), HEIGHT]],
                                4, 'Lime', 'Green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


