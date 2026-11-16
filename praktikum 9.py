# Marchellina Crachia
# 065002600045
# Modul 9

def tulis_biodata():
  nama = input("Masukkan Nama mu: ")
  umur = input("Masukkan Umur mu: ")
  alamat = input("Masukkan Alamatmu: ")
  email = input("Masukkan Emailmu: ")
  dosen = input("Masukkan Dosen Walimu: ")

  file = open("Biodata.txt", "w")
  file.write(
      f"Nama: {nama}\nUmur: {umur}\nAlamat: {alamat}\nEmail:"
      f" {email}\nDosen Wali: {dosen}"
  )
  file.close()


def baca_biodata():
  print("\nBerikut Ini Data Kamu")
  file = open("Biodata.txt", "r")
  print(file.read())
  file.close()


tulis_biodata()
baca_biodata()
