import socket

UDP_IP = "192.168.0.155"
UDP_PORT = 50007
MESSAGE = b'\x33\x05\x32\x03\x94\x5c\x03\x00\xcb'

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))