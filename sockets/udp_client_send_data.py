from socket import socket, AF_INET, SOCK_DGRAM

MAX_SIZE = 4096
PORT = 23456

if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_DGRAM)
    try:
        msg = "Hello UDP server"
        while True:
            sock.sendto(msg.encode(), ('localhost', PORT))
            data, addr = sock.recvfrom(MAX_SIZE)
            print("Server says: ")
            print(repr(data))
            more = input("want to send more data to server[y/n]?: ")
            if more.lower() == 'y':
                msg = input("Enter payload: ")
            else:
                break
    except KeyboardInterrupt:
        print("Exited by user")
        sock.close()
    except Exception as err:
        print("Uncatched error: " + str(err))
        sock.close()
    input()