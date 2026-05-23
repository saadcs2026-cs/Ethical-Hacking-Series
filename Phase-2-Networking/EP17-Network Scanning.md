# EP 17 — Network Scanning

## Definition
Discovering active devices, open ports
and services on a network.
First step in every penetration test!

## What Hackers Scan For
- Active devices on network
- Open ports — potential entry points
- Running services and software
- Operating system versions
- Weak or default passwords

## Tools Used
- Nmap — most popular scanner
- Angry IP Scanner — simple and fast
- Netdiscover — finds WiFi devices
- Masscan — very fast scanner

## Simple Python Port Scanner
import socket
target = "192.168.1.1"
for port in range(1, 100):
    sock = socket.socket()
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    sock.close()

## Important
Always scan only networks you
own or have permission to scan!

## Follow on Instagram
@code.shield_ for full episode!
