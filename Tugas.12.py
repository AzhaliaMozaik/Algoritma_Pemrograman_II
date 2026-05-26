print("\n===============================================PERTEMUAN 12===============================================")
print("----------------------------------------------AZHALIA MOZAIK---------------------------------------------")

#===============================================Soal No.1================================================
print("\n===============================================Soal No.1================================================")
def penjumlahan(x):
    bilangan = 15 
    return x + 15

print(penjumlahan(44))
# print(bilangan) #HAPUS # DI print(bilangan) AKAN ERROR KARENA MENCOBA MEMANGGIL VARIABEL BILANGAN DARI LUAR FUNGSI

#===============================================Soal No.2================================================
print("\n===============================================Soal No.2================================================")
angka_awal = 5   
 
def tambah_lima(x):  
    return x + angka_awal  

print(tambah_lima(10))
print(angka_awal)    

#===============================================Soal No.3================================================
print("\n===============================================Soal No.3================================================")
def tambah_sepuluh(x):  
    angka = 10          
    return x + angka    

print(tambah_sepuluh(15))   

#===============================================Soal No.4================================================
print("\n===============================================Soal No.4================================================")
bilangan = 5
print(bilangan)

def return_bilangan():
    global bilangan
    bilangan = 2 
    return bilangan 
    
print(return_bilangan())
print(bilangan)

#===============================================Soal No.5================================================
print("\n===============================================Soal No.5================================================")
def hitung_imt(berat, tinggi):
    imt = berat / (tinggi * tinggi)
    return imt

# input dari user
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (meter): "))

# hitung IMT
index_massa_tubuh = hitung_imt(berat, tinggi)

# kategori
kategori = ["Normal", "Gemuk", "Obesitas"]

# penentuan kategori
if 18.5 <= index_massa_tubuh <= 25.0:
    print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori", kategori[0])
elif 25.0 < index_massa_tubuh <= 27.0:
    print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori", kategori[1])
else:
    print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori", kategori[2], "- Anda harus diet!")

#===============================================Soal No.6================================================
print("\n===============================================Soal No.6================================================")
def cek_segitiga(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Sisi tidak valid"
    
    return "Segitiga valid" if (a + b > c and b + c > a and c + a > b) else "Bukan segitiga"

print(cek_segitiga(1, 1, 1))
print(cek_segitiga(1, 1, 3))

# Selesai diperbaiki: Membuat sampel list Nomor_1 agar tidak memicu NameError saat dislice
Nomor_1 = [10, 20, 30, 40, 50]
New_Nomor = Nomor_1[1:4]
print(New_Nomor)

#===============================================Soal No.7================================================
print("\n===============================================Soal No.7================================================")
def segitiga2(n):
    for i in range(n, 0, -1):
        print("*" * i)

segitiga2(5) # Selesai diperbaiki: Nama fungsi disamakan menjadi segitiga2

#===============================================Soal No.8================================================
print("\n===============================================Soal No.8================================================")
def segitiga3(n):
    for i in range(1, n + 1): 
        print(" " * (n - i) + "*" * i)

segitiga3(5)

#===============================================Soal No.9================================================
print("\n===============================================Soal No.9================================================")
def faktorial(n):
    hasil = 1 
    for i in range(1, n + 1):
        hasil *= i 
    return hasil 
angka = 5
print(f"Faktorial dari {angka} adalah {faktorial(angka)}")

#===============================================Soal No.10===============================================
print("\n===============================================Soal No.10===============================================")
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    elem_1 = elem_2 = 1
    hasil_jumlah = 0

    for i in range(3, n + 1): 
        hasil_jumlah = elem_1 + elem_2
        elem_1 = elem_2
        elem_2 = hasil_jumlah

    return elem_2 

for i in range(1, 10):
    print(i, "->", fibonacci(i))

#===============================================Soal No.11===============================================
print("\n===============================================Soal No.11===============================================")
def factorial(n):
    if n < 0:
        return None      
    if n == 0 or n == 1:
        return 1             
    return n * factorial(n - 1)

for i in range(6):
    print(i, "->", factorial(i))

#===============================================Soal No.12===============================================
print("\n===============================================Soal No.12===============================================")
def fibonacci_rekursif(n):
    if n < 1:
        return None      
    if n < 3:
        return 1             
    return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)

for i in range(1, 10):
    print(i, "->", fibonacci_rekursif(i))

print("\n===============================================TERIMAKASIH===============================================")
print("---------------------------------------------------------------------------------------------------------\n")