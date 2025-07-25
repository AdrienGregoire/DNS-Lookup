# DNS Lookup Tool (Python)

A Python tool for performing DNS lookups: IP addresses, hostnames, aliases, etc.

---

## Project Structure

```
dns_lookup/
|── SRC/
    ├── scan.py
    └── lookup.py
├── main.py
```

---

## Features

- Get main IP address of a domain
- Get all associated IP addresses
- Reverse lookup to get hostname
- Get DNS aliases

---

## ▶Usage

### Run the program

```bash
python3 main.py
```

This will perform a DNS lookup on `google.com`. Soon, you will choose your domain name.

---

## Function Descriptions

### `get_ip(domain)`
> Returns the main IPv4 address for the domain.

### `get_ipx(domain)`
> Returns all IP addresses associated with the domain.

### `get_host(ip)`
> Resolves a hostname from an IP address.

### `get_aliases(domain)`
> Retrieves DNS aliases for the domain.

---

## Dependencies

- Python 3.x
- Built-in `socket` module

---

## 💡 Example Output

```
IP: soon
All IPs: soon
Host: soon
Aliases: soon
```

---

## 📜 License

MIT - Free to use, modify, and redistribute.