#!/usr/bin/env python

import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print("Connected by", addr)
        
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data: 
                break
            conn.send(data)

        conn.close()

