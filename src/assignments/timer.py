#Code Skulptor GUI module
import simplegui

#Event Handler
def tick():
	print "Tick!"

#Register handler
timer= simplegui.create_timer(1000,tick)

#Start timer
timer.start()	