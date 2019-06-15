from pyfiglet import Figlet
from termcolor import colored
from terminaltables import SingleTable


def welcome():
    banner = Figlet(font="banner3-D")
    print(colored(banner.renderText("Alfred"), "blue"))


def tools():
    f = Figlet(font="dotmatrix")
    print(colored(f.renderText("Tools"), "cyan"))
    print(colored("[*] Enter the name of the tool to use it", "cyan"))
    infotab = [['Tool', 'Description'],
               ['nmtool', 'Scan host for open ports'],
               ['nspython', 'A DNS querying tool'],
               ['hash', 'Checks the value of a given hash via hashtoolkit'],
               ['ddos', 'DDoS a given host and port'],
               ['proxifetch', 'Fetch proxy from API'],
               ['metadata', "Retrieve Metadata from images and PDF files"],
               ['ftpbrute', "Brute-force FTP for credentials"],
               ['dirbrute', "Brute-force website for files and directories"],
               ]
    table = SingleTable(infotab)
    print(colored(table.table, "cyan"))
