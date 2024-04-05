import requests
import time
import os
from colorama import *
import ctypes

logo = f'''{Fore.LIGHTMAGENTA_EX}            .-.
           ((`-)
            \\
             \\
      .="""=._))
     /  .,   .'
    /__(,_.-'
   `    /|
       /_|__
         | `))
         |
         
{Fore.LIGHTRED_EX}Made by GoT Flamingo
{Fore.LIGHTYELLOW_EX}Github.com/gotflamingo 
'''


ctypes.windll.kernel32.SetConsoleTitleW("Auto Loot box | Github.com/gotflamingo | Made By GoT Flamingo")
os.system("cls")
print(logo)
TOKEN = input(f"{Fore.LIGHTWHITE_EX}Enter {Fore.LIGHTGREEN_EX}Discord Token:{Fore.LIGHTWHITE_EX} ")

headers = {
    'accept': '*/*',
    'accept-language': 'en,en-US;q=0.9,da-DK;q=0.8,da;q=0.7',
    'authorization': f'{TOKEN}',
    'origin': 'https://discord.com',
    'referer': 'https://discord.com/channels/@me',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'da',
    'x-discord-timezone': 'Europe/Copenhagen',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tLz9kaXNjb3JkdG9rZW49T0RJNE5qWXhNekkzTVRneU1qazVNVGMyLkc3S0hXbC4wMWlEQnNkczVJQ29zVEVLZUNIRGRpUVlobXkxNmFWNzZPNTVFNCIsInJlZmVycmluZ19kb21haW4iOiJkaXNjb3JkLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyODE4MDksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
}



while True:
    response = requests.post('https://discord.com/api/v9/users/@me/lootboxes/open', headers=headers)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loot box | Github.com/gotflamingo | Made By GoT Flamingo")
    if response.status_code == 200:
        print(f"{Fore.LIGHTGREEN_EX}Loot box successfully opened.")
    else:
        ctypes.windll.kernel32.SetConsoleTitleW("Auto Loot box | Github.com/gotflamingo | Made By GoT Flamingo")
        print(f"{Fore.LIGHTRED_EX}Failed to open loot box. Status code: {response.status_code}")
    time.sleep(5)
