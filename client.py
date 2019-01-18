import socket

# No need for getaddrinfo
sock = socket.create_connection(("www.google.com", 80))
rline = f"GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n"
sock.send(rline.encode("utf-8"))
sock.shutdown(socket.SHUT_WR)

alldata = b""
while True:
    data = sock.recv(1024)
    if not data:
        break
    alldata += data

sock.close()

print(alldata.decode("utf-8", "ignore"))