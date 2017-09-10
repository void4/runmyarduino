import platform
import os
import json
import traceback
import time
import sys
import subprocess
import threading
from socketIO_client import SocketIO, LoggingNamespace

robotID = '0' #Do not change this here.
server = "runmyrobot.com"
port = 8022
print('Using socket io to connect to %s' % server)
socketIO = SocketIO(server, port, LoggingNamespace)
print('Finished using socket io to connect to %s' % server)
funcs = {}
#Decorators
def commands(func):
    funcs['commands'] = func

def messages(func):
    funcs['messages'] = func

def exclusive_control(func):
    funcs['exclusive_control'] = func
#Handlers
def on_handle_command(*args):
    if args[0]['robot_id'] == robotID and 'commands' in funcs:
        threading.Thread(target=funcs['commands'], args=args).start()

def on_handle_exclusive_control(*args):
    if args[0]['robot_id'] == robotID and 'exclusive_control' in funcs:
        thread.start_new_thread(funcs['exclusive_control'], args)

def on_handle_chat_message(*args):
    if args[0]['robot_id'] == robotID and 'messages' in funcs:
        threading.Thread(target=funcs['messages'], args=args).start()

#from communication import socketIO
socketIO.on('command_to_robot', on_handle_command)
socketIO.on('exclusive_control', on_handle_exclusive_control)
socketIO.on('chat_message_with_name', on_handle_chat_message)

def myWait():
  socketIO.wait()
  thread.start_new_thread(myWait, ())

def sendChargeStateCallback(x):
    sendChargeState()

def identifyRobotId():
    socketIO.emit('identify_robot_id', robotID);

def isInternetConnected():
    return True

def run(ID):
    global robotID
    robotID = ID
    identifyRobotId()
    waitCounter = 0
    lastInternetStatus = False
    while True:
        if robotID == '0':
            pass
        socketIO.wait(seconds=10)

        if (waitCounter % 100) == 0:
            internetStatus = isInternetConnected()
            if internetStatus != lastInternetStatus:
                if internetStatus:
                    print("Connection: OK")
                else:
                    print("Connection: LOST")
            lastInternetStatus = internetStatus

        if (waitCounter % 6) == 0:

            # tell the server what robot id is using this connection
            identifyRobotId()

    waitCounter += 1
