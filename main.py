import secrets
from colorama import init, Fore, Back, Style
import random
from time import sleep
init()
print(Fore.RED + '''
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░
'''
)
btc = 31280
btc_all = 0
ask_how_to_work = input("Спрашивать ли о продолжении при нахождении биткоина? Y/N\n=> ")
if "y" in ask_how_to_work.lower():
    work_round = True
else:
    work_round = False
    print("Для остновки - Ctrl+C")
while True: 
    for i in range(random.randint(0,100)):
        sleep(0.1)
        print(Fore.RED +"token:",secrets.token_urlsafe(16),"==> 0.00BTC")
    btc_found = random.uniform(0.1, 1)
    in_usd = btc_found * btc
    print(Fore.GREEN +"token:",f"{secrets.token_urlsafe(16)} ==> {btc_found}BTC ~ {in_usd}USD")
    btc_all += btc_found
    if work_round == True:
        if "y" in input("Продолжить? Y/N\n=> ").lower():
            continue
        else:
            print(f"Заработано: {btc_all}BTC ~ {btc_all*btc}USD")
            print("Пока")
            sleep(1)
            break



