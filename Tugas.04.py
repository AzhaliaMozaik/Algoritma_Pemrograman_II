print("\n===============================================PERTEMUAN 4===============================================")
print("----------------------------------------------AZHALIA MOZAIK---------------------------------------------")

#===============================================Soal No.1================================================
print("\n===============================================Soal No.1================================================")
print("Kucing itu, namanya siapa?")
anything = input()
print(anything, "Kucing yang lucu sekali")

#===============================================Soal No.2================================================
print("\n===============================================Soal No.2================================================")
Makanan = input("Makanan apa yang kamu pesan : ")
print("Pesanan Anda Yaitu ", Makanan, "Sedang kami buat. Harap menunggu, Terimakasih!!")

#===============================================Soal No.3================================================
print("\n===============================================Soal No.3================================================")
HargaBarang = float(input("Masukkan harga barang : "))
Pajak = HargaBarang + 20
print(HargaBarang, "Total Pembelian", Pajak)

#===============================================Soal No.4================================================
print("\n===============================================Soal No.4================================================")
HargaBarang = float(input("Masukkan harga barang : "))
Total = HargaBarang + 20       
print("Harga Barang", HargaBarang, "Total Pembelian", Total)

#===============================================Soal No.5================================================
print("\n===============================================Soal No.5================================================")
leg_A = float(input("Input first leg length A: "))
leg_B = float(input("Input second leg length B: "))
hypo = (leg_A**2 + leg_B**2)** 0.5       
print("Hypotenuse length is", hypo)

#===============================================Soal No.6================================================
print("\n===============================================Soal No.6================================================")
leg_A = float(input("Input first leg length A: "))
leg_B = float(input("Input second leg length B: "))
print("Hypotenuse length is", (leg_A**2 + leg_B**2)** 0.5)

#===============================================Soal No.7================================================
print("\n===============================================Soal No.7================================================")
Buku = input("Buku apa yang ingin anda pinjam: ")
Tenggat = input("Berapa lama bukunya akan dipinjam: ")
print("Thank You")
print("\nBuku " + Buku + " Batas waktu peminjaman " + Tenggat)

#===============================================Soal No.8================================================
print("\n===============================================Soal No.8================================================")
print("+" + 10 * "#" + "+")
print(("|" + " " * 10 + "|\n") * 5, end = "")
print("+" + 10 * "#" + "+")

#===============================================Soal No.9================================================
print("\n===============================================Soal No.9================================================")
leg_A = float(input("Input first leg length: "))
leg_B = float(input("Input seconde leg length: "))
print("hypotenuse lenght is " + str((leg_A**2 + leg_B**2)** 0.5))

#===============================================Soal No.10===============================================
print("\n===============================================Soal No.10===============================================")
x = input("Enter a number: ")
print(type(x))

#===============================================Soal No.11===============================================
print("\n===============================================Soal No.11===============================================")
A = float(input("Nilai A: "))
B = float(input("Nilai B: "))
Penjumlahan = A + B
Pengurangan = A - B
Pembagian = A / B
Perkalian = A * B
print("A + B = ", Penjumlahan)
print("A - B = ", Pengurangan)
print("A / B = ", Pembagian)
print("A * B = ", Perkalian)
print("\n SELAMAT KAMU SUDAH PINTAR MATEMATIKA")

#===============================================Soal No.12===============================================
print("\n===============================================Soal No.12===============================================")
x = float(input("x = "))
y = 1.0 / (x + 1.0 / (x + 1.0 / (x + 1.0 / x))) # Sedikit diperbaiki rumusnya agar polanya sesuai pecahan berlanjut
print("Nilai y adalah", y)

#===============================================Soal No.13===============================================
print("\n===============================================Soal No.13===============================================")
Jam = int(input("Waktu mulai (Jam): "))
Menit = int(input("Waktu mulia (Menit): "))
Durasi = int(input("Durasi acara (Menit): "))
Total_Menit = Menit + Durasi 

# Menghitung jam akhir dan menit akhir agar outputnya lengkap dan logis
Jam_Akhir = (Jam + (Total_Menit // 60)) % 24
Menit_Akhir = Total_Menit % 60
print(f"Acara selesai pada pukul -> {Jam_Akhir:02d}:{Menit_Akhir:02d}")

print("\n===============================================TERIMAKASIH===============================================")
print("---------------------------------------------------------------------------------------------------------\n")