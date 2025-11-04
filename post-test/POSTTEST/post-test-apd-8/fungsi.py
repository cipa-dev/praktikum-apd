import os
from data import akun, produk, transaksi        
from prettytable import PrettyTable
from warna import TITLE, SUCCESS, ERROR, RESET
# fungsi tanpa parameter
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def tampilkan_produk():
    print("\n--- Daftar Produk Syifa Hijab ---")
    if not produk:
        print(ERROR + "Belum Ada Produk")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama", "Harga", "Stok"]
        for i, item in enumerate(produk):
            table.add_row([i+1, item['nama'], item['harga'], item['stok']])
        table.align["Nama"] = "l"
        print(table)
# fungsi dengan parameter
def tambah_produk(nama, harga, stok):
    produk.append({"nama": nama, "harga": harga, "stok": stok})
def ubah_produk(index, nama, harga, stok):
    produk[index] = {"nama": nama, "harga": harga, "stok": stok}
def hapus_produk(index):
    produk.pop(index)
def cetak_struk(nama, harga, jumlah):
    tabel = PrettyTable()
    total = harga * jumlah
    print("\n--- Struk Pembelian ---")
    tabel.field_names = ["Produk", "Harga Satuan", "Jumlah", "Total Harga"]
    tabel.add_row([nama, harga, jumlah, total])
    print(tabel)
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