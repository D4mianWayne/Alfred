import threading
import urllib.request
import queue
from termcolor import colored

threads = 10
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"
resume = False

def build_word_list(word_list_file, resume_word):
    fd = open(word_list_file, "rb")
    word_list = fd.readlines()
    fd.close()

    if len(word_list):
        word_queue = queue.Queue()
        if not resume_word:
            for word in word_list:
                word = word.rstrip().decode("utf8")
                word_queue.put(word)
        else:
            resume_found = False
            for word in word_list:
                word = word.rstrip().decode("utf8")
                if resume_found:
                    word_queue.put(word)
                if word == resume_word:
                    resume_found = True
        return word_queue
    return None


def brute_forcer(word_queue, target_url, extensions):
    """Takes the word queue and builds an attempt list for each attempt. Then, each entry
       in the attempt list (brute) is tried against the target URL/path. If the response
       is successful, we print the output and add to our successful attempts list.
    """
    while not word_queue.empty():
        attempt_list = []
        attempt = word_queue.get()

        if "." in attempt:
            attempt_list.append("/" + attempt)
            if extensions:
                for extension in extensions:
                    attempt_no_extension = attempt.split(".")[0]
                    attempt_extension = attempt_no_extension + extension
                    if attempt != attempt_extension:
                        attempt_list.append("/" + attempt_extension)
            else:
                attempt_list.append("/" + attempt)
        else:
            attempt_list.append("/" + attempt + "/")

        for brute in attempt_list:
            url = target_url + brute
            headers = {}
            headers["User-Agent"] = user_agent
            request = urllib.request.Request(url, headers=headers)
            successful_attempts = []
            try:
                response = urllib.request.urlopen(request)
                if len(response.read()):
                    if response.url not in successful_attempts:
                        successful_attempts.append(response.url)
                        print("[{}] => {}".format(response.code,response.url))
            except:
                pass

def main():
    try:
        print("""
        =================================================================================
        ============================ Dirbuster: Python ==================================
        It's a forced browsing script written in python, It uses bunch of words from the file
        and attempt to discover directories and files on the basis of words.
        =================================================================================
        =============================== Example Inputs ===================================
        Url: http://10.0.0.2
        Wordlist: all.txt
        Extensions: .php,.xml
        ==================================================================================""")
        wordlist = input("Enter Wordlist: ")
        url = input("Enter Url: ")
        extensions = input("Enter File Extensions {You can also leave it empty}: ")
        extensions = list(map(str,extensions.split(",")))
        word_list = build_word_list(wordlist,resume)
        print("""
        =================================================================================
        [*]Threads: 10
        [*]User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0
        [*]Wordlist: {}
        [*]URL: {}
        [*]extensions: {}
        ==================================================================================""".format(wordlist,url,extensions))
        if word_list:
            print(colored("[+]Word Queue Created.","green"))
            if extensions != ['']:
                print("====================== Starting ======================")
                for _ in range(threads):
                    t = threading.Thread(target=brute_forcer,args=(word_list,url,extensions))
                    t.start()
            else:
                print("====================== Starting ======================")
                for _ in range(threads):
                    t = threading.Thread(target=brute_forcer,args=(word_list,url,extensions))
                    t.start()
        else:
            print("Unable to create word queue.")
    except Exception as E:
        print(E)
        print("===================== Something went wrong ============================")

