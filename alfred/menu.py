from pyfiglet import Figlet
from termcolor import colored
from terminaltables import SingleTable

def welcome():
    banner = Figlet(font="banner3-D")
    print(colored(banner.renderText("Alfred"),"blue"))

def tools():
    f = Figlet(font="dotmatrix")
    print(colored(f.renderText("Tools"),"cyan"))
    print(colored("[*]Enter the name pf the tool to use it","cyan"))
    infotab = [['\nTool','\nDescription'],
        ['nmtool','Scan host for open ports'],
        ['nspython','A DNS querying Tool'],
        ['hash','Checks the value of a given hash from hashtoolkit'],

        ['proxifetch','Fetch proxy from API'],
        ['metadata',"Retrieve Metadata from Image and PDF files"],
        ['ftpbrute',"Bruteforce FTP for credentials recover"],
        ['dirbrute',"Bruteforce Website for files and directory recover"],
        ]
    table = SingleTable(infotab)
    print(colored(table.table,"cyan"))
