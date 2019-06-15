import requests
import json


def get(n):
    for i in range(n):
        r = requests.get("https://api.getproxylist.com/proxy")
        if r.status_code == 200:
            data = json.loads(r.text)
            print("=" * 20)
            print("[+] Data about proxy:\n")
            print("IP: ", data.get("ip"))
            print("Port: ", data.get("port"))
            print(f"Anonymity: {data.get('anonymity')} \nType: {data.get('protocol')}")
        else:
            print("[-] API is not responding!")
            break


def main():
    try:
        n = int(input("[?] Amount of proxy: "))
        get(n)
    except:
        print("[?] Error encountered!")
