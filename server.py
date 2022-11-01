#   Binds REP socket to tcp://*:5555

import zmq
import uuid

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#  Wait for next request from client
while True:
    message = socket.recv()
    print(f"Received request: {message}")

    #  Generate a random UUID
    GUID = uuid.uuid4()
    print(f"sending: {GUID} \n")

    # Send GUID back to client
    socket.send_pyobj(GUID)
