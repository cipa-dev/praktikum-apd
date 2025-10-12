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
        keranjang = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Menu Member ---")
        print("1. Lihat Produk")
        print("2. Beli Produk")
        print("3. Logout")
        menu_member = input("Pilih Menu: ")
# pilihan menu member
        if menu_member == "1":
            print("\n--- Daftar Produk ---")
            if len(produk) == 0:
                print("Belum Ada Produk")
            else:
                for i in range(len(produk)):
                    print(f"{i+1}. Nama: {produk[i][0]}, Harga: {produk[i][1]}, Stok: {produk[i][2]}")
            input("Tekan Enter Untuk Lanjut")
# menu member untuk membeli produk
        elif menu_member == "2":
            print("\n--- Beli Produk ---")
            if len(produk) == 0:
                print("Belum Ada Produk")
            else:
                for i in range(len(produk)):
                    print(f"{i+1}. Nama: {produk[i][0]}, Harga: {produk[i][1]}, Stok: {produk[i][2]}")
                idx = input("Pilih Nomor Produk: ")
                if idx.isdigit() and 1 <= int(idx) <= len(produk):
                    i = int(idx) - 1
                    jumlah = input("Jumlah yang ingin dibeli: ")
                    if jumlah.isdigit() and int(jumlah) > 0:
                        jumlah = int(jumlah)
                        if produk[i][2] >= jumlah:
                            produk[i][2] -= jumlah
                            total = produk[i][1] * jumlah
                            print("\n--- Struk Pembelian ---")
                            print(f"Produk: {produk[i][0]}")
                            print(f"Harga Satuan: {produk[i][1]}")
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
        elif menu_member == "3":
            break
# tampilan jika pilihan tidak valid
        else:
            print("Pilihan Tidak Valid")
            input("Tekan Enter Untuk Lanjut")