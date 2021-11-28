# MIT License
#
# Copyright (c) 2021 Pablo Henrique
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import colorama
import pyautogui
import time
import threading
import configparser
import random
from colorama import Fore, Back, Style
from datetime import datetime
import glob



pyautogui.FAILSAFE = False
now = datetime.now()
current_time = now.strftime("[%H:%M:%S]")


colorama.init()
config = configparser.ConfigParser()
config.read('settings.ini')


MapsCleared = 0
CiclesDone = 0
ErrorsFound = 0
UseMouse = True


BotaoWork = eval(config.get('settings', 'BotaoWork'), {}, {})
BotaoClose = eval(config.get('settings', 'BotaoClose'), {}, {})
BotaoMapa = eval(config.get('settings', 'BotaoMapa'), {}, {})
BotaoVoltar = eval(config.get('settings', 'BotaoVoltar'), {}, {})
BotaoHeroes = eval(config.get('settings', 'BotaoHeroes'), {}, {})
BotaoConnect = eval(config.get('settings', 'BotaoConnect'), {}, {})
BotaoMeta = eval(config.get('settings', 'BotaoMeta'), {}, {})
BotaoNewMap = eval(config.get('settings', 'BotaoNewMap'), {}, {})

TabsMeta = int(config['settings']['TabsMeta'])

PosicaoScroll = eval(config.get('settings', 'PosicaoScroll'), {}, {})
NumScroll = int(config['settings']['NumScroll'])
VelScroll = int(config['settings']['VelScroll'])

DelayFarm = int(config['settings']['DelayFarm'])
DelayStats = int(config['settings']['DelayStats'])
Heroes = int(config['settings']['Heroes'])


DelayToStart = int(config['settings']['DelayToStart'])
AntiDetection = bool(config.getboolean('settings', 'AntiDetection'))
AntiBot = int
MultiAccount = bool(config.getboolean('settings', 'MultiAccount'))
Accounts = int(config['settings']['Accounts'])


def pprint(text):
    print(datetime.now().strftime("[%H:%M:%S]") + str(text))


# Put the heroes to work function
def work():
    global CiclesDone
    print(datetime.now().strftime("[%H:%M:%S]") + 'Putting heroes to work...')
    time.sleep(3)
    pyautogui.moveTo(BotaoVoltar)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(BotaoHeroes)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(PosicaoScroll)
    time.sleep(0.5)
    pyautogui.click()

    for s in range(NumScroll):
        pyautogui.scroll(VelScroll)
        time.sleep(0.5)
    time.sleep(2)

    for _ in range(Heroes):
        pyautogui.moveTo(BotaoWork)
        pyautogui.click()
        time.sleep(2)

    time.sleep(1)
    pyautogui.moveTo(BotaoClose)
    pyautogui.click()
    CiclesDone = CiclesDone + 1


# Open map from initial page
def abrir_mapa():
    print(datetime.now().strftime("[%H:%M:%S]") + "Opening map...")
    time.sleep(3)
    pyautogui.moveTo(BotaoMapa)
    pyautogui.click()


# Open map multi acc
def abrir_mapa2():
    print(datetime.now().strftime("[%H:%M:%S]") + "Opening map...")
    time.sleep(3)
    for i in range(1, Accounts + 1):
        config = configparser.ConfigParser()
        aux = (f'multi{str(i)}.ini')
        config.read(aux)

        global BotaoMapa

        BotaoMapa = eval(config.get('settings', 'BotaoMapa'), {}, {})
        pyautogui.moveTo(BotaoMapa)
        pyautogui.click()


#Single Account farm
def bot():
    while True:
        abrir_mapa()
        work()
        abrir_mapa()
        tempo_farm()


# Multiacc loop farm
def multiacc():
    global Accounts
    global CurrentConfig
    while True:
        for i in range(1, Accounts + 1):
            config = configparser.ConfigParser()
            aux = (f'multi{str(i)}.ini')
            config.read(aux)

            global BotaoWork
            global BotaoClose
            global BotaoMapa
            global BotaoVoltar
            global BotaoHeroes
            global BotaoNewMap
            global PosicaoScroll
            global VelScroll
            global Heroes
            global NumScroll

            BotaoWork = eval(config.get('settings', 'BotaoWork'), {}, {})
            BotaoClose = eval(config.get('settings', 'BotaoClose'), {}, {})
            BotaoMapa = eval(config.get('settings', 'BotaoMapa'), {}, {})
            BotaoVoltar = eval(config.get('settings', 'BotaoVoltar'), {}, {})
            BotaoHeroes = eval(config.get('settings', 'BotaoHeroes'), {}, {})
            BotaoNewMap = eval(config.get('settings', 'BotaoNewMap'), {}, {})
            PosicaoScroll = eval(config.get('settings', 'PosicaoScroll'), {}, {})
            NumScroll = int(config['settings']['NumScroll'])
            VelScroll = int(config['settings']['VelScroll'])
            Heroes = int(config['settings']['Heroes'])

            abrir_mapa()
            work()
            abrir_mapa()

        tempo_farm()


