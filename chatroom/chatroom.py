import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('binding server ...')
serv.bind(('127.0.0.1', 8080))
serv.listen(5)
print('listening on 8080 ...')
while True:
    conn1, addr1 = serv.accept()
    conn2, addr2 = serv.accept()
    while True:
        from_client1 = ''
        from_client2 = ''
        data1 = conn1.recv(4096)
        data2 = conn2.recv(4096)
        if not data1:
            break
        if not data2:
            break
        from_client1 += data1.decode('utf-8')
        from_client2 += data2.decode('utf-8')
        print('[x] received message from client 1 : ' + from_client1)
        print('[x] received message from client 2 : ' + from_client2)
        conn1.send(b"I am SERVER")
        conn2.send(b"I am SERVER")
    conn1.close()
    conn2.close()
    print('client disconnected')
