import os
import subprocess
from termcolor import colored
from pyfiglet import Figlet
import json


def db_check():
    if not os.path.exists("/usr/share/exploitdb"):
        print("[!] Couldn't find exploit database. Try running install.py again. [!]")
        return

    f = Figlet(font='slant')
    print(f.renderText("     Search"))
    supported_platforms = ['windows', 'linux', 'macos', 'php']
    message = "Platform [{}, all]: ".format(",".join(supported_platforms))
    q1 = input(message).lower()
    if q1 == 'all':
        return ""
    elif q1 in supported_platforms:
        return q1
    else:
        print("[!] Unknown platform '{}'. Use 'all'".format(q1))
        return ""

def main():
    search = db_check()
    xploit = search+" "+input("Search: ")
    print(colored("Running Search....","yellow"))
    data = subprocess.check_output("searchsploit -j {}".format(xploit),shell=True)
    data = json.loads(data)
    print(colored("-"*45+"Exploit"+"-"*45,"yellow"))
    for exploit in data["RESULTS_EXPLOIT"]:
        print(colored("="*60))
        message = ("Title: {Title}"
                   "Platform: {Platform}"
                   "Path: {Path}"
                   "Author: {Author}").format(**exploit)
    print(colored(message,"yellow"))
    print(colored("-"*60))
