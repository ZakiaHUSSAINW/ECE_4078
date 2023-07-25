# teleoperate the robot with your keyboard (M1)
# will be extended in following milestones for system integration

# basic python packages
from bottle import get,post,run,route,request,template,static_file
import threading
import socket #ip

############### add your codes below ###############
# TODO: Add necessary utility functions and initialisation for robot teleoperation
from AlphaBot import AlphaBot
Ab = AlphaBot()
####################################################

# bottle functions
@get("/")
def index():
	return template("index")
	
@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='./')

@route('/fonts/<filename>')
def server_fonts(filename):
    return static_file(filename, root='./fonts/')
	
@post("/cmd")
def cmd():
    code = request.body.read().decode()
    print(code)

    ############### add your codes below ###############
    if code == "stop":
        #pass # TODO: replace with your code to make the robot stop
        Ab.stop()
        print("stop")
    elif code == "forward":
        #pass # TODO: replace with your code to make the robot move forward
        Ab.forward()
        print("forward")
    elif code == "backward":
        #pass # TODO: replace with your code to make the robot move backward
        Ab.backward()
        print("backward")
    elif code == "turnleft":
        #pass # TODO: replace with your code to make the robot turn left
        Ab.left()
        print("turnleft")
    elif code == "turnright":
        #pass # TODO: replace with your code to make the robot turn right
        Ab.right()
        print("turnright")
    ####################################################
    return "OK"

# Threading timer	
def timerfunc():
	global t        #Notice: use global variable!
	t = threading.Timer(0.02, timerfunc)
	t.start()
    
t = threading.Timer(0.02, timerfunc)
t.setDaemon(True)
t.start()

# Socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('8.8.8.8',80))
localhost=s.getsockname()[0]
run(host = localhost, port = 8000)
