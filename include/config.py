import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

LISTEN_PORT = 8888
BUFFER_SIZE = 4096

BLOCKLIST_FILE = os.path.join(BASE_DIR, "config", "blocked_domains.txt")
LOG_FILE = os.path.join(BASE_DIR, "logs", "proxy.log")
