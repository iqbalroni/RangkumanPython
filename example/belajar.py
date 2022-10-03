from cgi import print_environ
import os

def myInput() :
    global nilA,nilB
    print("====================================")
    nilA = int(input("Masukan Nilai A : "))
    nilB = int(input("Masukan Nilai B : "))
    print("====================================")

print("*_______________________*")
print("|PILIHAN MENU ALGORITMA |")
print("|=======================|")
print("|1.Pertambahan          |")
print("|2.Pengurangan          |")
print("|3.Pembagian            |")
print("*_______________________*")
pilih = int(input("Masukan Pilihan Anda :"))
os.system('cls')
print("====================================")
if pilih == 1 :
    print("PERTAMBAHAN")
    myInput()
    hasil = nilA + nilB
    print("Hasilnya adalah "+str(hasil))
elif pilih == 2 : 
    print("PENGURANGAN")
    myInput()
    hasil = nilA - nilB
    print("Hasilnya adalah "+str(hasil))
elif pilih == 3 : 
    print("PEMBAGIAN")
    myInput()
    hasil = nilA / nilB
    print("Hasilnya adalah "+str(hasil))
else : 
    print("YANG ANDA MASUKAN SALAH")

print("====================================")