# Time to delay the work function
def tempo_farm():
    global DelayFarm
    global AntiBot
    global AntiDetection
    if AntiDetection:
        AntiBot = random.randint(300, 1200)
    else:
        AntiBot = 0

    anti_bot = int(AntiBot)
    mins, secs = divmod(anti_bot, 60)
    formatTime = (f'{mins:02d}:{secs:02d}')
    print(datetime.now().strftime("[%H:%M:%S]") + f"Added: [{formatTime}] minutes for avoid pattern detection")
    countdown = DelayFarm + anti_bot

    while countdown:
        mins, secs = divmod(countdown, 60)
        hours, mins = divmod(mins, 60)
        timeformat = (f'{hours:d}:{mins:02d}:{secs:02d}')
        print(datetime.now().strftime("[%H:%M:%S]") + f"Heroes farming/resting. Waiting timer:\t[{timeformat}]\r",
              end="")
        time.sleep(1)
        countdown -= 1


# Check for errors
def check_errors():
    global ErrorsFound

    while True:
        errors = glob.glob("Errors/*.png")
        for erro in errors:
            erro = pyautogui.locateCenterOnScreen(erro)
            if erro:
                print("Error found")
                pyautogui.moveTo(erro)
                time.sleep(0.7)
                pyautogui.click(erro)
                pyautogui.hotkey('ctrl', 'f5')
                ErrorsFound = ErrorsFound + 1
                connect()
                time.sleep(60)




#Click next map
def check_map():
    global MapsCleared
    maps = glob.glob("NewMap/*.png")
    while True:
        for map in maps:
            map = pyautogui.locateCenterOnScreen(map)
            if map:
                pyautogui.moveTo(map)
                time.sleep(0.8)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                MapsCleared = MapsCleared + 1


# Use Mouse to login
def mouse_login():
    print("Using mouse to login")
    aux = None

    if MultiAccount:
        for i in range(1, Accounts):
            sign = pyautogui.locateCenterOnScreen(f"Imgs\\SIGN{i}.png")
            if sign:
                print("Sign found")
                aux = sign
    else:
        sign = pyautogui.locateCenterOnScreen(f"Imgs\\SIGN.png")
        if sign:
            print("Sign found")
            aux = sign


    if aux:
        pyautogui.moveTo(aux)
        time.sleep(3)
        pyautogui.click()
        print("Sign Clicked")
        time.sleep(15)
    else:
        print("Sign not Clicked")


# Connect from mainpage
def connect():
    global UseMouse

    retries = 0

    main = glob.glob(f"Imgs/MAIN*.png")

    time.sleep(5)


    while True:
        aux = None
        auxAba = None

        for img in main:
            img = pyautogui.locateCenterOnScreen(img)
            aux = img

        if aux:
            print("\n")
            pprint(Fore.RED + "Error found or game was stuck. Reconnecting.")
            print(Fore.MAGENTA)
            print("\n")
            aux2 = aux
            pyautogui.moveTo(aux2)
            pyautogui.click()
            time.sleep(3)
            retries = retries + 1
            print(f"\nretries:{retries}\n")

            if retries >= 3:
                pyautogui.press('f5')
                retries = 0
            else:
                pass

            if UseMouse:
                mouse_login()
            else:
                pass


            for _ in range(15):
                Aba = pyautogui.locateCenterOnScreen("Imgs\\ABAMETA.png")
                if Aba:
                    auxAba = Aba
                else:
                    pass


            if auxAba:
                pyautogui.moveTo(auxAba)
                time.sleep(0.3)
                pyautogui.click()
                mouse_login()
            else:
                pass

            time.sleep(20)

            if MultiAccount:
                abrir_mapa2()
            else:
                abrir_mapa2()


