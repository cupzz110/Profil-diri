import random

angka_rahasia = random.randint(1, 100)
percobaan = 0

print("=============================")
print("       GAME TEBAK ANGKA      ")
print("=============================")
print("Saya memilih angka dari 1-100.\n")

while True:
    try:
        tebakan = int(input("Masukkan tebakan: "))
    except ValueError:
        print("Input harus berupa angka!\n")
        continue
    except (EOFError, KeyboardInterrupt):
        print("\nInput dibatalkan. Program selesai.")
        raise SystemExit

    percobaan += 1

    if tebakan > angka_rahasia:
        print("Terlalu besar!\n")
    elif tebakan < angka_rahasia:
        print("Terlalu kecil!\n")
    else:
        print("\nSELAMAT! Tebakan kamu benar!")
        print(f"Percobaan: {percobaan}")
        break