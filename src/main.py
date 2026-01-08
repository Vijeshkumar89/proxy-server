import socket
import threading
import sys

sys.path.append("include")

from config import LISTEN_PORT
from proxy import handle_client, load_blocklist

def main():
    blocked_domains = load_blocklist()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("", LISTEN_PORT))
    server.listen(100)

    print(f"[+] Proxy listening on port {LISTEN_PORT}")

    while True:
        client_socket, client_addr = server.accept()
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_addr, blocked_domains),
            daemon=True
        )
        thread.start()

if __name__ == "__main__":
    main()
