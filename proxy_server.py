#!/usr/bin/env python

import socket
import multiprocessing

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def handle_conn(conn, addr):
    print("Connected by", addr)
    with socket.create_connection(("www.google.com", 80)) as goog:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data: 
                break
            goog.send(data)
        
        while True:
            data = goog.recv(BUFFER_SIZE)
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
        p = multiprocessing.Process(target=handle_conn, args=(conn, addr))
        p.daemon = True
        p.start()
        print(p)
        