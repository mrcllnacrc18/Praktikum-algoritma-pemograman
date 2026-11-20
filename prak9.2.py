# Marchellina Crachia
# 065002600045
# Latihan 2 Modul 9


def buat_file():
  nama_file = input("Masukkan Nama File: ")
  nama = input("Masukkan Namamu: ")
  nim = input("Masukkan NIM kamu: ")
  angkatan = input("Masukkan tahun angkatanmu: ")

  file = open(nama_file + ".txt", "w")
  file.write(f"Nama: {nama}\nNIM: {nim}\nAngkatan: {angkatan}\n")
  file.close()
  print("File Berhasil Dibuat")


def baca_file():
  nama_file = input("Masukkan Nama File: ")

  file = open(nama_file + ".txt", "r")
  print(file.read())
  file.close()


def tambah_file():
  nama_file = input("Masukkan Nama File: ")
  sahabat = input("Masukkan Nama Sahabatmu: ")
  catatan = input("Masukkan Catatan Tambahan kamu: ")

  file = open(nama_file + ".txt", "a")
  file.write(f"Nama Sahabat: {sahabat}\nCatatan: {catatan}\n")
  file.close()
  print("Data Berhasil Ditambahkan")


while True:
  print("===== Program File Handling =====")
  print("1. Membuat dan Menulis File")
  print("2. Membaca File")
  print("3. Menambahkan Text Pada File")
  print("4. Keluar Dari Program")

  pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4): ")

  if pilihan == "1":
    buat_file()
  elif pilihan == "2":
    baca_file()
  elif pilihan == "3":
    tambah_file()
  elif pilihan == "4":
    print("Terima Kasih Sudah Menggunakan Program Saya")
    break
  else:
    print("Pilihan tidak valid")
