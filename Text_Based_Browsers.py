import requests as requests
import os
import sys
from bs4 import BeautifulSoup
from collections import deque
from colorama import Fore


# write your code here
dir = sys.argv[1]
my_stack = deque()


def save_file(url, d, file):
    if url.startswith('https://'):
        url = url.lstrip('https://')
    url = url.split('.')[0]
    f = open(f'./{d}/{url}', 'w', encoding='utf-8')
    f.write(file)
    f.close()


if not  (os.access(dir, os.F_OK)):
   os.mkdir(dir)

while True:
    url = input()
    if (url not in ["back", "exit"]) and url.count('.') > 0:
        if not url.startswith('https://'):
            url = 'https://' + url

        my_stack.append(url.split('https://')[1])
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                page_content = resp.content
                soup = BeautifulSoup(page_content, 'html.parser')
                for tag in soup.find_all(True):
                    if tag.name == 'a':
                        # print('a')
                        print(Fore.BLUE + f'{tag.getText()}')
                    else:
                        print(tag.getText())
                save_file(url, dir, soup.get_text())
        except requests.exceptions.ConnectionError as err:
            print(f'Invalid URL: {err}')

    else:
        if url == 'exit':
            break

        elif url == "back":
            # print(my_stack)
            if len(my_stack) > 0:
                docs = my_stack.popleft().split('.')[0]
                file = open(f'{dir}/{docs}')
                print(file.read())
                # print(file.closed)
                # print(file.close())
                file.close()
                continue

        else:
            print('Invalid URL')






# while (url := input()) != 'exit':
#     if not url.startswith('https://'):
#         url = 'https://' + url
#     r = requests.get(url)
#     print(r.content)
