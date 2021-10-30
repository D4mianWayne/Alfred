import PyPDF2
from PyPDF2 import PdfFileReader
import os
from termcolor import colored

def metadata_pdf(filename):
    try:
        pdfile = PdfFileReader(open(filename,"rb"))
        meta = pdfile.getDocumentInfo()
        print(colored("MetaData for {}".format(filename),"yellow"))
        for key,values in meta.items():
            print("[+]{}: {}".format(key,values))
    except:
        pass
def metadata_image(filename):
    try:
        os.system("exiftool "+filename)
    except:
        print("""
        Issue Occured
        ==================================================================================
        Either exiftool not installed or file does not exist in given path!
        ==================================================================================""")
        pass

def main():
    print("""
    ============================== Metadata Extractor ==================================
    
    ====================================================================================
    [*]1:PDF Metadata: It uses Python's PyPDF2 to extract metadata of a PDF.
    [*]2:Image Metadata: It uses the standard Perl's Exiftool package to retreieve metadata
    ====================================================================================
    
    ======================================= Usage ======================================
    After invoking the tool by entering exifdata, enter 1,2 for PDF, image metadata extraction
    respectively.
    <alfred>exifdata
    --snip--
    <alfred>2
    --snip--
    Enter Filename: Basic.jpg
    Metadata for Bsic.jpg
    --snip--
    ======================================================================================""")
    try:
        choice = int(input(">"))
        if choice == 1:
            pdf = input("[-]Enter FileName: ")
            metadata_pdf(pdf)
        elif choice == 2:
            image = input("[-]Enter Filename: ")
            metadata_image(image)
    except:
        print("[!]Wrong Input")
    print(" "*5+"=========================================================================================")
    
