# Python HTTP Proxy Server

## Description
This project implements an HTTP forward proxy server using Python sockets.
The proxy filters client requests based on a blocklist and forwards allowed
requests to the destination server.

---

## Features
- HTTP request forwarding
- Domain blocking
- Request logging
- Concurrent client handling
- HTTPS CONNECT tunneling

---

## Directory Structure
```
proxy-project/
├── src/
├── include/
├── config/
├── docs/
├── tests/
├── setup.py
```
---

## Execution

Run the proxy server from the project root:


The proxy listens on port 8888.

---

## Usage

HTTP request: curl -x http://localhost:8888 http://example.com

Blocked domain: curl -x http://localhost:8888 http://example.com

HTTPS request: curl -x http://localhost:8888 https://www.example.com

---

## Logging

Log file:logs/proxy.log

Each entry contains:
- Timestamp
- Client IP
- Requested domain
- Action (ALLOWED / BLOCKED)

---

## Documentation
- Design: `docs/design.md`
- Testing: `tests/TESTING.md`

---

## Video Demonstration

A complete video demonstration of the proxy server features, including
HTTP forwarding, domain blocking, logging, HTTPS CONNECT support, and
concurrent request handling, is available at the link below:

📽️ Video Demo: https://drive.google.com/file/d/1pm3voQjNXyd5nsM45q-Xi3xVCZqjwXLL/view?usp=drive_link

---
