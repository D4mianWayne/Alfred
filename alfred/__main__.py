from pyfiglet import Figlet
from termcolor import colored
from . import ftpbrute, wpscan, nmap, nspython, hashcrack, metadata, dirbrute, metadata, sploitsearch, crypto
import os

def helper():
    return """
    ===========Available Commands ==============
    ------------------------
    |       Tools          |
    ------------------------
    |  [*]hashcrack        |
    |  [*]dirb             |
    |  [*]ftpbrute         |
    |  [*]nmap             |
    |  [*]nsloookup        |
    |  [*]exifdata         |
    |  [*]sploitsearch     |
    |  [*]wpscan           |
    |  [*]crypto           |
    ------------------------
    |       Other          |
    ------------------------
    |  [*]help             |
    |  [*]assist           |
    ------------------------"""

try:
    os.system('clear')
    print("""
    ===============  ALFRED  =================
    ===========================================
    Name: Alfred
    Version: 1.0.1
    Created by: Ayushman Dubey (@d4mianwayne)
    Link: https://github.com/d4mianwayne/Alfred
    ===========================================""")
    print(helper())

    def main():
        cmd = input("\nalfred@assist# ")
        if cmd == "ftpbrute":
            ftpbrute.main()
            main()
        elif cmd == "crypto":
            crypto.main()
            main()
        elif cmd == "dirb":
            dirbrute.main()
        elif cmd == "hashcrack":
            hashcrack.main()
            main()
        elif cmd == "nmap":
            nmap.main()
            main()
        elif cmd == "nslookup":
            nspython.main()
            main()
        elif cmd == "exifdata":
            metadata.main()
            main()
        elif cmd == "sploitsearch":
            sploitsearch.main()
            main()
        elif cmd == "wpscan":
            wpscan.main()
            main()
        elif cmd in ["?","help"]:
            print(helper())
            main()
        elif cmd in ["quit","q","exit"]:
            exit(0)
        else:
            print("Unknown Command!")
            main()
except KeyboardInterrupt:
    print(colored("Exiting.......","yellow"))
    exit(0)

if __name__ == "__main__":
    main()
