##
## SOLO PROJECT, 2025
## lookup.py
## File description:
## all get-functions
##

import socket

def get_ip(domain : str) -> str | bool:
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception:
        return False

def get_all_ips(domain : str) -> str | bool:
    try:
        data = socket.gethostbyname_ex(domain)
        all_ips = repr(data[2])
        return all_ips
    except Exception:
        return False

def get_host(ip : str) -> str | bool:
    try:
        data = socket.gethostbyaddr(ip)
        ip = repr(data[0])
        return ip
    except Exception:
        return False

def get_aliases(domain : str) -> str | bool:
    try:
        data = socket.gethostbyname_ex(domain)
        aliases = repr(data[1])
        return aliases
    except Exception:
        return False
