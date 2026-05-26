print("\n===============================================PERTEMUAN 7===============================================")
print("----------------------------------------------AZHALIA MOZAIK---------------------------------------------")

#===============================================Soal No.1================================================
print("\n===============================================Soal No.1================================================")
Kebutuhan = ["Tisu", "Sikat Gigi", "Parfum", "Sabun"]
print(" Kebutuhan yang diperlukan:", Kebutuhan)
Kebutuhan[0] = "Tisu Basah"
print("\n Ini Kebutuhan Sebelumnya:", Kebutuhan)
Kebutuhan[2] = Kebutuhan[3]
print(" Kebutuhan sekarang:", Kebutuhan)

#===============================================Soal No.2================================================
print("\n===============================================Soal No.2================================================")
Kebutuhan = ["Tisu", "Sikat Gigi", "Parfum", "Sabun", "Shampo"]
print(Kebutuhan[0])
print(Kebutuhan[3])
print(Kebutuhan)

#===============================================Soal No.3================================================
print("\n===============================================Soal No.3================================================")
Kebutuhan = ["Tisu", "Sikat Gigi", "Parfum", "Sabun", "Shampo"]
print("Kebutuhan yang diperlukan:", len(Kebutuhan))

#===============================================Soal No.4================================================
print("\n===============================================Soal No.4================================================")
Kebutuhan = ["Tisu", "Sikat Gigi", "Parfum", "Sabun", "Shampo"]
del Kebutuhan[1]
print(len(Kebutuhan))
print(Kebutuhan)

#===============================================Soal No.5================================================
print("\n===============================================Soal No.5================================================")
Kebutuhan = ["Tisu", "Sikat Gigi", "Parfum", "Sabun", "Shampo"]
print(Kebutuhan[-1])
print(Kebutuhan[-2])
print(Kebutuhan[-3])
print(Kebutuhan[-4])
print(Kebutuhan[-5])

#===============================================Soal No.6================================================
print("\n===============================================Soal No.6================================================")
Topi_List = [1, 2, 3, 4, 5]
Topi_List[2] = int(input("Masukkan Angka Integer: "))
del Topi_List[-1]
print("Total List saat ini: ", len(Topi_List))
print(Topi_List)

#===============================================Soal No.7================================================
print("\n===============================================Soal No.7================================================")
Kebutuhan = ["Tisu", "Sikat Gigi", "Parfum", "Sabun"]
print(len(Kebutuhan))
print(Kebutuhan)

Kebutuhan.append("Shampo")
print(len(Kebutuhan))
print(Kebutuhan)

Kebutuhan.insert(1, "Kaca")
print(len(Kebutuhan))
print(Kebutuhan)

#===============================================Soal No.8================================================
print("\n===============================================Soal No.8================================================")
Buku = []
for i in range(5):
    Buku.append(i + 3)
print(Buku)

#===============================================Soal No.9================================================
print("\n===============================================Soal No.9================================================")
Buku = []
for i in range(5):
    Buku.insert(0, i + 3) 
print(Buku)

#===============================================Soal No.10===============================================
print("\n===============================================Soal No.10===============================================")
Nomor = [25, 30, 80, 10, 59]
Total = 0
for i in range(len(Nomor)):
    Total += Nomor[i]
print(Total)

#===============================================Soal No.11===============================================
print("\n===============================================Soal No.11===============================================")
Nomor = [25, 30, 80, 10, 59]
Total = 0
for i in Nomor:
    Total += i
print(Total)

#===============================================Soal No.12===============================================
print("\n===============================================Soal No.12===============================================")
# CODE 1
My_List = [25, 30, 80, 10, 59]
My_List[0], My_List[4] = My_List[4], My_List[0] 
My_List[1], My_List[3] = My_List[3], My_List[1]
print(My_List) 
My_List = [25, 30, 80, 10, 59]

# CODE 2
List = len(My_List)
for i in range(List // 2):
    My_List[i], My_List[List - i - 1] = My_List[List - i - 1], My_List[i]
print(My_List)
 
#===============================================Soal No.13===============================================
print("\n===============================================Soal No.13===============================================")
exo = []
print("Langkah 1:", exo)

exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("Langkah 2:", exo)

Anggota_Tambahan = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for nama in Anggota_Tambahan:
    exo.append(nama)
print("Langkah 3:", exo)

exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
print("Langkah 4:", exo)

exo.insert(-2, "Xiumin")
print("Langkah 5:", exo)

print("Jumlah Anggota Exo:", len(exo))

print("\n===============================================TERIMAKASIH===============================================")
print("---------------------------------------------------------------------------------------------------------\n")