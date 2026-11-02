# Marchellina Crachia
# 065002600045
# Modul 6

def is_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    return False

def hitung_hari(bulan, tahun=0):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if is_kabisat(tahun):
            return 29
        else:
            return 28
    return 0

# Program Utama
print("Program ini akan menentukan jumlah hari dalam bulan tertentu")

while True:
    print("Masukkan 0 untuk menghentikan program")
    input_bulan = input("masukkan bulan (1-12): ")
    
    if input_bulan.strip() == "":
        print("Input tidak boleh kosong, silakan masukkan angka (0-12).\n")
        continue

    bulan = int(input_bulan)
    
    if bulan == 0:
        print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
        break
    elif bulan < 1 or bulan > 12:
        print("Bulan tidak valid, silakan masukkan angka 1-12.\n")
        continue
        
    if bulan == 2:
        tahun = int(input("masukkan tahun (e.g., 2021): "))
        jumlah_hari = hitung_hari(bulan, tahun)
    else:
        jumlah_hari = hitung_hari(bulan)
        
    print(f"{jumlah_hari} hari dalam sebulan")
