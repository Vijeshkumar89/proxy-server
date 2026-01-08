import socket
import sys

sys.path.append("include")

from config import BUFFER_SIZE, BLOCKLIST_FILE, LOG_FILE
from utils import timestamp, normalize_host
from tunnel import handle_connect


def load_blocklist():
    blocked = set()
    with open(BLOCKLIST_FILE) as f:
        for line in f:
            domain = line.strip().lower()
            if domain:
                blocked.add(domain)
    return blocked


def log(entry):
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")


def recv_headers(sock):
    data = b""
    while b"\r\n\r\n" not in data:
        chunk = sock.recv(BUFFER_SIZE)
        if not chunk:
            break
        data += chunk
    return data


def handle_client(client_sock, client_addr, blocked_domains):
    try:
        request = recv_headers(client_sock)
        if not request:
            client_sock.close()
            return

        request_text = request.decode(errors="ignore")
        lines = request_text.split("\r\n")
        request_line = lines[0]

        method, target, _ = request_line.split()

        host = ""
        for line in lines:
            if line.lower().startswith("host:"):
                host = normalize_host(line.split(":", 1)[1])
                break

        time_now = timestamp()

        if host in blocked_domains:
            response = (
                        "HTTP/1.1 403 Forbidden\r\n"
                        "Content-Type: text/plain\r\n"
                        "Content-Length: 23\r\n\r\n"
                        "Blocked by proxy\n"
                    )
            client_sock.sendall(response.encode())
            log(f"{time_now} | {client_addr[0]} | {host} | BLOCKED")
            client_sock.close()
            return

        log(f"{time_now} | {client_addr[0]} | {host} | ALLOWED")

        # HTTPS CONNECT
        if method.upper() == "CONNECT":
            dest_host, dest_port = target.split(":")
            handle_connect(client_sock, dest_host, int(dest_port))
            return

        # Normal HTTP forwarding
        server_sock = socket.create_connection((host, 80))
        server_sock.sendall(request)

        while True:
            data = server_sock.recv(BUFFER_SIZE)
            if not data:
                break
            client_sock.sendall(data)

        server_sock.close()
        client_sock.close()

    except Exception:
        client_sock.close()
