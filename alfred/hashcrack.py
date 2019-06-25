import requests
import json
import re
from termcolor import colored

def hash_check(string:str):
    print(colored("[*]Looking for hash on hashtoolkit database.","cyan",attrs=['reverse','blink']))
    if len(string) == 32:
        r = requests.get("https://md5.pinasthika.com/api/decrypt?value="+string)
        if r.status_code == 200:
            data = json.loads(r.text).get("result")
            if data:
                print("[+] Hash Found: {}".format(data))
            else:
                print("[-] Not Found!")
        else:
            print("[-] Unknown Issue Occured!")
    elif len(string) == 40:
        r = requests.get("https://hashtoolkit.com/reverse-sha1-hash?hash="+string).text
        try:
            match = re.findall(r"<span>\w+</span>",r)[1]
            print(colored("[+] Found Hash: {}".format(match[6:-7]),"green"))
        except:
            print(colored("[-] Nothing Found in the Database!","red"))
    else:
        print("!Unable to search for this hash since MD5 & SHA1 are supported as of now.")


def main():
    print("=====================================================================================")
    string = input("Enter String: ")
    hash_check(string)
    print("================================= Done ==============================================")



    
