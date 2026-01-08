import time

def timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def normalize_host(host: str) -> str:
    return host.strip().lower()
