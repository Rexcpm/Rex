#!/usr/bin/python

import os
import sys
import time
import signal
import random
import requests
from time import sleep
from pyfiglet import figlet_format
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.live import Live
from rich.align import Align
from rich.spinner import Spinner
from rich.progress import track
from pyfiglet import Figlet
from random import randint
import secrets
from chanxreyno import Rexcpm  # Your game logic class

__CHANNEL_USERNAME__ = "𝐂𝐡𝐚𝐧 𝐗 𝐑𝐞𝐲𝐧𝐨 𝐂𝐏𝐌𝟐 𝐓𝐨𝐨𝐥 𝐂𝐡𝐚𝐧𝐧𝐞𝐥"
__GROUP_USERNAME__   = "𝐂𝐡𝐚𝐧 𝐗 𝐑𝐞𝐲𝐧𝐨 𝐂𝐏𝐌𝟐 𝐓𝐨𝐨𝐥 𝐂𝐡𝐚𝐭"

console = Console()
fig = Figlet(font='slant')

# Signal handler with style
def signal_handler(sig, frame):
    console.print("\n[bold red]✖ Exit triggered. Shutting down...[/bold red]")
    time.sleep(0.5)
    console.print("[bold yellow]👋 Goodbye, Hacker.[/bold yellow]")
    sys.exit(0)

# Gradient text rendering
def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')

