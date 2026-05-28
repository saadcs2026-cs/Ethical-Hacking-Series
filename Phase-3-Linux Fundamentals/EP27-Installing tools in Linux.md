# EP 27 — Installing Tools in Linux

## APT Package Manager
apt is Linux's built in tool installer.
Like an app store in the terminal!

### Basic APT Commands
| Command | Purpose |
|---------|---------|
| sudo apt update | Updates package list |
| sudo apt upgrade | Upgrades all tools |
| sudo apt install toolname | Installs a tool |
| sudo apt remove toolname | Removes a tool |
| sudo apt search toolname | Searches for tool |

### Example
sudo apt install nmap
→ Downloads and installs Nmap
→ Automatically handles dependencies

## Other Install Methods

### pip (Python tools)
pip install requests
pip install scapy
pip install impacket

### git clone (GitHub tools)
git clone https://github.com/tool
cd tool
python setup.py install

### Direct Download
wget https://url/tool.sh
chmod +x tool.sh
./tool.sh

## Essential Tool Installs
| Command | Tool |
|---------|------|
| sudo apt install nmap | Network scanner |
| sudo apt install wireshark | Packet analyser |
| sudo apt install sqlmap | SQL injection |
| sudo apt install hydra | Brute force |
| sudo apt install netcat | Network utility |
| sudo apt install metasploit-framework | Exploitation |

## Follow on Instagram
@code.shield_ for full episode!
