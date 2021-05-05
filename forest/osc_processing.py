import OSC
from osc_dancing import pHeadStart

##########################################################
# As of March 2021, Stretch body APi only supports Python 2.
# This is an example code of OSC functionality; to receive messages.
# Using the pyOSC package.
##########################################################

def handler(addr, tags, data, client_address):
    message = []
    message.append(addr)
    message.append(data[0])
    print(message)

    if(message[0] == '/noteon'):
        if(message[1] == 60):
            print("Here")
            headflagStart.set()
            print("Head Choreo 0 started...")

    if(message[1] == '/noteoff'):
        if(message[1] == 60):
            headflagStart.clear()


def osc_functionality():
    s = OSC.OSCServer(('0.0.0.0', 7001))  # listen on localhost, port 57120
    s.addMsgHandler('/noteon', handler)  # call handler() for OSC messages received with the /noteOn address
    s.addMsgHandler('/noteoff', handler)  # call handler() for OSC messages received with the /noteOff address
    s.serve_forever()

    return

if __name__ == "__main__":
    s = OSC.OSCServer(('0.0.0.0', 8000))  # listen on localhost, port 57120
    s.addMsgHandler('/noton', handler)     # call handler() for OSC messages received with the /noteOn address
    s.addMsgHandler('/noteoff', handler)     # call handler() for OSC messages received with the /noteOff address
    s.serve_forever()