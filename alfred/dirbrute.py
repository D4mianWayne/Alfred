import threading
import urllib.request
import queue
from termcolor import colored

threads = 50
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"


def build_word_list(word_list_file, resume_word=None):
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
            try:
                successful_attempts = []
                response = urllib.request.urlopen(request)
                if len(response.read()):
                    if response.url not in successful_attempts:
                        successful_attempts.append(response.url)
                        print(colored(f"\n[+] {response.code} => {response.url}", "cyan"))
            except:
                pass


def main():
    try:
        print("#" * 25)
        print(colored("[+] Brute-force directory/file check", "magenta"))
        word_list = input("Enter wordlist: ")
        url = input("Enter URL: ")
        extensions = input("Enter file extensions (You can also leave it empty): ")
        extensions = list(map(str, extensions.split()))
        word_list = build_word_list(word_list)
        if word_list:
            print(colored("[+] Word queue created.", "green"))
            if extensions:
                print(colored("[+] Starting...", "blue"))
                print(colored("[*]" + ', '.join(extensions), "yellow"))
                for i in range(threads):
                    t = threading.Thread(target=brute_forcer, args=(word_list, url, extensions))
                    t.start()
            else:
                print(colored("[+] Starting...", "blue"))
                for i in range(threads):
                    t = threading.Thread(target=brute_forcer, args=(word_list, url, extensions))
                    t.start()
        else:
            print(colored("[!] Unable to create word queue.", "red"))
    except Exception as E:
        print(E)
        print(colored("[!] Something went wrong.", "red"))
