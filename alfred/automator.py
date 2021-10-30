import socket
import subprocess
from context import ctx


default_wordlist = ctx.dirbuster_wordlist   

def check_hostname(hostname):
    try:
        if socket.gethostbyname(hostname) == hostname:
            print('{} is a valid IP address'.format(hostname))
        elif socket.gethostbyname(hostname) != hostname:
            print('{} is a valid hostname'.format(hostname))
    except socket.gaierror:
        print("Something is wrong")


def nmap_scan(hostname):
    try:
        if check_hostname(hostname):
            subprocess.run(["nmap", "-sV", "-sC", "-A", "-oX", hostname])
            # Need to parse XML output and then pass the open ports to another function
    except Exception as E:
        print(f"Error: {E}")

def gobuster(hostname, open_port_type):
    try:
        if open_port_type == "https":
            subprocess.run(["gobuster", "dir", "-u", f"https://{hostname}", "-w", default_wordlist, "-o", f"gobuster_{hostname}_https.out"])
        else:
            if open_port_type == "http":
                subprocess.run(["gobuster", "dir", "-u", f"https://{hostname}", "-w", default_wordlist, "-o", f"gobuster_{hostname}_http.out"])
    except Exception as E:
        print(f"Error: {E}")