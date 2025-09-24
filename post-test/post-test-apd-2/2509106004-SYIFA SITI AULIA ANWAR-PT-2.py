# Input data pasien
nama = input("Masukkan Nama Pasien: ")
tinggi = float(input("Masukkan Tinggi Badan (cm): "))
berat = float(input("Masukkan Berat Badan (kg): "))

# Hitung berat ideal
beratIdeal = tinggi - 100
selisih = berat - beratIdeal

# Flags boolean
isKekurangan = selisih < -5
isNormal = -5 <= selisih <= 5
isKelebihan = selisih > 5

# List status
statusList = ["Kekurangan Berat Badan", "Berat Badan Normal", "Kelebihan Berat Badan"]

# Boolean sebagai index
statusIndex = [isKekurangan, isNormal, isKelebihan].index(True)
status = statusList[statusIndex]

# Hasil cek dalam format tabel
print("=" * 65)
print(f"|{'HASIL CEK BERAT BADAN':^63}|")
print("=" * 65)
print(f"| Nama Pasien     :{nama:<45}|")
print(f"| Tinggi Badan    :{tinggi:>4.1f} cm{'':<37}|")
print(f"| Berat Badan     :{berat:>4.1f} kg{'':<38}|")
print(f"| Berat Ideal     :{beratIdeal:>4.1f} kg{'':<38}|")
print(f"| Status          :{status:<45}|")
print("=" * 65)