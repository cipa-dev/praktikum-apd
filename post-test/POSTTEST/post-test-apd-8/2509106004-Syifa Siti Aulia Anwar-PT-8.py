import os
from data import akun, produk, transaksi
from fungsi import clear, tampilkan_produk, tambah_produk, ubah_produk, hapus_produk, cetak_struk, login, beli_produk
from warna import  TITLE, SUCCESS, ERROR, RESET
# daftar menu program
while True:
    clear()
    print(TITLE + "---Selamat Datang Di Syifa Hijab---")
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
                print(SUCCESS + "--- Menu Admin ---")
                print("1. Tampilkan Produk")
                print("2. Tambah Produk")
                print("3. Ubah Produk")
                print("4. Hapus Produk")
                print("5. Logout")
                menu_admin = input("Pilih Menu: ")
# menu admin untuk menampilkan produk
                if menu_admin == "1":
                    tampilkan_produk()
                    input(RESET + "Tekan Enter Untuk Lanjut")
# menu admin untuk menambah produk
                elif menu_admin == "2":
                    print(SUCCESS + "\n--- Tambah Produk Baru ---")
                    nama = input("Nama produk: ")
                    try:
                        harga = int(input("Harga: "))
                        stok = int(input("Stok: "))
                        tambah_produk(nama, harga, stok)
                        print("Produk Berhasil Ditambahkan")
                    except ValueError:
                        print(ERROR + "Harga dan Stok harus berupa angka")
                    input(RESET + "Tekan Enter Untuk Lanjut")
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
                        print(ERROR + "Input Tidak Valid")
                    input(RESET + "Tekan Enter Untuk Lanjut")
# menu admin untuk menghapus produk
                elif menu_admin == "4":
                    tampilkan_produk()
                    try:
                        idx = int(input("Pilih Nomor Produk: ")) - 1
                        hapus_produk(idx)
                        print("Produk Berhasil Dihapus")
                    except (ValueError, IndexError):
                        print("Nomor Tidak Valid")
                    input(RESET + "Tekan Enter Untuk Lanjut")
# jika pilihan tidak valid
                elif menu_admin == "5":
                    break
                else:
                    print(ERROR + "Pilihan Tidak Valid")
                    input(RESET + "Tekan Enter Untuk Lanjut")
# jika login sebagai member
        elif role == "member":
            while True:
                clear()
                print(SUCCESS + "--- Menu Member ---")
                print("1. Lihat Produk")
                print("2. Beli Produk")
                print("3. Logout")
                menu_member = input("Pilih Menu: ")
# menu member untuk melihat produk
                if menu_member == "1":
                    tampilkan_produk()
                    input(RESET + "Tekan Enter Untuk Lanjut")
# menu member untuk membeli produk
                elif menu_member == "2":
                    print(SUCCESS + "\n--- Beli Produk ---")
                    if not produk:
                        print(ERROR + "Belum Ada Produk")
                    else:
                        beli_produk()
                    input(RESET + "Tekan Enter Untuk Lanjut")
# jika pilihan tidak valid
                elif menu_member == "3":
                    break
                else:
                    print(ERROR + "Pilihan Tidak Valid")
                    input(RESET + "Tekan Enter Untuk Lanjut")
# membuat akun baru untuk login
    elif menu_awal == "2":
        clear()
        print(SUCCESS + "--- Register Akun Baru ---")
        username = input("Username baru: ")
        password = input("Password: ")
        role = input("Role (admin/member): ").lower() # memilih role admin atau member
        if username in akun:
            print(ERROR + "Username Sudah Digunakan.") # jika username dan password sudah digunakan
        elif role not in ["admin", "member"]:
            print(ERROR + "Role Tidak Valid.")
        else:
            akun[username] = {"password": password, "role": role}
            print("Akun Berhasil Dibuat.")
        input(RESET + "Tekan Enter Untuk Lanjut")
# keluar dari program
    elif menu_awal == "3":
        print(TITLE + "Terima Kasih Telah Menggunakan Program Syifa Hijab")
        break
# jika pilihan tidak valid
    else:
        print("Pilihan Tidak Valid")
        input(RESET + "Tekan Enter Untuk Lanjut")