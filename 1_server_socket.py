import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    print('Waiting for connection ...')
    client_socket, addr = server_socket.accept()    #<---Block
    print('Connection from : ', addr)

    while True:
        print('Waiting for client request')
        request = client_socket.recv(4*1024)    #<---Block

        if request:
            print(f'Received: {request.decode()}')
            response = b'Hello from server \n'
            client_socket.send(response)    #<---Block
        else:
            break

    client_socket.close()
    print('Ready for new client')
