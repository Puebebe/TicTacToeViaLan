import socket as sock

class Server:
    def __init__(self, address, port = 80, connectionsLimit = 2):
        self.address = address
        self.port = port
        self.connectionsLimit = connectionsLimit
        self.clients = []

    def run(self):
        print("Starting server...")

        self.socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM) 
        self.socket.bind((self.address, self.port))
        self.socket.listen(self.connectionsLimit)
        print("Waiting for connections...")

        client_socket, socket = self.socket.accept()

        print("------------\nSomeone has connected. Socket on the other side: ", socket, "\n------------")

        self.clients.append(client_socket)

        client_socket.send("I see you".encode('UTF-8'))