print("\n===============================================PERTEMUAN 11===============================================")
print("----------------------------------------------AZHALIA MOZAIK---------------------------------------------")

#===============================================Soal No.1================================================
print("\n===============================================Soal No.1================================================")
def memulai_ujian(nilai=True):
    print("Tiga.....")
    print("Dua.....")
    print("Satu.....")
    if not nilai:
        return
    
    print("Selamat Mengerjakan Ujian! Kerjakan Sebaik-baiknya")

memulai_ujian()

#===============================================Soal No.2================================================
print("\n===============================================Soal No.2================================================")
def memulai_ujian(nilai=True):
    print("Tiga.....")
    print("Dua.....")
    print("Satu.....")
    if not nilai:
        return
    
    print("Selamat Mengerjakan Ujian! Kerjakan Sebaik-baiknya")

memulai_ujian(False)

#===============================================Soal No.3================================================
print("\n===============================================Soal No.3================================================")
def nilai(a, b): 
    return a + b          

nilai_akhir = nilai(42, 44)
print("Nilai Akhir: ", nilai_akhir)

#===============================================Soal No.4================================================
print("\n===============================================Soal No.4================================================")
def nilai():  
    print("Nilai aku kurang bagus")
    return 0

print("Nilai aku pas banget KKM")
nilai()
print("Aku harus mulai belajar agar nilaiku meningkat")

#===============================================Soal No.5================================================
print("\n===============================================Soal No.5================================================")
def nilai(n):
    if (n % 2 == 0):
        return True
    
print(nilai(15))
print(nilai(14))

#===============================================Soal No.6================================================
print("\n===============================================Soal No.6================================================")
def penjumlahan(daftar):
    s = 0

    for elemen in daftar :
        s += elemen

    return s

print(penjumlahan([15, 59, 25]))

#===============================================Soal No.7================================================
print("\n===============================================Soal No.7================================================")
def penjumlahan(daftar):
    s = 0

    for elemen in daftar :
        s += elemen

    return s

#print(penjumlahan(15))  #HAPUS # PADA print(penjumlahan(15)) AKAN EROR KARENA MEMASUKKAN ANGKA TUNGGAL '15' (BUKAN LIST)

#===============================================Soal No.8================================================
print("\n===============================================Soal No.8================================================")
def fungsi_aneh(n):
    list_aneh = []

    for i in range(0, n):
        list_aneh.insert(0, i)

    return list_aneh

print(fungsi_aneh(15))

#===============================================Soal No.9================================================
print("\n===============================================Soal No.9================================================")
def tahun_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

for i in range(len(data_uji)):
    th = data_uji[i]
    print(th, "-> ", end="")
    
    hasil = tahun_kabisat(th)
    
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")

#===============================================Soal No.10===============================================
print("\n===============================================Soal No.10===============================================")
def tahun_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

def hari_didalam_bulan(tahun, bulan):
    jumlah_hari = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if bulan == 2 and tahun_kabisat(tahun):
        return 29
    return jumlah_hari[bulan]

data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

for i in range(len(data_uji)):
    thn = data_uji[i]
    bln = data_bulan[i]
    
    print(thn, bln, "-> ", end="")
    
    hasil = hari_didalam_bulan(thn, bln)
    
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")

#===============================================Soal No.11===============================================
print("\n===============================================Soal No.11===============================================")
def tahun_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

def hari_didalam_bulan(tahun, bulan):
    if bulan < 1 or bulan > 12:
        return None
        
    jumlah_hari = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if bulan == 2 and tahun_kabisat(tahun):
        return 29
        
    return jumlah_hari[bulan]

def hari_pada_tahun(tahun, bulan, hari):
    if tahun < 1:
        return None
        
    maks_hari = hari_didalam_bulan(tahun, bulan)
    if maks_hari is None or hari < 1 or hari > maks_hari:
        return None
    
    total_hari = 0
    
    for bln in range(1, bulan):
       total_hari += hari_didalam_bulan(tahun, bln)        
       total_hari += hari
       return total_hari

print(hari_pada_tahun(2000, 12, 31))

#===============================================Soal No.12===============================================
print("\n===============================================Soal No.12===============================================")
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
        
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
            
    return True

for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
        
print()

#===============================================Soal No.13===============================================
print("\n===============================================Soal No.13===============================================")
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
        
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
            
    return True

for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
        
print()

#===============================================Soal No.14===============================================
print("\n===============================================Soal No.14===============================================")
def Liter100km_ke_mpg(liter):
    mil = 100 / 1.609344
    galon = liter / 3.785411784
    return mil / galon

def mpg_ke_Liter100km(mil):
    liter = 3.785411784
    km100 = (mil * 1.609344) / 100
    return liter / km100

print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.0))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))

print("\n===============================================TERIMAKASIH===============================================")
print("---------------------------------------------------------------------------------------------------------\n")