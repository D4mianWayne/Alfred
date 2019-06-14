import os
import subprocess
from termcolor import colored
from pyfiglet import Figlet
import json


def check_db():
    if not os.path.exists("/usr/share/exploitdb"):
        print(colored("[!]Unable to find the database.","red",attrs=["reverse","blink"]))
    return 
    f = Figlet(font="slant")
    print(colored(f.renderText("Search"),"cyan"))
    platforms = ["linux","windows","macos"]
    message = colored(input("Platform [{}]: ".format(''.join(platforms)),"cyan").lower())
    if message == "all":
        return ""
    elif message in platforms:
        return message
    else:
        print(colored("[!]Unknown Platform, use all command."))
        return ""

def main():
    search = check_db()
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
