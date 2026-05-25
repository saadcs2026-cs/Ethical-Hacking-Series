# EP 25 — User Permissions in Linux

## Permission Types
| Symbol | Permission | Value |
|--------|-----------|-------|
| r | Read | 4 |
| w | Write | 2 |
| x | Execute | 1 |
| - | No permission | 0 |

## Permission Sets
Every file has 3 permission sets:
- Owner — the file creator
- Group — users in same group
- Others — everyone else

## Reading Permissions
ls -la shows:
-rwxr-xr-- file.txt

Breaking it down:
- → file type (- = file, d = directory)
rwx → owner: read, write, execute
r-x → group: read and execute
r-- → others: read only

## chmod — Changing Permissions
| Command | Meaning |
|---------|---------|
| chmod 777 file | Everyone full access |
| chmod 755 file | Owner full, others read/execute |
| chmod 600 file | Owner read/write only |
| chmod +x file | Make executable |

## Common Permission Values
777 = rwxrwxrwx (dangerous!)
755 = rwxr-xr-x (standard)
644 = rw-r--r-- (files)
600 = rw------- (private)

## Security Risks
### Misconfigured Permissions
- World writable files — anyone can edit
- SUID files — run as root user
- Weak /etc/shadow permissions

### Always Check During Pen Test
find / -perm -4000 2>/dev/null
→ finds SUID files
→ potential privilege escalation!

## Follow on Instagram
@code.shield_ for full episode!
