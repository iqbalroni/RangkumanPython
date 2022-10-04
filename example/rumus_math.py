import os

def clean() :
    os.system("cls")

def batas() :
    print("========================")

def judul(text) :
    batas()
    print(text)
    batas()

batas()
print("[1].Menghitung Kecepatan")
print("[2].Menghitung Jarak")
print("[3].Menghitung Waktu")
print("[4].Perkalian")
print("[5].Mencari Volume Kubus")
batas()
pilih = int(input("Masukan Pilihan Di Atas : "))
clean()
if(pilih == 1) :
    judul("MENGHITUNG KECEPATAN")
    jarak = int(input("Masukan Jarak : "))
    waktu = int(input("Masukan Waktu : "))
    batas()
    print("HASIL DARI KECEPATANNYA ADALAH",jarak/waktu)
    batas()
elif(pilih == 2) : 
    judul("MENGHITUNG JARAK")
    kecepatan = int(input("Masukan Kecepatan : "))
    waktu = int(input("Masukan Waktu : "))
    batas()
    print("HASIL DARI JARAKNYA ADALAH",kecepatan*waktu)
    batas()
elif(pilih == 3) : 
    judul("MENGHITUNG WAKTU")
    kecepatan = int(input("Masukan Kecepatan : "))
    jarak = int(input("Masukan Jarak : "))
    batas()
    print("HASIL DARI WAKTUNYA ADALAH",jarak/kecepatan)
    batas()
elif(pilih == 4):
    judul("PERKALIAN")
    angka = int(input("Masukan Angka : "))
    batas()
    for x in range(10) : 
        print(x+1,"x",angka,"=",(x+1)*angka)
    batas()
elif(pilih == 5) :
    judul("MENCARI VOLUME KUBUS")
    sisi = int(input("Masukan Panjang Sisi : "))
    print("Diketahui s =",sisi,"Cm")
    print("Ditanyakan V = ?")
    print("Penyelesaian")
    print("V =",sisi,"^3")
    print("V =",sisi*sisi*sisi,"cm ^3")
    batas()
else :
    print("INPUTAN ANDA SALAH")
    batas()