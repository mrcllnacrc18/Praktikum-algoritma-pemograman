# Marchellina Crachia
# 065002600045
# Latihan 1 Praktikum 7

# menentukan prima
def cek_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return False
    return True

# menampilkan hasil
def tampilkan_hasil(n):
    if cek_prima(n):
        print(f"{n} adalah bilangan Prima")
    else:
        print(f"{n} bukanlah bilangan Prima")

# Program Utama
print("Program Pengecek Bilangan Prima")
print("Ketik 0 untuk menghentikan program")

while True:
    input_angka = int(input("Masukkan angka: "))
    
    if input_angka == 0:
        print("Terima kasih telah menggunakan program saya!")
        break
        
    tampilkan_hasil(input_angka)
