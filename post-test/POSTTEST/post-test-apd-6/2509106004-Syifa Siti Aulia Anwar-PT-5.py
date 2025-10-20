import os
# data akun disimpan dalam dictionary dengan username sebagai key
akun = {
    "admin": {"password": "004", "role": "admin"},
    "member": {"password": "cipa", "role": "member"}
}
# daftar menu program
produk = []
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    clear()
    print("---Selamat Datang Di Syifa Hijab---")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih Menu: ")
    if menu_awal == "1":
        clear()
        print("--- Login ---")
        username = input("Username: ")
        password = input("Password: ")
# jika username dan pw admin
        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
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
                        print("\n--- Daftar Produk Syifa Hijab ---")
                        if not produk:
                            print("Belum Ada Produk")
                        else:
                            for i, item in enumerate(produk):
                                print(f"{i+1}. Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")
                        input("Tekan Enter Untuk Lanjut")
# menu admin untuk menambah produk
                    elif menu_admin == "2":
                        print("\n--- Tambah Produk Baru ---")
                        nama = input("Nama produk: ")
                        harga = input("Harga: ")
                        stok = input("Stok: ")
                        if harga.isdigit() and stok.isdigit():
                            produk.append({"nama": nama, "harga": int(harga), "stok": int(stok)})
                            print("Produk Berhasil Ditambahkan")
                        else:
                            print("Harga Dan Stok Harus Angka")
                        input("Tekan Enter Untuk Lanjut")
# menu admin untuk mengubah produk
                    elif menu_admin == "3":
                        print("\n--- Ubah Produk ---")
                        if not produk:
                            print("Belum Ada Produk")
                        else:
                            for i, item in enumerate(produk):
                                print(f"{i+1}. Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")
                            idx = input("Pilih Nomor Produk: ")
                            if idx.isdigit() and 1 <= int(idx) <= len(produk):
                                i = int(idx) - 1
                                nama = input("Nama Baru: ")
                                harga = input("Harga Baru: ")
                                stok = input("Stok Baru: ")
                                if harga.isdigit() and stok.isdigit():
                                    produk[i] = {"nama": nama, "harga": int(harga), "stok": int(stok)}
                                    print("Produk Berhasil Diubah")
                                else:
                                    print("Harga Dan Stok Harus Angka")
                            else:
                                print("Nomor Tidak Valid")
                        input("Tekan Enter Untuk Lanjut")
# menu admin untuk menghapus produk
                    elif menu_admin == "4":
                        print("\n--- Hapus Produk ---")
                        if not produk:
                            print("Belum Ada Produk")
                        else:
                            for i, item in enumerate(produk):
                                print(f"{i+1}. Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")
                            idx = input("Pilih Nomor Produk: ")
                            if idx.isdigit() and 1 <= int(idx) <= len(produk):
                                produk.pop(int(idx) - 1)
                                print("Produk Berhasil Dihapus")
                            else:
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
# menu member untuk melihat produk yang tersedia
                    if menu_member == "1":
                        print("\n--- Daftar Produk ---")
                        if not produk:
                            print("Belum Ada Produk")
                        else:
                            for i, item in enumerate(produk):
                                print(f"{i+1}. Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")
                        input("Tekan Enter Untuk Lanjut")
# menu member untuk membeli produk
                    elif menu_member == "2":
                        print("\n--- Beli Produk ---")
                        if not produk:
                            print("Belum Ada Produk")
                        else:
                            for i, item in enumerate(produk):
                                print(f"{i+1}. Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")
                            idx = input("Pilih Nomor Produk: ")
                            if idx.isdigit() and 1 <= int(idx) <= len(produk):
                                i = int(idx) - 1
                                jumlah = input("Jumlah yang ingin dibeli: ")
                                if jumlah.isdigit() and int(jumlah) > 0:
                                    jumlah = int(jumlah)
                                    if produk[i]["stok"] >= jumlah:
                                        produk[i]["stok"] -= jumlah
                                        total = produk[i]["harga"] * jumlah
                                        print("\n--- Struk Pembelian ---")
                                        print(f"Produk: {produk[i]['nama']}")
                                        print(f"Harga Satuan: {produk[i]['harga']}")
                                        print(f"Jumlah: {jumlah}")
                                        print(f"Total Harga: {total}")
                                        print("Terima Kasih Telah Berbelanja di Syifa Hijab!")
                                    else:
                                        print("Stok Tidak Cukup")
                                else:
                                    print("Jumlah Harus Angka dan Lebih Dari 0")
                            else:
                                print("Nomor Produk Tidak Valid")
                        input("Tekan Enter Untuk Lanjut")
# jika pilihan tidak valid
                    elif menu_member == "3":
                        break
                    else:
                        print("Pilihan Tidak Valid")
                        input("Tekan Enter Untuk Lanjut")
# jika username dan password salah
        else:
            print("Login Gagal, Cek Kembali Username Dan Password")
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