##
## SOLO PROJECT, 2025
## main.py
## File description:
## the main file of the project
##

from SRC.scan import dns_lookup
import sys

def main():
    try:
        dns_lookup(sys.argv[1])
    except IndexError:
        print("please enter a domain name")
    return 0

if __name__ == "__main__":
    main()
