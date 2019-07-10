from itertools import *
import base64
import codecs


def xor():
    s1 = input("Enter 1st string: ")
    s2 = input("Enter 2nd string: ")
    if len(s1) != len(s2):
        print("[!]Strings lengths are not equal, you should use repeating key xor.")
    else:
        print(''.join(chr(ord(i)^ord(j)) for i,j in zip(s1,s2)))
    
def repeatxor():
    s1 = input("Enter string: ")
    key = input("Enter key: ")
    print(''.join(chr(ord(i)^ord(j)) for i,j in zip(s1,cycle(key))))

def base64enc():
    s1 = input("Enter string: ")
    s1 = bytes(s1,"utf-8")
    print((base64.b64encode(s1)).decode("utf-8"))

def base64dec():
    try:
        s1 = input("Enter string: ")
        s1 = bytes(s1,"utf-8")
        print((base64.b64decode(s1)).decode("utf-8"))
    except:
        print("[!]Padding is not valid.")

def rot13():
    s = input("Enter string: ")
    print(codecs.encode(s, "rot-13"))

def xorbrute():
    s1 = input("Enter string: ")
    for i in range(128):
        s = ''.join(chr(ord(j)^i) for j in s1)
        print("Key: {}: {}".format(i,s))

def main():
    print("""
         +-------------------------+
         + 1: Xor                  +
         ---------------------------
         + 2: Repeating Xor        +
         ---------------------------
         + 3: Xor Bruteforce       +
         ---------------------------
         + 4: ROT13                +
         ---------------------------
         + 5: Base64 Encoding      +
         ---------------------------
         + 6: Base64 Decoding      +
         ---------------------------""")
    c = input("Enter: ")
    tools = {"1": xor, "2":repeatxor, "3": xorbrute, "4": rot13, "5": base64enc, "6": base64dec}
    try:
        tools[c]()
    except:
        print("[!]Invalid Command.")
