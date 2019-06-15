import os
from termcolor import colored


def formaturl(url):
    return url.replace("https://", "").replace("http://", "").replace("www.", "")


def color(string):
    return colored(string, "blue")


def nslookup(url):
    url = formaturl(url)
    print(color("[+] Reverse DNS lookup:"))
    os.system("nslookup " + url)


def nslookup_record(url, rec="mx"):
    url = formaturl(url)
    print(color(f"[*] Querying {url} for {rec} records."))
    os.system(f"nslookup -type={rec} {url}")


def records_all(url):
    url = formaturl(url)
    print(color(f"[*] Querying all of the available DNS records of {url}"))
    os.system(f"nslookup -type=any {url}")


def main():
    print(colored("[*] Uses nslookup to query DNS", "blue"))
    print(color("""
1:[*] Reverse DNS query
2:[*] Record query (Default MX Record)
3:[*] All of the available DNS query
"""))
    try:
        choice = int(input("> "))
        if choice == 1:
            url = input("Enter host: ")
            nslookup(url)
        elif choice == 2:
            url = input("Enter host: ")
            rec = input("Enter type: ")
            if rec:
                nslookup_record(url, rec)
            else:
                nslookup_record(url)
        elif choice == 3:
            url = input("Enter host: ")
            records_all(url)
        else:
            print(colored("[!] Wrong input.", "red"))
    except:
        print(colored("[!] Wrong input", "red"))


if __name__ == "__main__":
    main()
