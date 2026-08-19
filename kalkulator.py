# Menampilkan menu
print("=== KALKULATOR SEDERHANA ===")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta pilihan dari user
pilihan = input("Pilih operasi (1/2/3/4): ")

# Input nilai
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

# Proses sesuai pilihan
if pilihan == '1':
    hasil = a + b
    print("Hasil penjumlahan a + b =", hasil)
elif pilihan == '2':
    hasil = a - b
    print("Hasil pengurangan a - b =", hasil)
elif pilihan == '3':
    hasil = a * b
    print("Hasil perkalian a * b =", hasil)
elif pilihan == '4':
    if b != 0:
        hasil = a / b
        print("Hasil pembagian a / b =", hasil)
    else:
        print("Error: Tidak bisa membagi dengan nol!")
else:
    print("Pilihan tidak valid!")