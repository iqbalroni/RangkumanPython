import pyfiglet
from termcolor import colored

print(colored(pyfiglet.figlet_format("HACKNAME"),"red"))
nama = input("Masukan Nama :")
loop = int(input("masukan Perulangan :"))

for x in range(loop) :
    print(colored(pyfiglet.figlet_format(nama,font = "banner3-D"),"green"))