import requests
import json
import re
from termcolor import colored

def hash_check(string:str):
    if len(string) == 32:
        r = requests.get("https://md5.pinasthika.com/api/decrypt?value="+string)
        if r.status_code == 200:
            data = json.loads(r.text).get("result")
            if data:
                print(colored("[+] Hash Found: {}".format(data),"green"))
            else:
                print(colored("[-] Not Found!","red"))
        else:
            print("[-] Unknown Issue Occured!")
    else:
        r = requests.get("https://hashtoolkit.com/reverse-hash?hash="+string).text
        try:
            match = re.findall(r"<span>\w+</span>",r)[1]
            print(colored("[+] Found Hash: {}".format(match[6:-7]),"green"))
        except:
            print(colored("[-] Nothing Found in the Database!","red"))
def main():
    try:
        hash = input("Enter Hash String: ")
        if not hash:
            print(colored("[!]Please Enter Hash String!","red"))
        print(colored("[*]Checking Databases for Hash","blue",attrs=["reverse","blink"]))
        hash_check(hash)
    except:
        print(colored("[!]Something went wrong!","red"))

    