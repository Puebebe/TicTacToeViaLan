import socket as sock

socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

socket.connect(("169.254.234.176", 80))

while True:
    msg = input()
    socket.send(msg.encode("UTF-8"))


# DESKTOP-PBN06MI\TicTacToe
