# Marchellina Crachia
# 065002600045
# Modul 8 Latihan 2

print(
    "Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk"
    " berhenti"
)
angka_input = input("Masukkan Angka: ")

if angka_input == "":
  print("Program Selesai")
else:
  pangkat_input = input("Masukkan Pangkatnya: ")


  def pangkat(basis, eksponen):
    if eksponen == 0:
      return 1
    elif eksponen > 0:
      return basis * pangkat(basis, eksponen - 1)
    else:
      return 1 / pangkat(basis, -eksponen)


  hasil = pangkat(float(angka_input), int(pangkat_input))
  print(f"Hasilnya adalah: {hasil}")
