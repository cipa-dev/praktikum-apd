import os
while True:
    os.system('cls')
    print('=== Selamat Datang Di Syifa Hijab ===')
    status = input('Apakah Anda Memiliki Member Syifa Hijab? (y/n): ').lower()
    login = False

    if status == 'y':
        print('\n=== Login Member ===')
        attempts = 3
        while attempts > 0:
            username = input('Masukkan username: ')
            password = input('Masukkan password: ')
            if username.strip() == '' or password.strip() == '':
                print('Username dan password tidak boleh kosong!')
                continue
            login = True if username == 'cipa' and password == '004' else False
            if login:
                print('Login berhasil! Selamat Berbelanja Di Syifa Hijab.\n')
                break
            else:
                attempts -= 1
                print(f'Login gagal! Sisa percobaan: {attempts}')
        if not login:
            print('\nAnda Berbelanja Sebagai Non-member.\n')
    elif status == 'n':
        print('\nAnda Berbelanja Sebagai Non-member.\n')
    else:
        print('\nInput tidak valid. Anda dianggap sebagai Non-member.\n')

    # daftar produk dan harga
    keranjang = ''
    total = 0
    pashmina = 70000
    segiempat = 35000
    instan = 40000
    ciput = 15000
    peniti = 5000
    # menu belanja
    while True:
        print('=== Produk Syifa Hijab ===')
        print('1. Hijab Pashmina - Rp 70.000')
        print('2. Hijab Segi Empat - Rp 35.000')
        print('3. Hijab Instan - Rp 40.000')
        print('4. Ciput - Rp 15.000')
        print('5. Peniti - Rp 5.000')
        print('0. Checkout')
        pilihan = input('Pilih produk (1-0): ')
        # proses input dan hitung total
        if pilihan == '1':
            jumlah = int(input('Jumlah Hijab Pashmina: '))
            subtotal = jumlah * pashmina
            total += subtotal
            keranjang += f'{jumlah} Hijab Pashmina - Rp {subtotal:,}\n'
            print(f'Produk berhasil ditambahkan. Total sementara: Rp {total:,}\n')
        elif pilihan == '2':
            jumlah = int(input('Jumlah Hijab Segi Empat: '))
            subtotal = jumlah * segiempat
            total += subtotal
            keranjang += f'{jumlah} Hijab Segi Empat - Rp {subtotal:,}\n'
            print(f'Produk berhasil ditambahkan. Total sementara: Rp {total:,}\n')
        elif pilihan == '3':
            jumlah = int(input('Jumlah Hijab Instan: '))
            subtotal = jumlah * instan
            total += subtotal
            keranjang += f'{jumlah} Hijab Instan - Rp {subtotal:,}\n'
            print(f'Produk berhasil ditambahkan. Total sementara: Rp {total:,}\n')
        elif pilihan == '4':
            jumlah = int(input('Jumlah Ciput: '))
            subtotal = jumlah * ciput
            total += subtotal
            keranjang += f'{jumlah} Ciput - Rp {subtotal:,}\n'
            print(f'Produk berhasil ditambahkan. Total sementara: Rp {total:,}\n')
        elif pilihan == '5':
            jumlah = int(input('Jumlah Peniti: '))
            subtotal = jumlah * peniti
            total += subtotal
            keranjang += f'{jumlah} Peniti - Rp {subtotal:,}\n'
            print(f'Produk berhasil ditambahkan. Total sementara: Rp {total:,}\n')
        elif pilihan == '0':
            os.system('cls')
            print('=== Struk Belanja Syifa Hijab ===')
            print(keranjang)
            if login:
                diskon = int(total * 0.15)
                total_bayar = total - diskon
                print(f'Total Sebelum Diskon : Rp {total:,}')
                print(f'Diskon 15%            : Rp {diskon:,}')
                print(f'Total Setelah Diskon : Rp {total_bayar:,}')
            else:
                print(f'Total Belanja : Rp {total:,}')
            print('=== TERIMA KASIH SUDAH BERBELANJA DI SYIFA HIJAB ===\n')
            break
        else:
            print('Pilihan tidak valid!\n')
            # ulangi loop menu belanja
    ulang = input('Apakah Anda ingin melakukan transaksi baru? (y/n): ').lower()
    if ulang != 'y':
        print('Terima Kasih Telah Berbelanja, Sampai Jumpa Lagi Di Syifa Hijab!')
        break

