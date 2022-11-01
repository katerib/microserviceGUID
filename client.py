#   Connects REQ socket to tcp://localhost:5555

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


#  Send message to request GUID when needed (x3 loop for testing)
for x in range(3):
    print(f"Sending request to server ...")
    socket.send_string("generateGUID")

    #  Get reply
    message = socket.recv_pyobj()
    print(f"Received reply [ {message} ]\n")
