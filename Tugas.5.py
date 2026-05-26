print("\n=================================PERTEMUAN 5=================================")
print("--------------------------------AZHALIA MOZAIK-------------------------------")

#=================================Soal No.1==================================
print("\n=================================Soal No.1==================================")
x = 0
y = 1
z = 0
print(x==y)
print(x==z)
print(x!=y)
print(x!=z)
print(x<y)
print(y<z)
print(x>y)
print(y>z)
print(x<=y)
print(x<=z)
print(y<=z)
print(x>=y)
print(x>=z)
print(y>=z)

#=================================Soal No.2==================================
print("\n=================================Soal No.2==================================")
input_n = int(input("Masukkan Nilai: "))
print(input_n > 100)

#=================================Soal No.3==================================
print("\n=================================Soal No.3==================================")
Stok_Makan_Kucing = 3
if Stok_Makan_Kucing < 5:
    print("Jatah makan kucing hampir habis")

#=================================Soal No.4==================================
print("\n=================================Soal No.4==================================")
Stok_Makan_Kucing = 10
if Stok_Makan_Kucing <= 5:
    print("Jatah makan kucing hampir habis")
if Stok_Makan_Kucing > 8:
    print("Sudah terkecukupi")
if Stok_Makan_Kucing >= 10:
    print("Terlalu banyak Stok makan kucing")

#=================================Soal No.5==================================
print("\n=================================Soal No.5==================================")
x = 15
if x > 15: 
    print("x lebih besar dari pada 15")
else:
    print("x lebih kecil atau sama dengan 15")

#=================================Soal No.6==================================
print("\n=================================Soal No.6==================================")
Ukuran_Baju = 59

if Ukuran_Baju >= 70: 
    print("Ukuran Baju XL")
elif Ukuran_Baju >= 60: 
    print("Ukuran Baju L")
elif Ukuran_Baju >= 50: 
    print("Ukuran Baju M")
else:
    print("Ukuran Baju S") 

#=================================Soal No.7==================================
print("\n=================================Soal No.7==================================")
Angka1 = int(input("Masukkan angka pertama: "))
Angka2 = int(input("Masukkan angka kedua: "))
if Angka1 > Angka2: Angka_besar = Angka1
else: Angka_besar = Angka2
print("Angka yang besar adalah ", Angka_besar)

#=================================Soal No.8==================================
print("\n=================================Soal No.8==================================")
Angka1 = int(input("Masukkan angka pertama: "))
Angka2 = int(input("Masukkan angka kedua: "))
Angka3 = int(input("Masukkan angka ketiga: "))
Angka_besar = Angka1
if Angka2 > Angka_besar:
    Angka_besar = Angka2
if Angka3 > Angka_besar:
    Angka_besar = Angka3
print("Angka yang besar adalah", Angka_besar)

#=================================Soal No.9==================================
print("\n=================================Soal No.9==================================")
Angka1 = int(input("Masukkan angka pertama: "))
Angka2 = int(input("Masukkan angka kedua: "))
Angka3 = int(input("Masukkan angka ketiga: "))
Angka_besar = max(Angka1, Angka2, Angka3)
print("Angka yang besar adalah", Angka_besar)

#=================================Soal No.10=================================
print("\n=================================Soal No.10=================================")
Pendapatan = float(input("Masukkan perdapatan bulanan Anda: "))
Pajak = 0
Pendapatan_Tahunan = Pendapatan * 12
if Pendapatan_Tahunan <= 60000000:
    Pajak = Pendapatan_Tahunan * 0.05
elif Pendapatan_Tahunan <= 250000000:
    Pajak = Pendapatan_Tahunan * 0.15
elif Pendapatan_Tahunan <= 500000000:
    Pajak = Pendapatan_Tahunan * 0.25
else:
    Pajak = Pendapatan_Tahunan * 0.30
print("Pajak peghasilan yang harus dibayar adalah sebesar", Pajak, "Rupiah")

print("\n=================================TERIMAKASIH=================================")
print("-----------------------------------------------------------------------------\n")