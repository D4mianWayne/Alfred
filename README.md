# Alfred
![](https://github.com/D4mianWayne/Alfred/blob/master/Snaps/Screenshot%20from%202019-06-13%2017-27-23.png)

Alfred is a Pentesting Framework for Beginners.

### Available Tools:

* `Nmtool`- Nmap Scan Tool
* `metadata` - Extract metadata of PDF and Image
* `dirbrute` - bruteforce directories and files
* `ftpbrute` - bruteforce ftp service for credentials
* `hash` - check hashvalue from hashtoolkit
* `nspython` - DNS querying
* `proxifetch` - Fetch proxy from API
* `ddos` - DDoS a host

### Installation

* Clone the repository
    - git clone https://github.com/D4mianWayne/Alfred

* `sudo apt-get update`
* `python3 setup.py install`
* `Alfred`

**NOTE**: Apart from python packages it needs nmap and libimage-exiftool-perl.

Show your love [here](https://saythanks.io/to/D4mianWayne)

### Usage
##### `nmtool`
`[Alfred]>nmtool
 [*]Scan for Open Ports on Host
                  ==============================
                  1: TCP Scan
                  2: UDP Scan
                  3: Verson Scan
                  4: TCP SYN Scan
                  5: Xmas Scan
                  6: Checks Default Scripts for Vulnerlability
Enter Host address: 10.0.0.72
Which type of scan?: 3
Do you want to enable OS Detection?: no
[+]Scanning 10.0.0.72

Starting Nmap 7.60 ( https://nmap.org ) at 2019-06-13 20:18 IST
Nmap scan report for 10.0.0.72
Host is up (0.23s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.6 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.7 ((Ubuntu))
6667/tcp open  irc     ngircd
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=6/13%OT=22%CT=1%CU=42096%PV=Y%DS=2%DC=I%G=Y%TM=5D02625
OS:8%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=109%TI=Z%CI=I%TS=8)OPS(O1=M
OS:54DST11NW6%O2=M54DST11NW6%O3=M54DNNT11NW6%O4=M54DST11NW6%O5=M54DST11NW6%
OS:O6=M54DST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(R=Y%
OS:DF=Y%T=40%W=6903%O=M54DNNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=
OS:0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF
OS:=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=
OS:%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%
OS:IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops
Service Info: Host: irc.example.net; OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 41.70 seconds`
* `metadata` - Extract metadata of PDF and Image
* `dirbrute` - bruteforce directories and files
* `ftpbrute` - bruteforce ftp service for credentials
* `hash` - check hashvalue from hashtoolkit
* `nspython` - DNS querying
* `proxifetch` - Fetch proxy from API
* `ddos` - DDoS a host



