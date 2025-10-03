import os

# Data akun member (hanya satu contoh)
USERNAME = "cipa"
PASSWORD = "12345"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def login():
    kesempatan = 3
    while kesempatan > 0:
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        
        if username == "" or password == "":
            print("⚠ Username/Password tidak boleh kosong!\n")
            continue

        if username == USERNAME and password == PASSWORD:
            print("✅ Login berhasil!\n")
            return True
        else:
            kesempatan -= 1
            print(f"❌ Login gagal! Sisa percobaan: {kesempatan}\n")

    print("❌ Gagal login 3 kali. Anda dianggap sebagai Non-Member.\n")
    return False

def menu_belanja(is_member):
    keranjang = ""   # string kosong
    total = 0        # total harga

    while True:
        print("=== MENU BELANJA ===")
        print("1. Hijab Pashmina - Rp50000")
        print("2. Hijab Segi Empat - Rp40000")
        print("3. Inner Hijab - Rp20000")
        print("4. Bros - Rp10000")
        print("5. Ciput - Rp15000")
        print("6. Checkout")

        pilihan = input("Pilih produk (1-6): ")

        if pilihan == "1":
            keranjang += "Hijab Pashmina - Rp50000\n"
            total += 50000
            print("🛒 Hijab Pashmina berhasil ditambahkan.")
            print(f"Total sementara: Rp{total}\n")
        elif pilihan == "2":
            keranjang += "Hijab Segi Empat - Rp40000\n"
            total += 40000
            print("🛒 Hijab Segi Empat berhasil ditambahkan.")
            print(f"Total sementara: Rp{total}\n")
        elif pilihan == "3":
            keranjang += "Inner Hijab - Rp20000\n"
            total += 20000
            print("🛒 Inner Hijab berhasil ditambahkan.")
            print(f"Total sementara: Rp{total}\n")
        elif pilihan == "4":
            keranjang += "Bros - Rp10000\n"
            total += 10000
            print("🛒 Bros berhasil ditambahkan.")
            print(f"Total sementara: Rp{total}\n")
        elif pilihan == "5":
            keranjang += "Ciput - Rp15000\n"
            total += 15000
            print("🛒 Ciput berhasil ditambahkan.")
            print(f"Total sementara: Rp{total}\n")
        elif pilihan == "6":
            cetak_struk(keranjang, total, is_member)
            break
        else:
            print("⚠ Pilihan tidak valid!\n")

def cetak_struk(keranjang, total, is_member):
    clear_screen()
    print("=== STRUK BELANJA ===")
    print(keranjang)
    print("------------------------")
    
    if is_member:
        diskon = int(total * 0.15)
        total_bayar = total - diskon
        print(f"Total Sebelum Diskon : Rp{total}")
        print(f"Diskon (15%)         : Rp{diskon}")
        print(f"Total Bayar          : Rp{total_bayar}")
    else:
        print(f"Total Bayar          : Rp{total}")
    print("========================\n")

def main():
    while True:
        clear_screen()
        print("=== Selamat Datang di Syifa Hijab ===")
        status = input("Apakah Anda Member? (y/n): ").lower()
        
        if status == "y":
            is_member = login()
        elif status == "n":
            is_member = False
        else:
            print("⚠ Input tidak valid. Anda dianggap sebagai Non-Member.\n")
            is_member = False
        
        menu_belanja(is_member)
        
        ulang = input("Mulai transaksi baru? (y/n): ").lower()
        if ulang != "y":
            print("Terima kasih sudah berbelanja di Syifa Hijab 💖")
            break

# Jalankan program
main()