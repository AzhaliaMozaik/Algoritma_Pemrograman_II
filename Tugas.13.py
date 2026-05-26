print("\n===============================================PERTEMUAN 13===============================================")
print("----------------------------------------------AZHALIA MOZAIK---------------------------------------------")

#===============================================Soal No.1================================================
print("\n===============================================Soal No.1================================================")
kucing = ("Caca", "Cici", "Mici")
kucingku = "Joy", "Cemong"
kucing_kosong = ()

print(kucing)
print(kucingku)
print(kucing_kosong)

#===============================================Soal No.2================================================
print("\n===============================================Soal No.2================================================")
kucing = ("Caca", "Cici", "Mici", "Cemong", "Joy")
print(kucing[0])  
print(kucing[-1]) 
print(kucing[:1]) 
print(kucing[:2])  

for element in kucing:  
    print(element)

#===============================================Soal No.3================================================
print("\n===============================================Soal No.3================================================")
kucing = ("Caca", "Cici", "Mici", "Cemong", "Joy")
print("Tuple awal:", kucing)     

print("\n--- Catatan Soal No.3: Operasi di bawah ini ilegal pada Tuple (Sengaja di-comment agar tidak error) ---")
# kucing.append("Lala")          # ERROR: Tuple tidak punya fungsi append
# del kucing                     # Menghapus variabel kucing dari memori, maka fungsi jadi tidak memiliki nilai
# print(kucing)                  # ERROR: Variabel sudah dihapus
# kucing ["Caca"] = ["chiko"]    # ERROR: Tuple tidak bisa diubah isinya

#===============================================Soal No.4================================================
print("\n===============================================Soal No.4================================================")
nomor = (25, 30, 80, 10, 59)

n1 = nomor + (15, 7)
n2 = nomor * 2

print(len(n2))
print(n1)
print(n2)
print(7 in nomor)
print(-7 not in nomor)

#===============================================Soal No.5================================================
print("\n===============================================Soal No.5================================================")
data = ("Rozaan", 19, "Mahasiswa")

nama, umur, status = data

print(nama)
print(umur)
print(status)

#===============================================Soal No.6================================================
print("\n===============================================Soal No.6================================================")
mahasiswa = {
    "nama": "Mas Ojan",
    "nomor hp": "2530801080"
}

print(mahasiswa)

#===============================================Soal No.7================================================
print("\n===============================================Soal No.7================================================")
buku = {
    "judul": "Python Dasar",
    "harga": 75000
}

print(buku["judul"])

#===============================================Soal No.8================================================
print("\n===============================================Soal No.8================================================")
mobil = {
    "merk": "Toyota",
    "tahun": 2022
}

print(mobil.keys())

#===============================================Soal No.9================================================
print("\n===============================================Soal No.9================================================")
# Selesai diperbaiki: Menambahkan tanda kutip pembuka pada "umur" dan menambahkan operator "="
data_siswa = {"nama": "raffi", "umur": 19, "sekolah": "MAHASISWA 2"}

nilai_saja = data_siswa.values()

print(nilai_saja)

#===============================================Soal No.10===============================================
print("\n===============================================Soal No.10===============================================")
# Selesai diperbaiki: Menambahkan operator "=" pada pembuatan dictionary dan pemanggilan variabel
mobil = {"merk": "Toyota", "warna": "Hitam"}

pasangan = mobil.items()
print(pasangan)

#===============================================Soal No.11===============================================
print("\n===============================================Soal No.11===============================================")
stok = {"apel": 10, "jeruk": 5}

stok_baru = {"jeruk": 12, "mangga": 8}

stok.update(stok_baru)
print(stok)

#===============================================Soal No.12===============================================
print("\n===============================================Soal No.12===============================================")
# Selesai diperbaiki: Menambahkan operator "=" yang sempat tertinggal
laptop = {"brand": "Asus", "ram": "16GB", "ssd": "512GB"}

item_terakhir = laptop.popitem()

print("Item yang dihapus:", item_terakhir)
print("Sisa dictionary:", laptop)

#===============================================Soal No.13===============================================
print("\n===============================================Soal No.13===============================================")
dictionary = {
    "rozaan" : 97,
    "dava" : 85,
    "rapi" : 83,
    "azha" : 99
}

for nama in dictionary.keys():
    print("nilai", nama, "->", dictionary[nama])

dictionary["azha"] = 90
del dictionary["rapi"]

print("\nversi modifikasi")
for nama in dictionary.keys():
    print("nilai", nama, "->", dictionary[nama])

#===============================================Soal No.14===============================================
print("\n===============================================Soal No.14===============================================")
try:
    angka = int(input("masukan angka: "))
    hasil = angka * 2 + 15
    print(hasil)
except ValueError:
    print("input harus angka")

#===============================================Soal No.15===============================================
print("\n===============================================Soal No.15===============================================")
try:
    angka = int(input("Masukan angka: "))
    hasil = 100 / angka + 15   
    print("Hasil:", hasil)
except (ValueError, ZeroDivisionError):
    print("Terjadi error: input harus angka atau tidak boleh nol")

print("\n===============================================TERIMAKASIH===============================================")
print("---------------------------------------------------------------------------------------------------------\n")