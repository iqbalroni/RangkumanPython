import pyfiglet,time
import pyautogui as bot
import os
from termcolor import colored

ulangi = "y"

dataNilai = [
    [
        "ACHMAD ABDILLAH",
        "Hadir",
        79,
        85,
        78
    ],
    [
        "AKSIN LABIBUS SAID",
        "Hadir",
        81,
        80,
        77
    ],
    [
        "ANANTA WIDAYANI",
        "Hadir",
        83,
        80,
        76
    ],
    [
        "ARIF HIDAYATULLAH",
        "Hadir",
        88,
        87,
        78
    ],
    [
        "BIMA SATRIA PERMANA",
        "Hadir",
        0,
        0,
        0
    ],
    [
        "DAFANSYAH GILANG RAMADHAN",
        "Hadir",
        83,
        81,
        78
    ],
    [
        "DIMAS NURYADI SAPUTRA",
        "Hadir",
        78,
        80,
        77
    ],
    [
        "GALANG SAMUDRA EFENDI",
        "Hadir",
        79,
        80,
        77
    ],
    [
        "IMAM MUSTAQIM",
        "Hadir",
        84,
        81,
        78
    ],
    [
        "LUQMANUL HAKIM",
        "Hadir",
        83,
        87,
        85
    ],
    [
        "MOHAMMAD RADIT FIRMANZAH",
        "Hadir",
        78,
        76,
        78
    ],
    [
        "MUHAMMAD BAGAS RANDIYANTO",
        "Hadir",
        76,
        81,
        78
    ],
    [
        "MUHAMMAD IBNU AQIL",
        "Hadir",
        81,
        80,
        78
    ],
    [
        "MUHAMMAD ILMI RIZAL WARDANA SAFARI",
        "Hadir",
        81,
        81,
        80
    ],
    [
        "MUHAMMAD KABID GHITHRAF",
        "Hadir",
        80,
        79,
        83
    ],
    [
        "MUHAMMAD ZIDANE PUTRA DESWANTO",
        "Hadir",
        81,
        81,
        80
    ],
    [
        "RADHIT AUNULLAH ASSAJID",
        "Hadir",
        85,
        88,
        87
    ],
    [
        "RAFI AGUS LAKSONO",
        "Hadir",
        81,
        78,
        76
    ],
    [
        "RAIHAN ZAKI RAMADHANI",
        "Keluar",
        0,
        0,
        0
    ],
    [
        "RENO MUJIO RAHMAN",
        "Hadir",
        81,
        80,
        78
    ],
    [
        "RIVANDO PUTRA PRATAMA",
        "Hadir",
        0,
        0,
        0
    ],
    [
        "SITI RAUDATUL JANNAH",
        "Hadir",
        83,
        83,
        80
    ],
    [
        "SULTAN FACHRI AZIZ",
        "Hadir",
        80,
        83,
        83
    ],
    [
        "WILDAN AL AZIZ",
        "Hadir",
        78,
        80,
        77
    ],
    [
        "YOANRE LOUIS ALPHANABIUS HAZIRAN PERMADI",
        "Hadir",
        81,
        82,
        78
    ],
    [
        "ZASKIA AFRINA KHALIQ",
        "Hadir",
        78,
        79,
        78
    ]
]

while ulangi == "y" or ulangi == 'Y' :
    os.system("cls")
    print(colored("="*50,color="green"))
    print(colored(pyfiglet.figlet_format("BOT EX CEL"),color="green"))
    print(colored("="*50,color="green"))

    YoN = input(colored("Apakah Kamu Ingin Melakukan BOT EXCEL(Y/T) : ",color="yellow"))

    if(YoN == 'y' or YoN == 'Y') :
        os.system("cls")
        print(colored("=============================",color="green"))
        print(colored("Progress...",color="green"))
        print(colored("=============================",color="green"))
        time.sleep(2)

        for x in range(len(dataNilai)) :
            time.sleep(0.3)
            bot.write(str(x+1))
            bot.press("Tab")
            bot.write(dataNilai[x][0])
            bot.press("Tab")
            bot.write(dataNilai[x][1])
            bot.press("Tab")
            bot.write(str(dataNilai[x][2]))
            bot.press("Tab")
            bot.write(str(dataNilai[x][3]))
            bot.press("Tab")
            bot.write(str(dataNilai[x][4]))
            bot.press("Enter")

    os.system("cls")
    bot.alert(text="HIYAAA HIYAAA GA CAPEK KAN", title="BOT.Id")

    ulangi = input(colored("Ingin Mengulang Programnya (y/t) : ",color="yellow"))
