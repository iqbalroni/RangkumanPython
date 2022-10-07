from re import T
import os


dataBuah = []

while True :
    os.system("clear")
    print("Total Buah Ada ",str(len(dataBuah))," Buah")
    print("==="*10)

    buah = input("Masukan Nama Buah : ")
    rasa = input("Masukan Rasa Buah : ")

    buahBaru = [buah,rasa]
    dataBuah.append(buahBaru)

    os.system("clear")
    print("Daftar Buah : ")
    for x in range(len(dataBuah)) : 
        print(str(x+1),".Buah",dataBuah[x][0],"rasanya",dataBuah[x][1])
    
    print("==="*10)
    YnO = input("Apakah Kamu Ingin Menambah Data Lagi(Y/N) :")

    if(YnO == 'n' or YnO == 'N') :
        break

