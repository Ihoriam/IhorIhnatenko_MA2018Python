import simplegui

# game's settings
t = 0
format_string = "0.00.0"
success_attempts = 0
number_attempts = 0
flag = False


def tick():
    """Handler for timer"""
    global t
    t += 1


def draw(canvas):
    """Handler to draw on canvas"""
    canvas.draw_text(format(t), (100, 110), 40, 'Green')
    canvas.draw_text(format_attempts(number_attempts, success_attempts),
                     (260, 20), 20, 'Red')


def start_timer():
    """Handler for button"""
    global flag
    timer.start()
    flag = True


def stop_timer():
    """Handler for button"""
    global number_attempts, success_attempts, flag
    timer.stop()
    # using flag to ensure that hitting the "Stop" button when the timer
    # is already stopped does not change your score
    if flag:
        if int(format_string[-1]) == 0:
            success_attempts += 1
        number_attempts += 1
    flag = False


def reset_timer():
    """Handler for button"""
    global t, number_attempts, success_attempts
    timer.stop()
    number_attempts = 0
    success_attempts = 0
    t = 0
    flag = False


def format(t):
    """Format time to A:BC.D where A,C and D are digits
        in the range 0-9 and B is in the range 0-5."""
    global format_string
    # some math operation to convert time
    m_sec = t % 10
    sec = (t / 10) % 60
    minute = (t / 10) / 60
    # format text
    format_string = str(minute) + ":"
    if sec < 10:
        format_string += "0" + str(sec) + "." + str(m_sec)
    else:
        format_string += str(sec) + "." + str(m_sec)
    return format_string


def format_attempts(number_attempts, success_attempts):
    """Format some text"""
    # format text
    format_string = str(success_attempts) + "/" + str(number_attempts)
    return format_string


# create frame
frame = simplegui.create_frame("Stop: Game", 300, 200)

# registre draw handler
frame.set_draw_handler(draw)

# create timer
timer = simplegui.create_timer(100, tick)

# add buttons
frame.add_button("Start", start_timer, 200)
frame.add_button("Stop", stop_timer, 200)
frame.add_button("Reset", reset_timer, 200)

# start game
frame.start()


