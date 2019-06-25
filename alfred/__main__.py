from pyfiglet import Figlet
from termcolor import colored
import ftpbrute, wpscan, nmap,nspython, hashcrack, metadata, dirbrute, metadata, sploitsearch
import os

def helper():
    return """
    ===========Available Tools==============
    =========================================
    [*]hashcrack 
    [*]dirb
    [*]ftpbrute
    [*]nmap
    [*]nsloookup
    [*]exifdata
    [*]sploitsearch
    [*]wpscan
    [*]help
    ========================================="""

try:
    os.system('clear')
    print("""
    ===================================  ALFRED  =======================================
    ====================================================================================
    Name: Alfred
    Version: 1.0
    Created by: Ayushman Dubey (@d4mianwayne)
    Link: https://github.com/d4mianwayne/Alfred
    =====================================================================================""")
    print(helper())

    def main():
        cmd = input("\n<alfred>")
        if cmd == "ftpbrute":
            ftpbrute.main()
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
        else:
            print("Unknown Command!")
            main()
except KeyboardInterrupt:
    print(colored("Exiting.......","green"))
    exit(0)

if __name__ == "__main__":
    main()
