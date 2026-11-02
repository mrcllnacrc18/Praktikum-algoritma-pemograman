total_harga = 0.0

while True:
    input_umur = input("masukkan umur: ")
    
    if input_umur.strip() == "":
        break
        
    umur = int(input_umur)
    
    if umur <= 2:
        harga = 0.0
        print("Gratis")
    elif 3 <= umur <= 12:
        harga = 14.0
        print(f"Harga ${harga:.2f}")
    elif umur >= 65:
        harga = 18.0
        print(f"Harga ${harga:.2f}")
    else:
        harga = 23.0
        print(f"Harga ${harga:.2f}")
        
    total_harga += harga
    print(f"Running total: {total_harga:.2f}")

uang = float(input("masukkan jumlah uang: "))
kembalian = uang - total_harga
print(f"Running kembalian: {kembalian:.2f}")
