

def get_ordinal(angka):
  if 11 <= angka <= 13:
    sufiks = "th"
  elif angka % 10 == 1:
    sufiks = "st"
  elif angka % 10 == 2:
    sufiks = "nd"
  elif angka % 10 == 3:
    sufiks = "rd"
  else:
    sufiks = "th"
  return angka, sufiks


# Program Utama
print("Ordinal Number")
print("ketik 0 untuk menghentikan program")

while True:
  masukkan = int(input("masukkan angka: "))
  if masukkan == 0:
    print((0, "th"))
    print("terima kasih telah menggunakan program saya")
    break
  print(get_ordinal(masukkan))
