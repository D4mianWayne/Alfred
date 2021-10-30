import os
import subprocess
from termcolor import colored
from pyfiglet import Figlet
import json


def check_db():
    if not os.path.exists("/usr/share/exploitdb"):
        print("[!]Unable to find the database.")
        return 
    return 

    platforms = ["linux","windows","macos"]
    message = input("Platform [{}, all]: ".format(''.join(platforms)).lower())
    if message == "all":
        return ""
    elif message in platforms:
        return message
    else:
        print("[!]Unknown Platform, use all command.")

def main():
    print("""
    =========================== Searchsploit ===============================
    Serchsploit is a CMD tool which is used to search exploits from Offensive 
    Security Exploit Database.
    ========================================================================

    ========================== Enabled Options =============================
    j: This returns the info about the exploit in json(Javascript Object Notation)
    format.
    Platforms: macos, windows, linux
    ========================================================================

    ============================== Usgae ===================================
    <alfred>searchsploit
    Enter Platform: linux (You can leave it blank for all platform search)
    Search: Buffer Overflow 
    =========================================================================
    """)
    search = check_db()
    xploit = search+(input("Search: "))
    print("[*]Searchng....")
    data = subprocess.check_output("searchsploit -j {}".format(xploit),shell=True)
    data = json.loads(data)
    print(colored("-"*45+"Exploit"+"-"*45,"yellow"))
    for exploit in data["RESULTS_EXPLOIT"]:
        print(colored("="*60))
        message = ("\nTitle: {Title}"
                   "\nPlatform: {Platform}"
                   "\nPath: {Path}"
                   "\nAuthor: {Author}").format(**exploit)
        print(message)
        print("-"*60)
