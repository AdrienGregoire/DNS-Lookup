import SRC.lookup

def dns_lookup(string):
    ip = SRC.lookup.get_ip(string)
    ipx = SRC.lookup.get_ipx(string)
    host = SRC.lookup.get_host(ip)
    aliases = SRC.lookup.get_aliases(string)
    print(ip)
    print(ipx)
    print(host)
    print(aliases)
    return 0