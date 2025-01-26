# ghost.htb
LDAP Injection Script for intranet.ghost.htb:8008

This script is designed to perform an LDAP injection attack on the login page of intranet.ghost.htb:8008. It brute-forces the password for the gitea_temp_principal account by exploiting the LDAP query structure.

## Requirements 
```
pip install requests pwn
```
## Usage
```
python Bruter.py
```
[![asciicast](https://asciinema.org/a/mwhh1d9HWpWUbpJqo3mhMqn8X.svg)](https://asciinema.org/a/mwhh1d9HWpWUbpJqo3mhMqn8X)
