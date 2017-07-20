import socket

HOST = 'www.linux.org' # or localhost
PORT = 80
BUFSIZ = 4096
ADDR = (HOST, PORT)

if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(ADDR)
    while True:
        data = 'GET / HTTP/1.0\r\nHost:www.linux.org\r\n\r\n'
        if not data:
            print('No data found 1')
            break
        client_sock.send(data.encode('utf-8'))
        data = client_sock.recv(BUFSIZ)
        if not data:
            print('No data found 2')
            break
        else:
            print(data.decode('utf-8'))
    client_sock.close()