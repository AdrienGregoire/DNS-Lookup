##
## SOLO PROJECT, 2025
## scan.py
## File description:
## call all get-functions
##

import SRC.lookup

def dns_lookup(domain):
    ip = SRC.lookup.get_ip(domain)
    all_ips = SRC.lookup.get_all_ips(domain)
    host = SRC.lookup.get_host(ip)
    aliases = SRC.lookup.get_aliases(domain)
    print("\n" + "=" * 10 + " DNS LOOKUP " + "=" * 10)
    print(f"Domain/IP   : {domain}")
    print(f"IP Address  : {ip}")
    print(f"All Ips     : {all_ips}")
    print(f"Hostname    : {host}")
    print(f"Aliases     : {aliases}")
    print("=" * 33)
    return 0
