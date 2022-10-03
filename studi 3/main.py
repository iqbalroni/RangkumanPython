# INPUT PYTHON
# cara membuat inputan di python biasanya menggunakan input({textnya})

# example : 
nama = input("masukan Nama : ")
print("Nama mu adalah",nama,"yang bertipe data",type(nama))

# di atas berlaku hanya untuk tipedata string
# dan jika int di sebelum input harus memasukan tipe datanya dulu
# contoh "int(input(.....))"

kelas = int(input("Masukan Kelas : "))
print("Kelas mu di",kelas,"yang bertipe data",type(kelas))

# dan untuk boolean jika kalau di input pasti memberikan nilai TRUE
# dengan cara mudahnya input di jadikan ke int dan akan di eksekusi bool
# jika nilai 0 akan bernilai false dan nilai 1 akan bernilai True
absen = bool(int(input("Apakah Kamu Masuk?")))
print("Hasilnya adalah ",absen," tipe data ",type(absen))