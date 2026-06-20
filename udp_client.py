#! /usr/bin/python3

# Simple UDP client example

import socket
import sys

localPort   = 12060

# Enable port reusage so we will be able to run multiple clients and servers on single (host, port). 
# Do not use socket.SO_REUSEADDR except you using linux(kernel<3.9): goto https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ for more information.
# For linux hosts all sockets that want to share the same address and port combination must belong to processes that share the same effective user ID!
# So, on linux(kernel>=3.9) you have to run multiple servers and clients under one user to share the same (host, port).
# Thanks to @stevenreddie

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# Enable broadcasting mode
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(("", localPort))
while True:
    data, addr = client.recvfrom(1024)
    print("received message: %s"%data.decode())

sys.exit(0)    

# Another example, not as clean
localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromClient       = "Hello from UDP Client"

serverAddressPort   = (localIP, localPort)

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(msgFromClient.encode(), serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server: {}".format(msgFromServer[0].decode())
print(msg)
