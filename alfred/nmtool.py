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
        os.system("nmap {} -O -Pn {}".format(table[s_type],host))
    else:
        os.system("nmap {} -Pn {}".format(table[s_type],host))

def main():
    print(colored('''
                  [*]Scan for Open Ports on Host
                  ==============================
                  1: TCP Scan
                  2: UDP Scan
                  3: Verson Scan
                  4: TCP SYN Scan
                  5: Xmas Scan
                  6: Checks Default Scripts for Vulnerlability''',"yellow"))  
    try:
        host = input("Enter Host address: ")
        choice = int(input("Which type of scan?: "))
        os_detection = input("Do you want to enable OS Detection?: ")
        if os_detection.lower() == "yes" or "y":
            nmap(host,choice,True)
        else:
            nmap(host,choice)
    except:
        print(colored("[!]Something went wrong, try again","red",attrs=["reverse","underline"]))
    

