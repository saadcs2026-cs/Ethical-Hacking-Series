# EP 29 — Most Used Hacking Tools in Kali

## Reconnaissance Tools
| Tool | Purpose | Command |
|------|---------|---------|
| Nmap | Network and port scanner | nmap -sV target |
| TheHarvester | Emails and subdomains | theharvester -d target.com |
| Maltego | Visual link analysis | maltego |
| Shodan | Internet device search | shodan search apache |

## Exploitation Tools
| Tool | Purpose | Command |
|------|---------|---------|
| Metasploit | Exploitation framework | msfconsole |
| SQLmap | SQL injection | sqlmap -u target.com |
| Hydra | Password brute force | hydra -l user -P list target |
| BeEF | Browser exploitation | beef-xss |

## Network Analysis Tools
| Tool | Purpose | Command |
|------|---------|---------|
| Wireshark | Packet capture | wireshark |
| Netcat | Network utility | nc -lvnp 4444 |
| Tcpdump | CLI packet capture | tcpdump -i eth0 |
| Aircrack-ng | WiFi security | aircrack-ng |

## Password Tools
| Tool | Purpose | Command |
|------|---------|---------|
| John the Ripper | Hash cracker | john hash.txt |
| Hashcat | GPU password cracker | hashcat -m 0 hash.txt |
| Crunch | Wordlist generator | crunch 8 8 |
| RockYou.txt | Famous wordlist | Located at /usr/share/wordlists/ |

## Web Application Tools
| Tool | Purpose |
|------|---------|
| Burp Suite | Web app testing |
| Nikto | Web vulnerability scanner |
| Dirb | Directory brute forcing |
| WPScan | WordPress scanner |

## Important Rule
Always use these tools only on
systems you own or have written
permission to test!

## Follow on Instagram
@code.shield_ for full episode!
