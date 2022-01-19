import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("conecting to server ...")
client.connect(('127.0.0.1', 8080))
while True:
    message = input('message : ')
    if message == 'exit':
        break
    client.send(message.encode('utf-8'))
    print('message sent.')
    from_server = client.recv(4096)
    print('[/] received message : ' + from_server.decode('utf-8'))
client.close()
