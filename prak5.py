def konversi_nilai(huruf):
    """Fungsi dengan parameter 'huruf' untuk mengembalikan bobot nilai angka."""
    if huruf == "A":
        return 4.00
    elif huruf == "A-":
        return 3.75
    elif huruf == "B+":
        return 3.50
    elif huruf == "B":
        return 3.00
    elif huruf == "B-":
        return 2.75
    elif huruf == "C+":
        return 2.50
    elif huruf == "C":
        return 2.00
    elif huruf == "C-":
        return 1.75
    elif huruf == "D":
        return 1.50
    elif huruf == "E":
        return 1.25
    else:
        return None  

def hitung_rata_rata():
    """Fungsi utama untuk menjalankan perulangan input dan menghitung rata-rata."""
    total_nilai = 0
    jumlah_input = 0

    while True:
        masukkan = input("masukkan nilai: ")
        
        if masukkan == "":
            pass
            
        # Memanggil fungsi konversi dengan mengirimkan argumen 'masukkan'
        n = konversi_nilai(masukkan)
        
        if n is None:
            print("Nilai tidak valid, silakan masukkan ulang.")
            continue
            
        print(f"nilai = {n}")
        total_nilai += n
        jumlah_input += 1

    if jumlah_input > 0:
        rata_rata = total_nilai / jumlah_input
        print(f"rata - rata nya adalah: {rata_rata}")
    else:
        print("Tidak ada nilai yang dimasukkan.")

# Memanggil fungsi utama program
hitung_rata_rata()
