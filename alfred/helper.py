from terminaltables import SingleTable
from termcolor import colored

def main():
    table_content = [
        ['Command','Description'],
        ['help','Display current menu'],
        ['tools','Shows Available Tools'],
        ['search','Search Exploits and get info'],
        ["exit","Exit Framework"]
    ]
    table = SingleTable(table_content)
    print(colored(table.table,"cyan"))