banner = """
╔════════════════════════════════════════════════════╗
║                                                    ║
║           ╔═══╗───╔╗──────╔═══╗                    ║
║           ║╔═╗║───║║──────║╔═╗║                    ║
║           ║║─╚╬╗─╔╣╚═╦══╦═╣║─╚╬══╦═╦══╗            ║
║           ║║─╔╣║─║║╔╗║║═╣╔╣║─╔╣╔╗║╔╣║═╣            ║
║           ║╚═╝║╚═╝║╚╝║║═╣║║╚═╝║╚╝║║║║═╣            ║
║           ╚═══╩═╗╔╩══╩══╩╝╚═══╩══╩╝╚══╝            ║
║           ────╔═╝║                                 ║
║           ────╚══╝                                 ║
╠════════════════════════════════════════════════════╣
║               ⚡ CyberCPM TOOLS ⚡                 ║
║           Car Parking Multiplayer Utilities        ║
║           Coded by: ɖքʀ•ʟʏռӼ | © 2025              ║
╚════════════════════════════════════════════════════╝
            [ Press Enter to continue ]

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
    print(Colorate.Horizontal(Colors.red_to_yellow, "CPM2 Tools Version: 1.02.4 || Author https://t.me/@DPR_LynX"))
    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
    print("< Wajib Logout Account CPM Sebelum Menggunakan Tools Ini >")

def load_key_data(cpm):
    data = cpm.get_key_data()
    print(Colorate.Horizontal(Colors.green_to_white, "=" * 20 + "[ Users Details ]" + "=" * 21))
    print(f"  >> Key Access  : {data.get('access_key')}")
    print(f"  >> Telegram ID : {data.get('telegram_id')}")
    print(f"  >> Balance     : {'Unlimited' if data.get('is_unlimited') else data.get('coins')}")

def count_saved_cars():
    folder_path = "dataplayer/cars"
    if not os.path.exists(folder_path):
        print("  >> Car Count   : 0")
        return
    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]
    print(f"  >> Car Count   : {len(files)}")

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data', {})
        player_storage = data.get('PlayerStorage', {})
        wallet_data = data.get('WalletData', {})
        if ('Name' in player_storage and
            'LocalID' in player_storage and
            'Other' in player_storage and
            'Slots' in player_storage['Other'] and
            'Money' in wallet_data and
            'Coins' in wallet_data):
            total_slots = player_storage['Other'].get('Slots', 'UNDEFINED')
            print(Colorate.Horizontal(Colors.green_to_white, "=" * 18 + "[ Player Information ]" + "=" * 18))
            print(f"  >> Name        : {player_storage.get('Name', 'UNDEFINED')}")
            print(f"  >> LocalID     : {player_storage.get('LocalID', 'UNDEFINED')}")
            print(f"  >> Money       : {wallet_data.get('Money', 'UNDEFINED')}")
            print(f"  >> Coin        : {wallet_data.get('Coins', 'UNDEFINED')}")
            print(f"  >> Total Slots : {total_slots}")
            cpm.get_all_player_cars()
            count_saved_cars()
        else:
            print("{Fore.RED}  [!] Upss. Sepertinya ada yang salah dengan akun anda, Silakan gunakan akun lain.")
            exit(1)

def prompt_valid_value(content, tag, password=False):
    while True:
        value = input(f"{content}: " if not password else getpass(f"{content}: "))
        if not value or value.isspace():
            print(f"{Fore.RED}  ---[{Style.RESET_ALL} tidak boleh kosong Silakan coba lagi.")
        else:
            return value

def signal_handler(sig, frame):
    print(f'\n{Fore.RED}  ---[ Program dihentikan ]---\n')
    exit(0)

def cariid(urutan):
    for mydatacar in nomercar:
        if mydatacar["urutan"] == urutan:
            return mydatacar["id"]

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner()
        print(Colorate.Horizontal(Colors.green_to_white, "=" * 17 + "[ LOGIN TO CPM ACCOUNT ]" + "=" * 17))
        acc_email = prompt_valid_value(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Email", "Email", False)
        acc_password = prompt_valid_value(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Password", "Password", False)
        acc_access_key = prompt_valid_value(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Access Key", "Access Key", False)
        print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Attempting login... ", end="")
        cpm = Rexcpm(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)

        if login_response != 0:
            if login_response == 100:
                print(f"{Fore.RED}  ACCOUNT NOT FOUND.")
                sleep(2)
                continue
            elif login_response == 101:
                print(f"{Fore.RED}  WRONG PASSWORD.")
                sleep(2)
                continue
            elif login_response == 103:
                print(f"{Fore.RED}  INVALID ACCESS KEY.")
                sleep(2)
                continue
            else:
                print(f"{Fore.RED}  Email or password not recognized!")
                sleep(2)
                continue
        else:
            print(f"{Fore.GREEN} Login Successful.")
            show_progress(f" Loading your data...", duration=2)
            sleep(2)

        while True:
            banner()
            load_key_data(cpm)
            load_player_data(cpm)
            cpm.save_player_slots_collection()
            print(Colorate.Horizontal(Colors.green_to_white, "=" * 25 + "[ MENU ]" + "=" * 25))
            print(f"  [{Fore.GREEN}01{Style.RESET_ALL}] Change Name {Fore.YELLOW}Free")
            print(f"  [{Fore.GREEN}02{Style.RESET_ALL}] Change Money {Fore.YELLOW}3000")
            print(f"  [{Fore.GREEN}03{Style.RESET_ALL}] Finish All Levels Done {Fore.YELLOW}10000")
            print(f"  [{Fore.GREEN}04{Style.RESET_ALL}] Remove Male Face {Fore.YELLOW}3000")
            print(f"  [{Fore.GREEN}05{Style.RESET_ALL}] Remove Female Face {Fore.YELLOW}3000")
            print(f"  [{Fore.GREEN}06{Style.RESET_ALL}] Unlock All Male Attributes {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}07{Style.RESET_ALL}] Unlock All Female Attributes {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}08{Style.RESET_ALL}] Unlock All Animations {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}09{Style.RESET_ALL}] Unlock All Homes {Fore.YELLOW}20000")
            print(f"  [{Fore.GREEN}10{Style.RESET_ALL}] Unlock All Paints {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}11{Style.RESET_ALL}] Unlock All Wheels {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}12{Style.RESET_ALL}] Unlock Brakes {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}13{Style.RESET_ALL}] Unlock Calipers {Fore.YELLOW}15000")
            print(f"  [{Fore.GREEN}14{Style.RESET_ALL}] Unlock Sound Police {Fore.YELLOW}7500")
            print(f"  [{Fore.GREEN}15{Style.RESET_ALL}] Unlock Police {Fore.YELLOW}10000")
            print(f"  [{Fore.GREEN}16{Style.RESET_ALL}] Unlock Bodykits {Fore.YELLOW}10000")
            print(f"  [{Fore.GREEN}17{Style.RESET_ALL}] Unlock Cars {Fore.YELLOW}3000")
            print(f"  [{Fore.GREEN}18{Style.RESET_ALL}] Swap Gearbox AWD {Fore.YELLOW}10000")
            print(f"  [{Fore.GREEN}00{Style.RESET_ALL}] Exit Tool")
            print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
            choice = input(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Select menu [01-18]: ").strip()

            if choice == "00":
                print(f"{Fore.CYAN}  ---[ Thanks for using our tool!\n ---[  Join our Telegram group: @DPR_LynX")
                sys.exit()

            elif choice == "01":
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Enter your new name.")
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Max 50 characters.")
                new_name = prompt_valid_value(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Name", "Name")
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                if 0 < len(new_name) <= 50:
                    if cpm.save_player_name(new_name):
                        show_progress(f" Applying changes...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                else:
                    print(f"{Fore.RED}  Invalid input.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "02":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 3000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Enter your desired amount of money.")
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Max 50,000,000.")
                amount = prompt_valid_value(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Money", "Money")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if amount.isdigit() and 0 < int(amount) <= 50000000:
                        if cpm.save_player_money(amount):
                            show_progress(f" Applying changes...", duration=2)
                            print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                        else:
                            print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                    else:
                        print(f"{Fore.RED}  Invalid amount.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "03":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 10000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Complete all levels.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.levels_done():
                        show_progress(f" Applying...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "04":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 3000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Remove male face.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.face_male():
                        show_progress(f" Removing...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfully!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "05":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 3000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Remove female face.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.face_female():
                        show_progress(f" Removing...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "06":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all male attributes.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.attribute_male():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "07":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all female attributes.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.attribute_female():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "08":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all animations.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_animations_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "09":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 20000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all homes.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_home_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "10":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all paints.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_paints_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "11":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock all wheels.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_wheels_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "12":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock brakes.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_brakes_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "13":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 15000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock calipers.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.unlock_calipers():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)
            
            elif choice == "14":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 7500
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Unlock sound police.")
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                else:
                    print(f"{Fore.CYAN}  ---[{Style.RESET_ALL} Processing... ", end="")
                    if cpm.all_sound_police_unlocked():
                        show_progress(f" Unlocking...", duration=2)
                        print(f"{Fore.GREEN}  ---[{Style.RESET_ALL} Successfuly!")
                    else:
                        print(f"{Fore.RED}  ---[{Style.RESET_ALL} Failed.")
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                sleep(2)

            elif choice == "15":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 10000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 21 + "[ Unlock Police ]" + "=" * 21))
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    sleep(2)
                else:
                    print("  Cars List:")
                    print(namacar)
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    input_ids = input(f"{Fore.CYAN} ---[{Style.RESET_ALL} Input number car: ").strip()
                    if not input_ids:
                        print(f"{Fore.RED} ---[ Input tidak boleh kosong.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
                    else:
                        nomor_list = [n.strip() for n in input_ids.split(",") if n.strip().isdigit()]
                        for i, nomor in enumerate(nomor_list, 1):
                            urutan = int(nomor)
                            car_entry = next((item for item in nomercar if item["urutan"] == urutan), None)
                            if not car_entry:
                                print(f"{Fore.RED} ---[ Please enter the correct car number.")
                                continue
                            carid = str(car_entry["id"])
                            carname = car_entry.get("name", f"Car ID {carid}")
                            filepath = f"dataplayer/cars/{carid}"
                            if not os.path.isfile(filepath):
                                print(f"{Fore.RED} ---[ You don't have a car with CarID {carid}")
                                continue
                            with open(filepath, "r") as f:
                                data = json.load(f)
                            car_id = data["data"].get("CarID", "???")
                            print(f"{Fore.CYAN} ---[{Style.RESET_ALL} Injecting CarID: {car_id} ({i}/{len(nomor_list)})...", end=" ")
                            result = cpm.unlocked_police(data["data"])
                            if result:
                                print(f"{Fore.GREEN} Successfuly!")
                            else:
                                print(f"{Fore.RED} Failed.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)

            elif choice == "16":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 10000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 21 + "[ Unlock Bodykits ]" + "=" * 21))
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    sleep(2)
                else:
                    print("  Cars List:")
                    print(namacar)
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    input_ids = input(f"{Fore.CYAN} ---[{Style.RESET_ALL} Input number car: ").strip()
                    if not input_ids:
                        print(f"{Fore.RED} ---[ Input tidak boleh kosong.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
                    else:
                        nomor_list = [n.strip() for n in input_ids.split(",") if n.strip().isdigit()]
                        for i, nomor in enumerate(nomor_list, 1):
                            urutan = int(nomor)
                            car_entry = next((item for item in nomercar if item["urutan"] == urutan), None)
                            if not car_entry:
                                print(f"{Fore.RED} ---[ Please enter the correct car number.")
                                continue
                            carid = str(car_entry["id"])
                            carname = car_entry.get("name", f"Car ID {carid}")
                            filepath = f"dataplayer/cars/{carid}"
                            if not os.path.isfile(filepath):
                                print(f"{Fore.RED} ---[ You don't have a car with CarID {carid}")
                                continue
                            with open(filepath, "r") as f:
                                data = json.load(f)
                            car_id = data["data"].get("CarID", "???")
                            print(f"{Fore.CYAN} ---[{Style.RESET_ALL} Injecting CarID: {car_id} ({i}/{len(nomor_list)})...", end=" ")
                            result = cpm.unlocked_bodykits(data["data"])
                            if result:
                                print(f"{Fore.GREEN} Successfuly!")
                            else:
                                print(f"{Fore.RED} Failed.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)

            elif choice == "17":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 3000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 21 + "[ Unlock Cars ]" + "=" * 22))
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    sleep(2)
                else:
                    print("  Cars List:")
                    print(namacar)
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    input_ids = input(f"{Fore.CYAN} ---[{Style.RESET_ALL} Input number car: ").strip()
                    if not input_ids:
                        print(f"{Fore.RED} ---[ Input tidak boleh kosong.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
                    else:
                        nomor_list = [n.strip() for n in input_ids.split(",") if n.strip().isdigit()]
                        for i, nomor in enumerate(nomor_list, 1):
                            urutan = int(nomor)
                            car_entry = next((item for item in nomercar if item["urutan"] == urutan), None)
                            if not car_entry:
                                print(f"{Fore.RED} ---[ Please enter the correct car number.")
                                continue
                            carid = str(car_entry["id"])
                            carname = car_entry.get("name", f"Car ID {carid}")
                            filepath = f"datacars/cars/{carid}"
                            if not os.path.isfile(filepath):
                                print(f"{Fore.RED} ---[ You don't have a car with CarID {carid}")
                                continue
                            with open(filepath, "r") as f:
                                data = json.load(f)
                            car_id = data["data"].get("CarID", "???")
                            print(f"{Fore.CYAN} ---[{Style.RESET_ALL} Injecting CarID: {car_id} ({i}/{len(nomor_list)})...", end=" ")
                            result = cpm.save_player_car(data["data"])
                            if result:
                                print(f"{Fore.GREEN} Successfuly!")
                            else:
                                print(f"{Fore.RED} Failed.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
                    
            elif choice == "18":
                key_data = cpm.get_key_data()
                is_unlimited = key_data.get("is_unlimited", False)
                coins = key_data.get("coins", 0)
                required_coins = 10000
                print(Colorate.Horizontal(Colors.green_to_white, "=" * 18 + "[ Swap Gearbox To AWD ]" + "=" * 17))
                if not is_unlimited and coins < required_coins:
                    print(f"{Fore.RED}  ---[{Style.RESET_ALL} Balance tidak mencukupi. Diperlukan {required_coins} koin.")
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    sleep(2)
                else:
                    print("  Cars List:")
                    print(namacar)
                    print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                    input_ids = input(f"{Fore.CYAN} ---[{Style.RESET_ALL} Input number car: ").strip()
                    if not input_ids:
                        print(f"{Fore.RED} ---[ Input tidak boleh kosong.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
                    else:
                        nomor_list = [n.strip() for n in input_ids.split(",") if n.strip().isdigit()]
                        for i, nomor in enumerate(nomor_list, 1):
                            urutan = int(nomor)
                            car_entry = next((item for item in nomercar if item["urutan"] == urutan), None)
                            if not car_entry:
                                print(f"{Fore.RED} ---[ Please enter the correct car number.")
                                continue
                            carid = str(car_entry["id"])
                            carname = car_entry.get("name", f"Car ID {carid}")
                            filepath = f"dataplayer/cars/{carid}"
                            if not os.path.isfile(filepath):
                                print(f"{Fore.RED} ---[ You don't have a car with CarID {carid}")
                                continue
                            with open(filepath, "r") as f:
                                data = json.load(f)
                            car_id = data["data"].get("CarID", "???")
                            print(f"{Fore.CYAN} ---[{Style.RESET_ALL} Injecting CarID: {car_id} ({i}/{len(nomor_list)})...", end=" ")
                            result = cpm.swap_gearbox_awd(data["data"])
                            if result:
                                print(f"{Fore.GREEN} Successfuly!")
                            else:
                                print(f"{Fore.RED} Failed.")
                        print(Colorate.Horizontal(Colors.green_to_white, "=" * 58))
                        sleep(2)
