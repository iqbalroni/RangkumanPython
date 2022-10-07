import pyfiglet,time
import pyautogui as bot
import os
from termcolor import colored
import webbrowser

ulangi = "y"

while ulangi == "y" :
    os.system("cls")
    print(colored("=============================",color="green"))
    print(colored("|       SPAM WHATSAPP       |",color="green"))
    print(colored("=============================",color="green"))
    loop = int(input("Loop Message : "))
    message = input("Your Message : ")

    os.system("cls")
    print(colored("=============================",color="green"))
    print(colored("Progress...",color="green"))
    print(colored("=============================",color="green"))
    time.sleep(2)

    for x in range(loop) :
        time.sleep(0.5)
        bot.write(message)
        bot.press("Enter")

    os.system("cls")
    print(colored("=============================",color="green"))
    print(colored("BERHASIL...",color="green"))
    print(colored("=============================",color="green"))
    ulangi = input("Ingin Mengulang Programnya (y/t)?")
