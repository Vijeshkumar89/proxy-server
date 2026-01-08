import socket
import threading
import sys

sys.path.append("include")

from config import BUFFER_SIZE


def forward(src, dst):
    try:
        while True:
            data = src.recv(BUFFER_SIZE)
            if not data:
                break
            dst.sendall(data)
    except:
        pass
    finally:
        try:
            dst.shutdown(socket.SHUT_WR)
        except:
            pass


def handle_connect(client_sock, host, port):
    server_sock = socket.create_connection((host, port))

    response = "HTTP/1.1 200 Connection Established\r\n\r\n"
    client_sock.sendall(response.encode())

    t1 = threading.Thread(target=forward, args=(client_sock, server_sock))
    t2 = threading.Thread(target=forward, args=(server_sock, client_sock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    server_sock.close()
    client_sock.close()
