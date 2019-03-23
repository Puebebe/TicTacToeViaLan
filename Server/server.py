import socket as sock

print("SERVER")

socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

#socket.bind(("169.254.197.5", 80))
socket.bind(("169.254.234.176", 80))
socket.listen(2)

client_socket, socket = socket.accept()

print("successful connection")

while True:
    msg = client_socket.recv(1024).decode()
    if msg != "":
        print(msg)

#client_socket.send("Message".encode('UTF-8'))