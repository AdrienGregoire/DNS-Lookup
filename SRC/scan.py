import SRC.lookup

def dns_lookup(string):
    ip = SRC.lookup.get_ip(string)
    all_ips = SRC.lookup.get_all_ips(string)
    host = SRC.lookup.get_host(ip)
    aliases = SRC.lookup.get_aliases(string)
    print(ip)
    print(all_ips)
    print(host)
    print(aliases)
    return 0