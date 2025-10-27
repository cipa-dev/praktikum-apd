import os
# variabel global
akun = {
    "admin": {"password": "004", "role": "admin"},
    "member": {"password": "cipa", "role": "member"}
}
produk = []
transaksi = []
# fungsi tanpa parameter
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def tampilkan_produk():
    print("\n--- Daftar Produk Syifa Hijab ---")
    if not produk:
        print("Belum Ada Produk")
    else:
        for i, item in enumerate(produk):
            print(f"{i+1}. Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")
# fungsi dengan parameter
def tambah_produk(nama, harga, stok):
    produk.append({"nama": nama, "harga": harga, "stok": stok})
def ubah_produk(index, nama, harga, stok):
    produk[index] = {"nama": nama, "harga": harga, "stok": stok}
def hapus_produk(index):
    produk.pop(index)
def cetak_struk(nama, harga, jumlah):
    total = harga * jumlah
    print("\n--- Struk Pembelian ---")
    print(f"Produk: {nama}")
    print(f"Harga Satuan: {harga}")
    print(f"Jumlah: {jumlah}")
    print(f"Total Harga: {total}")
    print("Terima Kasih Telah Berbelanja di Syifa Hijab!")
# fungsi rekursif untuk login
def login():
    clear()
    print("--- Login ---")
    username = input("Username: ")
    password = input("Password: ")
    if username in akun and akun[username]["password"] == password:
        return akun[username]["role"], username
    else:
        print("Login Gagal, Coba Lagi")
        input("Tekan Enter Untuk Ulangi")
        return login()
# fungsi rekursif untuk membeli produk
def beli_produk():
    tampilkan_produk()
    try:
        idx = int(input("Pilih Nomor Produk: ")) - 1
        if idx < 0 or idx >= len(produk):
            raise IndexError
        jumlah = int(input("Jumlah yang ingin dibeli: "))
        if jumlah <= 0:
            raise ValueError
        if produk[idx]["stok"] >= jumlah:
            produk[idx]["stok"] -= jumlah
            cetak_struk(produk[idx]["nama"], produk[idx]["harga"], jumlah)
        else:
            print("Stok Tidak Cukup")
    except (ValueError, IndexError):
        print("Input Tidak Valid, Coba Lagi")
        input("Tekan Enter Untuk Ulangi")
        beli_produk()
# daftar menu program
while True:
    clear()
    print("---Selamat Datang Di Syifa Hijab---")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih Menu: ")
# jika username dan pw admin
    if menu_awal == "1":
        role, username = login()
        if role == "admin":
            while True:
                clear()
                print("--- Menu Admin ---")
                print("1. Tampilkan Produk")
                print("2. Tambah Produk")
                print("3. Ubah Produk")
                print("4. Hapus Produk")
                print("5. Logout")
                menu_admin = input("Pilih Menu: ")
# menu admin untuk menampilkan produk
                if menu_admin == "1":
                    tampilkan_produk()
                    input("Tekan Enter Untuk Lanjut")
# menu admin untuk menambah produk
                elif menu_admin == "2":
                    print("\n--- Tambah Produk Baru ---")
                    nama = input("Nama produk: ")
                    try:
                        harga = int(input("Harga: "))
                        stok = int(input("Stok: "))
                        tambah_produk(nama, harga, stok)
                        print("Produk Berhasil Ditambahkan")
                    except ValueError:
                        print("Harga dan Stok harus berupa angka")
                    input("Tekan Enter Untuk Lanjut")
# menu admin untuk mengubah produk
                elif menu_admin == "3":
                    tampilkan_produk()
                    try:
                        idx = int(input("Pilih Nomor Produk: ")) - 1
                        nama = input("Nama Baru: ")
                        harga = int(input("Harga Baru: "))
                        stok = int(input("Stok Baru: "))
                        ubah_produk(idx, nama, harga, stok)
                        print("Produk Berhasil Diubah")
                    except (ValueError, IndexError):
                        print("Input Tidak Valid")
                    input("Tekan Enter Untuk Lanjut")
# menu admin untuk menghapus produk
                elif menu_admin == "4":
                    tampilkan_produk()
                    try:
                        idx = int(input("Pilih Nomor Produk: ")) - 1
                        hapus_produk(idx)
                        print("Produk Berhasil Dihapus")
                    except (ValueError, IndexError):
                        print("Nomor Tidak Valid")
                    input("Tekan Enter Untuk Lanjut")
# jika pilihan tidak valid
                elif menu_admin == "5":
                    break
                else:
                    print("Pilihan Tidak Valid")
                    input("Tekan Enter Untuk Lanjut")
# jika login sebagai member
        elif role == "member":
            while True:
                clear()
                print("--- Menu Member ---")
                print("1. Lihat Produk")
                print("2. Beli Produk")
                print("3. Logout")
                menu_member = input("Pilih Menu: ")
# menu member untuk melihat produk
                if menu_member == "1":
                    tampilkan_produk()
                    input("Tekan Enter Untuk Lanjut")
# menu member untuk membeli produk
                elif menu_member == "2":
                    print("\n--- Beli Produk ---")
                    if not produk:
                        print("Belum Ada Produk")
                    else:
                        beli_produk()
                    input("Tekan Enter Untuk Lanjut")
# jika pilihan tidak valid
                elif menu_member == "3":
                    break
                else:
                    print("Pilihan Tidak Valid")
                    input("Tekan Enter Untuk Lanjut")
# membuat akun baru untuk login
    elif menu_awal == "2":
        clear()
        print("--- Register Akun Baru ---")
        username = input("Username baru: ")
        password = input("Password: ")
        role = input("Role (admin/member): ").lower() # memilih role admin atau member
        if username in akun:
            print("Username Sudah Digunakan.") # jika username dan password sudah digunakan
        elif role not in ["admin", "member"]:
            print("Role Tidak Valid.")
        else:
            akun[username] = {"password": password, "role": role}
            print("Akun Berhasil Dibuat.")
        input("Tekan Enter Untuk Lanjut")
# keluar dari program
    elif menu_awal == "3":
        print("Terima Kasih Telah Menggunakan Program Syifa Hijab")
        break
# jika pilihan tidak valid
    else:
        print("Pilihan Tidak Valid")
        input("Tekan Enter Untuk Lanjut")