import socket

relay = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
relay.bind(("0.0.0.0", 5000))

print("UDP Relay running on port 5000")

clients = set()

while True:
    data, addr = relay.recvfrom(65535)
    clients.add(addr)

    for client in clients:
        if client != addr:
            relay.sendto(data, client)
