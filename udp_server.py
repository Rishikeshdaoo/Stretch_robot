import socket

ip = "192.168.1.2"
port = 5555
# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (ip, port)
s.bind(server_address)

def udp(q):
    print("####### Server is listening #######")
    data, address = s.recvfrom(4444)
    q.put(data.decode('utf-8'))
    print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")
    return

