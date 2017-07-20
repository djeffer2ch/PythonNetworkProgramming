from socket import socket, AF_INET, SOCK_DGRAM
from time import ctime

MAX_SIZE = 4096

if __name__ == '__main__':
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('localhost',23456))
    try:
        print("Now listening (I suppose)...")
        keepWorking = True
        while keepWorking:
            data, addr = sock.recvfrom(MAX_SIZE)
            resp = "UDP server sending data " + str(ctime())
            try:
                sock.sendto(resp.encode(), addr)
            except KeyboardInterrupt:
                print("Exited by user inner")
                break
            except Exception as err:
                print("Unhandled exception: " + str(err))
                break
            if not data or data.decode() == 'END':
                keepWorking = False
                print("Goodbye")
                break
            else:
                print("Received by user: " + str(data.decode()))
    except KeyboardInterrupt:
        print("Exited by user outer")
    except Exception as err:
        print("Unhandled exception: " + str(err))
    sock.close()
    input()