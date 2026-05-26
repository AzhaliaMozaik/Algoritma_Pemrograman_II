print("\n=================================PERTEMUAN 6=================================")
print("--------------------------------AZHALIA MOZAIK-------------------------------")

#=================================Soal No.1==================================
print("\n=================================Soal No.1==================================")
# Catatan: Loop ini bersifat infinite (berjalan terus), tekan Ctrl+C di terminal untuk menghentikan.
while True:
    print("Believe in yourself")
    break # Ditambahkan break sementara agar tidak hang saat dicoba, silakan hapus jika ingin benar-benar infinite

#=================================Soal No.2==================================
print("\n=================================Soal No.2==================================")
Pulpen = 4
while Pulpen <= 70:
    print("Pulpen")
    Pulpen *= 2

#=================================Soal No.3==================================
print("\n=================================Soal No.3==================================")
Angka_Genap = 0
Angka_Ganjil = 0
Angka = int(input("Masukkan suatu angka (Jika ingin berhenti ketik angka 0): "))
while Angka != 0:
    if Angka % 2 == 1:
        Angka_Ganjil += 1
    else:
        Angka_Genap += 1
    Angka = int(input("Masukkan suatu angka (Jika ingin berhenti ketik angka 0): "))
print("Jumlah Angka Ganjil: ", Angka_Ganjil)
print("Jumlah Angka Genap: ", Angka_Genap)

#=================================Soal No.4==================================
print("\n=================================Soal No.4==================================")
secret_number = 777

print(
"""
+==========================================+
| Selamat datang di game saya, muggle!     |
|                                          |
| Masukkan suatu angka dan tebak           |
| angka berapa yang saya  pilih            |
| untukmu.                                 |
| Jadi, berapakah angka rahasianya         |
+==========================================+
""")

Tebak_angka = int(input("Masukkan angka: "))

while Tebak_angka != secret_number:
    print("hahaha! kamu nyangkut deh di Loop saya")
    Tebak_angka = int(input("Masukkan angka lagi: "))

print(secret_number, "Selamat, Muggle! kamu bebas sekarang!")

#=================================Soal No.5==================================
print("\n=================================Soal No.5==================================")
for A in range(5):
    print("Nilai A saat ini adalah", A)
print()
for B in range(5, 9):
    print("Nilai B saat ini adalah", B)
print()
for C in range(1, 5, 9):
    print("Nilai C saat ini adalah", C)
print()
for D in range(2, 2):
    print("Nilai D saat ini adalah", D)
print()
for E in range(8, 3):
    print("Nilai E saat ini adalah", E)
print()

#=================================Soal No.6==================================
print("=================================Soal No.6==================================")
Power = 1
for expo in range(11):
    print("2 Pangkat ", expo, "adalah", Power)
    Power *= 2

#=================================Soal No.7==================================
print("\n=================================Soal No.7==================================")
#break
print("Intruksi Break: ")
for i in range(1, 7):
    if i == 4:
        break
    print("Bagian ini ada di dalam Loop", i)
print("Bagian ini ada di luar Loop")

#continue
print("\nIntruksi Continue:")
for i in range(1, 6):
    if i == 2:
        continue
    print("Bagian ini ada di dalam Loop", i)
print("Bagian ini ada di luar Loop")

#=================================Soal No.8==================================
print("\n=================================Soal No.8==================================")
secret_number = 777

print(
"""
+==========================================+
| Selamat datang di game saya, muggle!     |
|                                          |
| Masukkan suatu angka dan tebak           |
| angka berapa yang saya  pilih            |
| untukmu.                                 |
|                                          |
| Jadi, berapakah angka rahasianya         |
+==========================================+
""")

while True:
    Tebak_angka = int(input("Masukkan angka: "))
    
    if Tebak_angka == secret_number:
        print("SELAMAT, MUGGLE! KAMU BEBAS SEKARANG")
        break
    else:
        print("Hahaha! Kamu Tersangkut di Loop Saya, Ayo Tebak Lagi")

#=================================Soal No.9==================================
print("\n=================================Soal No.9==================================")
Kata = input("Masukkan suatu kata: ")
User_word = Kata.upper()

print("\nOutput:")
for Huruf in User_word:
    if Huruf == "A":
        continue
    elif Huruf == "I":
        continue
    elif Huruf == "U":
        continue
    elif Huruf == "E":
        continue
    elif Huruf == "O":
        continue
    else:
        print(Huruf)

#=================================Soal No.10=================================
print("\n=================================Soal No.10=================================")
A = 2   
while A <= 15:
    print(A)
    A += 2
else:
    print("else: ", A)

#=================================Soal No.11=================================
print("\n=================================Soal No.11=================================")
A = 15
B = 59
C = 59

print(A < B)   
print(A != B)  
print(B == C)  
print(C < A)   

print(A < B and B == C) 
print(A < B or C > A)    
print(not(A > B))        

#=================================Soal No.12=================================
print("\n=================================Soal No.12=================================")
A = 15
B = 59
C = 59

print(A < B)   
print(A != B)  
print(B == C)  
print(C < A)   

print(A < B and B == C) 
print(A < B or C > A)    
print(not(A > B))        

#=================================Soal No.13=================================
print("\n=================================Soal No.13=================================")
#Logical
A = True
B = False

print(A and B) 
print(A or B)    
print(not A)       

#Bit
A = 1
B = 5

print(A & B)
print(A | B)
print(A ^ B)
print(~ A)

#=================================Soal No.14=================================
print("\n=================================Soal No.14=================================")
A = 15
print(A << 1)
print(A >> 1)

#=================================Soal No.15=================================
print("\n=================================Soal No.15=================================")
X = 2
Y = 5

A = X & Y
B = X | Y
C = ~ X
D = X ^ 2
E = X >> 3
F = X << 1

print("A (X & Y) :", A)
print("B (X | Y) :", B)
print("C (~ X)   :", C)
print("D (X ^ 2) :", D)
print("E (X >> 3):", E)
print("F (X << 1):", F)

print("\n=================================TERIMAKASIH=================================")
print("-----------------------------------------------------------------------------\n")