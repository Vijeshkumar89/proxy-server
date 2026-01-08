# Proxy Server Design

## 1. Overview
This project implements an HTTP forward proxy server using Python sockets.

## 2. Architecture
- Client → Proxy → Server
- Thread-per-connection model

## 3. Components
- src/main.py – server startup
- src/proxy.py – request handling
- src/tunnel.py – CONNECT tunneling
- include/config.py – constants
- include/utils.py – helpers

## 4. Request Flow
1. Client connects
2. Proxy parses request
3. Blocklist check
4. Forward or block
5. Log decision

## 5. Testing
Tested using curl with allowed and blocked domains.

## 6. Limitations
- No caching
- No HTTP/2
