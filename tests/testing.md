# Proxy Server Testing

## Environment
- OS: Windows
- Language: Python 3
- Proxy Port: 8888
- Tool: curl

---

## Test Case 1: Proxy Startup

Command:python src/main.py

Expected Result:
- Proxy starts without error
- Console shows proxy listening message

---

## Test Case 2: HTTP Forwarding

Command:
Expected Result:
- Proxy starts without error
- Console shows proxy listening message

---

## Test Case 2: HTTP Forwarding

Command:curl -x http://localhost:8888 http://example.com

Expected Result:
- HTML content or HTTP redirect returned
- No proxy error

---

## Test Case 3: Domain Blocking

Configuration:
Add the following lines to `config/blocked_domains.txt`:
google.com

Restart proxy.

Command: curl -x http://localhost:8888 http://google.com

Expected Result: HTTP/1.1 403 Forbidden

---

## Test Case 4: Logging

File: logs/proxy.log

Expected Result:
- Each request logged
- Format: timestamp | client_ip | domain | ALLOWED / BLOCKED

---

## Test Case 5: HTTPS CONNECT

Command:curl -x http://localhost:8888 https://www.google.com

Expected Result:
- Successful TLS tunnel
- Binary output acceptable

---

## Test Case 6: Concurrent Requests

Command (run simultaneously in multiple terminals):curl -x http://localhost:8888 http://example.com

Expected Result:
- All requests handled successfully
- No blocking or crash

---

## Result

All test cases passed successfully.


