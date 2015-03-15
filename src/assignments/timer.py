# "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
successful_stops = 0
stops = 0
flag = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = 0
    B=0
    C = 0
    D = 0
    seconds = int(t);
    D = seconds % 10
    C = ((seconds / 10) %60)%10
    B = ((seconds / 10) %60)/10
    A = seconds /600
    return str(A)+":"+str(B)+str(C)+"."+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    timer.start()
    global flag
    flag = True

def stop_timer():
    global stops, successful_stops, counter, flag
    timer.stop()
    if (flag):
        flag = False
        stops = stops + 1
        if counter % 10 == 0:
            successful_stops = successful_stops+1
            

def reset_timer():
    global stops, successful_stops, counter, flag
    timer.stop()
    counter = 0
    successful_stops = 0
    stops = 0
    flag = False

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter = counter + 1
    

# define draw handler
def draw_handler(canvas):
    global counter
    canvas.draw_text(format(counter),[100,150],20,"White")
    canvas.draw_text(str(successful_stops)+"/"+str(stops),\
                     [250,50],15,"White")
    
# create frame
frame = simplegui.create_frame("Timer",300,300)
#adding 3 buttons for Start,Stop and Reset
frame.add_button("Start",start_timer,50)
frame.add_button("Stop",stop_timer,50)
frame.add_button("Reset",reset_timer,50)
frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(100,tick)
frame.start()

