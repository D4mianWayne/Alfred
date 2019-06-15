from terminaltables import SingleTable
from termcolor import colored


def main():
    table_content = [
        ['Command', 'Description'],
        ['help', 'Displays current menu'],
        ['tools', 'Shows available tools'],
        ['xploitsearch', 'Search exploits and get info'],
        ["exit", "Exit the framework"]
    ]
    table = SingleTable(table_content)
    print(colored(table.table, "cyan"))
