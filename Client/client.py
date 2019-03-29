import socket as sock

socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

socket.connect(("172.21.156.17", 80))