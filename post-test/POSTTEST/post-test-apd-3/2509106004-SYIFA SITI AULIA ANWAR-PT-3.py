# program kasir 
# konfirmasi kepemilikan member
print('=== Selamat Datang Di Syifa Hijab ===')
member = input('Apakah Anda Memiliki Member Syifa Hijab? (ya/tidak): ')
if member.lower() == 'ya':
    print("\n=== Login Member ===")
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')

    # autentikasi dengan ternary operator
    login = True if username == 'cipa' and password == '004' else False
    if not login:
        print('Login Gagal! Silahkan Periksa Kembali Username Dan Password Anda.')
        exit()
    else:
        print('Login berhasil! Selamat Berbelanja Di Syifa Hijab.\n')
else:
    print('\nAnda Berbelanja Sebagai Non-member.\n')

# daftar produk
print('=== Daftar Produk Syifa Hijab ===')
print('hijab pashmina', 70000),
print('hijab segi empat', 35000),
print('hijab instan', 40000),
print('ciput', 15000),
print('peniti', 5000), 

# input belanja
hijab_pashmina = int(input('Masukkan Jumlah Hijab Pashmina/pcs :'))
hijab_segiempat = int(input('Masukkan Jumlah Hijab Segi Empat/pcs :'))
hijab_instan  = int(input('Masukkan Jumlah Hijab Instan/pcs :'))
ciput = int(input('Masukkan Jumlah Ciput/pcs :'))
peniti = int(input('Masukkan Jumlah Peniti/pcs :'))

# hitung total belanja
total = (hijab_pashmina * 70000) + (hijab_segiempat * 35000) + (hijab_instan * 40000) + (ciput * 15000) + (peniti * 5000)

if member.lower() == 'ya' and login:
    diskon = total * 0.15
    total_setelah = total - diskon
    print(f'\n=== Struk Belanja Member Syifa Hijab ===')
    print(f'Total Sebelum Diskon : Rp {total:,}')
    print(f'Diskon 15%           : Rp {int(diskon):,}')
    print(f'Total Setelah Diskon : Rp {int(total_setelah):,}')
else:
    print(f'\n=== Struk Belanja Non-Member ===')
    print(f'Total Belanja : Rp {total:,}')

# terimakasih
print('=== TERIMA KASIH SUDAH BERBELANJA DI SYIFA HIJAB ===')
