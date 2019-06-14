from pyfiglet import Figlet
from termcolor import colored
from . import ftpbrute, nmtool,nspython, proxifetch, helper, hash, metadata, dirbrute, menu, metadata, xploitsearch
import os

try:
    os.system('clear')
    menu.welcome()
    print(colored('='*60,"cyan"))
    banner = """
             Alfred is a penetration testing toolkit while introduces the user
             to tools which are most commonly used to pentesting and CTFs and
             some other tools which will be handy."""
    print(colored(banner,"blue"))
    
    def main():
        term = input("[Alfred]>").lower()
        if term == "nmtool":
            nmtool.main()
            main()
        elif term == "nspython":
            nspython.main()
            main()
        elif term == "hash":
            hash.main()
            main()
        elif term == "xploitsearch":
            xploitsearch.main()
            main()
        elif term == "proxifetch":
            proxifetch.main()
            main()
        elif term == "metadata":
            metadata.main()
            main()
        elif term == "ftpbrute":
            ftpbrute.main()
            main()
        elif term == "dirbrute":
            dirbrute.main()
            main()
        elif term == "help":
            helper.main()
            main()
        elif term == "tools":
            menu.tools()
            main()
        elif term == "exit":
            exit(0)
        else:
            print(colored("[!]Unknown Command, if it's valid then it'll be added soon","red",attrs=['reverse','blink']))
            main()
except KeyboardInterrupt:
    print(colored("Exiting.......","green"))
    exit(0)

if __name__ == "__main__":
    main()
