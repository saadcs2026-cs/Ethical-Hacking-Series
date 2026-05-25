# EP 24 — File System in Linux

## Linux File System Structure
| Directory | Purpose |
|-----------|---------|
| / | Root — top of everything |
| /home | User home directories |
| /etc | System config files |
| /var | Variable data and logs |
| /tmp | Temporary files |
| /bin | Essential commands |
| /usr | User programs |
| /root | Root user home folder |
| /dev | Device files |
| /proc | Running processes |

## Important Folders for Hackers
### /etc/passwd
- Contains all user accounts
- Readable by everyone
- Target for reconnaissance

### /etc/shadow
- Contains encrypted passwords
- Only root can read it
- Target for privilege escalation

### /var/log
- System logs — tracks everything
- Check for suspicious activity
- Evidence of previous attacks

### /tmp
- Temporary files
- Writable by anyone
- Hackers often use this folder
- Cleared on reboot

### /root
- Root user home directory
- Highest privilege folder
- Main target for attackers

## Linux vs Windows Paths
Windows: C:\Users\Saad\Desktop
Linux: /home/saad/Desktop

No drive letters in Linux!
Everything starts from / (root)

## Follow on Instagram
@code.shield_ for full episode!
