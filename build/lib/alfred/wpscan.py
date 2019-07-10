import os

def _wpscan(url):
    os.system("wpscan --url {} -e -t 10 -o {}.txt".format(url,url))


def main():
    print("""
    ==================== WordPress Scanner ====================
    It uses wpscan as the tool for scanning by providing all automated
    enumeration already.
    Usage: 
    Type wpscan to invoke it and after that enter the host address.
    ============================================================
    ================= Enabled Options ======================
    -e: It performs every enumeration i.e. users, themes, vulnerable plugin etc.
    -o: For saving output in <host>.txt
    --url: Host input
    -t: Threaded Process (Default is set to 10)""")
    host = input("Enter Host: ")
    _wpscan(host)