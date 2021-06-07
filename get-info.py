#Get Info With Python
#By AlirezaR00t & Salvator__s
#---------------
import requests,os
from colorama import Fore,Back,Style
#---------------
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
os.system("clear")
print (Fore.RED + """███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼ـAR00tـ┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████""")

username = input(Fore.RED +"enter name: ")
#---------------
req = requests.get('https://twitter.com/'+username, headers=headers)

if '{"value":false}' in req.text:

    i = (Fore.GREEN + 'https://twitter.com/'+username)

    print("[x] Not Found : "+i)

else:

    i = (Fore.GREEN + 'https://twitter.com/'+username)

    print(Fore.BLUE + "[+] Found : "+i+" +")

#---------------

req = requests.get('https://www.pinterest.com/'+username, headers=headers)

if req.status_code == 200:

    i = (Fore.GREEN + 'https://www.pinterest.com/'+username)

    print(Fore.BLUE + "[+] Found : "+i+" +")

else:

    i = (Fore.GREEN + 'https://www.pinterest.com/'+username)

    print(Fore.RED + "[x] Not Found : "+i)

#---------------

req = requests.get('https://github.com/'+username, headers=headers)

if req.status_code == 200:

    i = (Fore.GREEN + 'https://github.com/'+username)

    print(Fore.BLUE + "[+] Found : "+i+" +")

else:

    i = ('https://github.com/'+username)

    print(Fore.RED + "[x] Not Found : "+i)

#---------------

req = requests.get('https://www.instagram.com/'+username, headers=headers)

if req.status_code == 200:

    i = (Fore.GREEN + 'https://www.instagram.com/'+username)

    print(Fore.BLUE + "[+] Found : "+i+" +")

else:

    i = (Fore.GREEN + 'https://www.instagram.com/'+username)

    print(Fore.RED + "[x] Not Found : "+i)

#---------------

req = requests.get('https://steamcommunity.com/id/'+username, headers=headers)

if req.status_code == 200:

    i = (Fore.GREEN + 'https://steamcommunity.com/id/'+username)

    print(Fore.BLUE + "[+] Found : "+i+" +")

else:

    i = (Fore.GREEN + 'https://steamcommunity.com/id/'+username)

    print(Fore.RED + "[x] Not Found : "+i)

#---------------

req = requests.get('https://soundcloud.com/'+username, headers=headers)

if req.status_code == 200:

    i = (Fore.GREEN + 'https://soundcloud.com/'+username)

    print(Fore.BLUE + "[+] Found : "+i+" +")

else:

    i = (Fore.GREEN + 'https://soundcloud.com/'+username)

    print(Fore.RED + "[x] Not Found : "+i)
