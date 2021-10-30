import os
from termcolor import colored
import socket
import re

def url2ip(url):
    return socket.gethostbyname(url)

def nmap(host,s_type,os_detection=False):
    print(colored("[+]Scanning {}".format(host),"green",attrs=["reverse","blink"]))
    table = {1:"-sT",2:"-sU",3:"-sV",4:"-sS",5:"-sX",6:"-sC"}
    if os_detection:
        os.system("nmap {} -sC -O -Pn {}".format(table[s_type],host))
    else:
        os.system("nmap {} -sC -Pn {}".format(table[s_type],host))

def main():
    print('''
    ============== Nmap ================
    Note: It relies on nmap, since it teaches begineers about it's usage.
    =============== Arguments =================
    -sT, -sV, -sU, -sS, -sX: TCP, UDP, Version, TCP SYN, Xmas
    -A: Enable OS detection, version detection, script scanning, and traceroute 
    -Pn: Treat all hosts as online
    -sC: Run all lua scripts for vulnerabilty scanning
    ============================================
    1: TCP Scan
    2: UDP Scan
    3: Version Scan
    4: TCP SYN Scan
    5: Xmas Scan
    ======================================
    Usage: Type nmap to invoke and after that enter host then the number shown above to scan for respective scan.
    ======================================
    Example:
    <Alfred>nmap
    Enter Host: <ip address>
    Scan Type: <index of scan>''')  
    try:
        host = input("Enter Host address: ")
        choice = int(input("Which type of scan?: "))
        nmap(host,choice)
    except:
        print(colored("[!]Error Occured, try again","red",attrs=["reverse","underline"]))
    

