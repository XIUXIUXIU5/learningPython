#!/usr/bin/env python
import socket,time,threading
#server
def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
while True:
    # accept a new connection:
    sock, addr = s.accept()
    # create thread to deal with the TCP connection:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
