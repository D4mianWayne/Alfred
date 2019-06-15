import PyPDF2
from PyPDF2 import PdfFileReader
import os
from termcolor import colored


def metadata_pdf(filename):
    try:
        pdffile = PdfFileReader(open(filename, "rb"))
        meta = pdffile.getDocumentInfo()
        print(colored("MetaData for {}".format(filename), "yellow"))
        for key, values in meta.items():
            print("[+]{}: {}".format(key, values))
    except:
        pass


def metadata_image(filename):
    try:
        os.system("exiftool " + filename)
    except:
        print(colored("Either exiftool is not installed or file does not exist in given path", "red"))
        pass


def main():
    print(colored("[*] 1:PDF Metadata\n[*] 2:Image Metadata", "yellow"))
    choice = int(input(">"))
    if choice == 1:
        pdf = input("[-] Enter fileName: ")
        metadata_pdf(pdf)
    elif choice == 2:
        image = input("[-] Enter filename: ")
        metadata_image(image)
    else:
        print(colored("[!] Wrong input", "red"))
