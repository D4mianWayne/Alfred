import os
from termcolor import colored
import socket
import re


def url2ip(url):
    return socket.gethostbyname(url)


def nmap(host, s_type, os_detection=False):
    print(colored("[+]Scanning {}".format(host), "green", attrs=["reverse", "blink"]))
    table = {1: "-sT", 2: "-sU", 3: "-sV", 4: "-sS", 5: "-sX", 6: "-sC"}
    if os_detection:
        os.system(f"nmap {table[s_type]} -O -Pn {host}")
    else:
        os.system(f"nmap {table[s_type]} -Pn {host}")


def main():
    print(colored('''
[*] Scan for Open Ports on Host
==============================
1: TCP Scan
2: UDP Scan
3: Version Scan
4: TCP SYN Scan
5: Xmas Scan
6: Checks Default Scripts for Vulnerability''', "yellow"))
    try:
        host = input("Enter the host address: ")
        choice = int(input("Enter the type of scan: "))
        os_detection = input("Enable OS detection?: ")
        if os_detection.lower() == "yes" or "y":
            nmap(host, choice, True)
        else:
            nmap(host, choice)
    except:
        print(colored("[!] Something went wrong, please try again", "red", attrs=["reverse", "underline"]))
