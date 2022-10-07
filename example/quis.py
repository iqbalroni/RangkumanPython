import random
import os
point = 0

def pembatas() : 
    print("=====================")

def minPoint() :
    global point
    point = point - 5

def addPoint() :
    global point
    point = point + 10

while True :
    os.system("cls")
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    pembatas()
    print("Point Kamu",point)
    pembatas()
    key = int(input("Hasil Dari "+str(a)+"+"+str(b)+"="))
    jawaban = a + b
    if(key == jawaban) :
        os.system("cls")
        pembatas()
        addPoint()
    else : 
        os.system("cls")
        minPoint()
        print("Jawaban Kamu Salah")
        if(point <= 0) : 
            os.system("cls")
            pembatas()
            print("GAMEOVER")
            pembatas()
            break