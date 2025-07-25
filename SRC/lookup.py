import socket

def get_ip(string):
    try:
        ip = socket.gethostbyname(string)
        return ip
    except Exception:
        return False

def get_ipx(string):
    try:
        data = socket.gethostbyname_ex(string)
        ipx = repr(data[2])
        return ipx
    except Exception:
        return False

def get_host(ip):
    try:
        data = socket.gethostbyaddr(ip)
        ip = repr(data[0])
        return ip
    except Exception:
        return False

def get_aliases(string):
    try:
        data = socket.gethostbyname_ex(string)
        aliases = repr(data[1])
        return aliases
    except Exception:
        return False
