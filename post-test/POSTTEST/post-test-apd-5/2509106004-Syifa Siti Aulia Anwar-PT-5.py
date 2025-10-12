import os
# login admin dan member
akun = [
    ["admin", "004", "admin"],
    ["member", "cipa", "member"],
]
# daftar menu program
produk = []
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---Selamat Datang Di Syifa Hijab---")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih Menu: ")
# pilihan menu awal 
    if menu_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Login ---")
        username = input("Username: ")
        password = input("Password: ")
        role = None
        for a in akun:
            if a[0] == username and a[1] == password:
                role = a[2]
                break
        if role == None:
            print("Login Gagal, Cek Kembali Username Dan Password")
            input("Tekan Enter Untuk Lanjut")
        elif role == "admin":
            while True:
# pilihan menu admin
                os.system('cls' if os.name == 'nt' else 'clear')
                print("--- Menu Admin ---")
                print("1. Tampilkan Produk")
                print("2. Tambah Produk")
                print("3. Ubah Produk")
                print("4. Hapus Produk")
                print("5. Logout")
                menu_admin = input("Pilih Menu: ")
                if menu_admin == "1":
                    print("\n--- Daftar Produk Syifa Hijab ---")
                    if len(produk) == 0:
                        print("Belum Ada Produk")
                    else:
                        for i in range(len(produk)):
                            print(f"{i+1}. Nama: {produk[i][0]}, Harga: {produk[i][1]}, Stok: {produk[i][2]}")
                    input("Tekan Enter Untuk Lanjut")
# menu admin untuk menambah produk
                elif menu_admin == "2":
                    print("\n--- Tambah Produk Baru ---")
                    nama = input("Nama produk: ")
                    harga = input("Harga: ")
                    stok = input("Stok: ")
                    if harga.isdigit() and stok.isdigit():
                        produk.append([nama, int(harga), int(stok)])
                        print("Produk Berhasil Ditambahkan")
                    else:
                        print("Harga Dan Stok Harus Angka")
                    input("Tekan Enter Untuk Lanjut")
# menu admin untuk mengubah produk
                elif menu_admin == "3":
                    print("\n--- Ubah Produk ---")
                    for i in range(len(produk)):
                        print(f"{i+1}. Nama: {produk[i][0]}, Harga: {produk[i][1]}, Stok: {produk[i][2]}")
                    idx = input("Pilih Nomor Produk: ")
                    if idx.isdigit() and 1 <= int(idx) <= len(produk):
                        i = int(idx) - 1
                        nama = input("Nama Baru: ")
                        harga = input("Harga Baru: ")
                        stok = input("Stok Baru: ")
                        if harga.isdigit() and stok.isdigit():
                            produk[i] = [nama, int(harga), int(stok)]
                            print("Produk Berhasil Diubah")
                        else:
                            print("Harga Dan Stok Harus Angka")
                    else:
                        print("Nomor Tidak Valid")
                    input("Tekan Enter Untuk Lanjut")
# menu admin untuk menghapus produk
                elif menu_admin == "4":
                    print("\n--- Hapus Produk ---")
                    for i in range(len(produk)):
                        print(f"{i+1}. Nama: {produk[i][0]}, Harga: {produk[i][1]}, Stok: {produk[i][2]}")
                    idx = input("Pilih nomor produk: ")
                    if idx.isdigit() and 1 <= int(idx) <= len(produk):
                        produk.pop(int(idx) - 1)
                        print("Produk Berhasil Dihapus")
                    else:
                        print("Nomor Tidak Valid")
                    input("Tekan Enter Untuk Lanjut")
# tampilan jika pilihan tidak valid
                elif menu_admin == "5":
                    break
                else:
                    print("Pilihan Tidak Valid")
                    input("Tekan Enter Untuk Lanjut")
# menu untuk member
        elif role == "member":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("--- Menu Member ---")
                print("1. Lihat Produk")
                print("2. Logout")
                menu_member = input("Pilih Menu: ")
# menampilkan produk yang tersedia
                if menu_member == "1":
                    print("\n--- Daftar Produk ---")
                    if len(produk) == 0:
                        print("Belum Ada Produk")
                    else:
                        for i in range(len(produk)):
                            print(f"{i+1}. Nama: {produk[i][0]}, Harga: {produk[i][1]}, Stok: {produk[i][2]}")
                    input("Tekan Enter Untuk Lanjut")
# tampilan jika pilihan tidak valid
                elif menu_member == "2":
                    break
                else:
                    print("Pilihan Tidak Valid")
                    input("Tekan Enter Untuk Lanjut")
# membuat akun baru
    elif menu_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Register Akun Baru ---")
        username = input("Username baru: ")
        password = input("Password: ")
        role = input("Role (admin/member): ").lower()
        duplikat = False
        for a in akun:
            if a[0] == username:
                duplikat = True
                break
        if duplikat:
            print("Username Sudah Digunakan.")
        elif role not in ["admin", "member"]:
            print("Role Tidak Valid.")
        else:
            akun.append([username, password, role])
            print("Akun Berhasil Dibuat.")
        input("Tekan Enter Untuk Lanjut")

    elif menu_awal == "3":
        print("Terima Kasih Telah Menggunakan Program Syifa Hijab")
        break

    else:
        print("Pilihan Tidak Valid")
        input("Tekan Enter Untuk Lanjut")