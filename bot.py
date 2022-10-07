import time,os
from termcolor import colored
import webbrowser
import pyautogui as bot

ulang = "y"

def textGreen(text) :
    print(colored(text,color="green"))

def Loading() :
    textGreen("================")
    textGreen("Loading..")
    textGreen("================")

while ulang == "y" :
    os.system("cls")
    textGreen("|============================|")
    textGreen("| 1. Open Visual Studio Code |")
    textGreen("| 2. Open Browser            |")
    textGreen("| 3. Github                  |")
    textGreen("| 4. Youtube                 |")
    textGreen("| 5. Laragon                 |")
    textGreen("|                            |")
    textGreen("| 0. Exit                    |")
    textGreen("|============================|")

    pilih = int(input("Pilih Menu Di Atas : "))
    os.system("cls")

    if(pilih == 1) :
        Loading()
        os.system("code")
    elif(pilih == 2) :
        Loading()
        webbrowser.open("https://www.google.com/")
    elif(pilih == 3) :
        Loading()
        webbrowser.open("http://github.com/iqbalroni")
    elif(pilih == 4) : 
        Loading()
        webbrowser.open("https://www.youtube.com/")
    elif(pilih == 5) :
        Loading()
        os.system("start C:\laragon\laragon.exe")
        time.sleep(1)
        bot.press("Enter")

    elif(pilih == 0) :
        break
    else : 
        textGreen("================")
        textGreen("Inputan Menu Salah")
        textGreen("================")

    time.sleep(0.5)
    os.system("cls")
    ulang = input("Ingin Mengulangi Program Lagi (y/t)? :")