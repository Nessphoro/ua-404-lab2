#!/usr/bin/env python

import socket
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def handle_echo(conn, addr):
    print("Connected by", addr)
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: 
            break
        conn.send(data)
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        p = Process(target=handle_echo, args=(conn, addr))
        p.daemon = True
        p.start()
        print(p)
        
