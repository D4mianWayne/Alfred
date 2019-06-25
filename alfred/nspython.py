import os
from termcolor import colored

def formaturl(url):
    return url.replace("https://","").replace("http://","").replace("www.","")

def color(string):
    return colored(string,"blue")
def nslookup(url):
    url = formaturl(url)
    print(color("[+]Reverse DNS lookup!"))
    os.system("nslookup "+url)

def nslookup_record(url,rec="mx"):
    url = formaturl(url)
    print(color("[*]Querying {} for {} records.".format(url,rec)))
    os.system("nslookup -type={} {}".format(rec,url))

def records_all(url):
    url = formaturl(url)
    print(color("[*]Querying all of the available DNS records of {}".format(url)))
    os.system("nslookup -type=any {}".format(url))

def main():
    print(colored("[*]Uses nslookup to query DNS","blue"))
    print(color("""
                1:[*]Reverse DNS Query
                2:[*]Record Query (Default MX Record)
                3:[*]All of the available DNS Query
                """))
    try:
        choice = int(input("> "))
        if choice == 1:
            url = input("Enter host: ")
            nslookup(url)
        elif choice == 2:
            url = input("Enter host: ")
            rec = input("Enter Type: ")
            if rec:
                nslookup_record(url,rec)
            else:
                nslookup_record(url)
        elif choice == 3:
            url = input("Enter Host: ")
            records_all(url)
        else:
            print(colored("[!]Wrong Input.","red"))
    except:
        print(colored("[!]Wrong Input!","red"))


if __name__ == "__main__":
    main()
