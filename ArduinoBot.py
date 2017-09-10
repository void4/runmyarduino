from pyfirmata import Arduino, util
import RunMyRobot

# XXX Replace this with your own robot id
robotID = "123456789"

board = Arduino("COM3")

@RunMyRobot.commands
def commands(args):
    print(args)
    if args["command"] == "L":
        board.digital[13].write(1)
    elif args["command"] == "R":
        board.digital[13].write(0)
        

@RunMyRobot.messages
def messages(args):
    print(args)

RunMyRobot.run(robotID)
