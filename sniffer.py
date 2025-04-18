import socket

# Use UDP instead of TCP
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

# Bind to all interfaces
sniffer.bind(("0.0.0.0", 0))

print("Listening for incoming packets...")
packet = sniffer.recvfrom(65565)

print("Captured Packet:")
print(packet)
