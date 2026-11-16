# Marchellina Crachia
# 065002600045
# Fungsi Rekursif

def jumlah_rekursif(n):
    if n <= 0:
        return 0
    else:
        angka = int(input(f"Masukkan angka ke-{n}: "))
        return angka + jumlah_rekursif(n - 1)

# Program Utama
jumlah_input = int(input("Masukkan Jumlah: "))
hasil = jumlah_rekursif(jumlah_input)
print(f"Hasil dari penjumlahan adalah: {hasil}")
