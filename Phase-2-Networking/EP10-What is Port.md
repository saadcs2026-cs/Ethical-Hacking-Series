# EP 10 — What is a Port?

## Definition
A port is a virtual door on your device
that allows specific types of traffic
in and out!
- Like different doors of a building
- Each port handles specific data type
- Your device has 65,535 ports total
- Some are open — some are closed

## Most Important Ports
| Port | Protocol | Use |
|------|----------|-----|
| 80   | HTTP     | Normal web traffic |
| 443  | HTTPS    | Secure web traffic |
| 22   | SSH      | Remote access |
| 21   | FTP      | File transfer |
| 3306 | MySQL    | Database |
| 8080 | HTTP Alt | Alternative web |

## Ports and Hacking
Open port = potential entry point!
Hackers use tools like Nmap to scan ports.
Find open ports → find vulnerabilities.
This is called port scanning — a key
skill in ethical hacking!

## Simple Port Scanner in Python
import socket
target = "192.168.1.1"
for port in range(1, 100):
    sock = socket.socket()
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    sock.close()

## Follow on Instagram
@code.shield_ for full episode!