# Show farm stats
def show_stats():
    while True:
        time.sleep(600)
        print("\n")
        print(Fore.BLUE + "-" * 80)
        print(Fore.BLUE + datetime.now().strftime("[%H:%M:%S]") + "Cicles  of farming done: " + str(CiclesDone))
        print(Fore.BLUE + datetime.now().strftime("[%H:%M:%S]") + "Maps Cleared: " + str(MapsCleared))
        print(Fore.BLUE + datetime.now().strftime("[%H:%M:%S]") + "Errors found: " + str(ErrorsFound))
        print(Fore.BLUE + "-" * 80)
        print("\n")
        print(Fore.MAGENTA)
        time.sleep(DelayStats)


# Start threading
def threads():
    threadss = []
    t1 = threading.Thread(target=check_errors)
    t2 = threading.Thread(target=check_map)

    if MultiAccount:
        t3 = threading.Thread(target=multiacc)
    else:
        t3 = threading.Thread(target=bot)

    t4 = threading.Thread(target=show_stats)
    #t5 = threading.Thread(target=connect)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    #t5.start()
    threadss.append(t1)
    threadss.append(t2)
    threadss.append(t3)
    threadss.append(t4)
    #threadss.append(t5)

    for thread in threadss:
        thread.join()


string1 = "BomberBot V1.03"
string2 = "Telegram:t.me/BomberBotBB"
string3 = "Github:github.com/henr1q/BomberBot"
string4 = "This bot is FREE."
print(Fore.GREEN + "=" * 40)
print(Fore.BLUE + string1.center(40, " "))
print(Fore.BLUE + string2.center(40, " "))
print(Fore.BLUE + string3.center(40, " "))
print(Fore.BLUE + Fore.RED + string4.center(40, " "))
print(Fore.GREEN + "=" * 40)
print(Fore.GREEN)


def botmenu():
    menu = int(input(
        "Choose a option:\n1)Run the bot\n2)Test/Debug a single function(Use this if you having problems with mapping) WORKING ON SINGLE ACCOUNT ONLY\n3)Exit\n\n"))
    print(Fore.MAGENTA)
    if menu == 1:
        defaultdelay = 10
        print(datetime.now().strftime(
            "[%H:%M:%S]") + f"Bot will start in {defaultdelay + DelayToStart} seconds. Make sure to go to the main page.")
        time.sleep(10 + DelayToStart)
        threads()
    elif menu == 2:
        menu2 = int(input(datetime.now().strftime(
            "\n[%H:%M:%S]") + "Choose a function to test it:\n1)Open Map\n2)Put heroes to work\n3)Connect from login page\n4)Find and click next map\n5)Check for error and try reconnect\n6)Relog from main page stuck\n7)Exit\n\n"))
        if menu2 == 1:
            print(Fore.CYAN + datetime.now().strftime(
                "[%H:%M:%S]") + "Delaying 5 seconds and starting the function. Make sure to go to the page where function should work.")
            time.sleep(5)
            abrir_mapa()
            botmenu()
        if menu2 == 2:
            print(Fore.CYAN + datetime.now().strftime(
                "[%H:%M:%S]") + "Delaying 5 seconds and starting the function. Make sure to go to the page where function should work.")
            time.sleep(5)
            work()
            botmenu()
        if menu2 == 3:
            print(Fore.CYAN + datetime.now().strftime(
                "[%H:%M:%S]") + "Delaying 5 seconds and starting the function. Make sure to go to the page where function should worke.")
            time.sleep(5)
            connect()
            botmenu()
        if menu2 == 4:
            print(Fore.CYAN + datetime.now().strftime(
                "[%H:%M:%S]") + "Delaying 5 seconds and starting the function. Make sure to go to the page where function should work.")
            time.sleep(5)
            check_map()
            botmenu()
        if menu2 == 5:
            print(Fore.CYAN + datetime.now().strftime(
                "[%H:%M:%S]") + "Delaying 5 seconds and starting the function. Make sure to go to the page where function should work.")
            time.sleep(5)
            check_errors()
            botmenu()
        if menu2 == 6:
            print(Fore.CYAN + datetime.now().strftime(
                "[%H:%M:%S]") + "Delaying 5 seconds and starting the function. Make sure to go to the page where function should work.")
            print("This function takes 3 minutes on main page")
            time.sleep(5)
            botmenu()
        if menu2 == 7:
            print(Fore.GREEN)
            botmenu()
        else:
            print(Fore.RED + datetime.now().strftime("[%H:%M:%S]") + "Choose a valid option")
    elif menu == 3:
        print("Error")
        #sys.exit()
    else:
        print(Fore.RED + datetime.now().strftime("[%H:%M:%S]") + "Choose a valid option")


botmenu()
