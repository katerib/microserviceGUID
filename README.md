# Microservice: GUID Maker

## Communication

The microservice relies on [ZeroMQ](https://zeromq.org/), an open-source universal messaging library. Messages are carried via sockets which are connected by a [request-reply pattern](https://zeromq.org/get-started/?language=python#).

The microservice will generate a random GUID upon request from the server. The GUID is a 128-bit universally unique identifier, or UUID object of type 'class'. 

The server creates a socket of type response `zmq.Context().socket(zqm.REP)`. Then, the server binds the socket to port 5555 and listens for messages. Once a random GUID is made, it will be sent back to the client as a Python object `socket.send_pyobj()`.

### REQUEST data

To **request** data, the client must first create a socket of type request `zqm.Context().socket(zqm.REQ)`. Once the socket is created, the client should connect to tcp://localhost:5555 and begin sending messages with `socket.send()`.

An example call is provided below. This call requests data by sending the string "generateGUID" to the server.

```python
import zmq

context = zmq.Context()
socket = context.socket(zqm.REQ)  # create a socket of type request
socket.connect("tcp://localhost:5555")  # connect

socket.send_string("generateGUID") # send request
```

### RECEIVE data

The server will send a message back to the client via a socket. To **receive** data, the client should expect to receive the GUID as a Python object. Since the send and receive methods are blocking, if there is no message from the server then the client (receiving side) will block. 

```python
message = socket.recv_pyobj()
```

### UML Sequence Diagram

![UML Sequence Diagram](/UML-Sequence-Diagram.png)

