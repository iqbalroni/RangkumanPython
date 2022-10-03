# TIPEDATA PYTHON
# type(angka) berfungsi untuk mencari tau suatu variabel bertipe data apa?

# 1.Tipe data satuan / (integer)
from operator import truediv


angka_int = 2
print("Angka yang muncul ",angka_int," bertipe data ",type(angka_int))

# 2.Tipe data angka dengan koma / (float)
angka_float = 1.5
print("Angka yang muncul ",angka_float," Bertipe data ",type(angka_float))

# 3.Tipe data kumpulan karakter2 / (String)
nama = "Bismillah"
print("Di atas munculnya ",nama," bertipe data ",type(nama))

# 4.Tipe data true atau false / (boolean)
cek = True
print("Tipe diatas menampilkan ", cek ," Bertipe data ",type(cek))

# Bilangan Kompleks
data = complex(5,1)
print(data)

# jika data yang tidak ada di python bisa menggunakan dari bahasa
# pemograman C , dengan mengimport kan "from ctypes import {nama_tipe_data}"
# example : 

from ctypes import c_double
# penggunaan tipedata di variabel
why = c_double(10.5)
print("muncul program di atas ",why," bertipe data",type(why))

# data boolean // jika nilai 0 menjadi False dan selain 0 akan bernilai True