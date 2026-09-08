#Pengelompokan Nilai Ujian Mahasiswa

batas_nilai = (65, 100)
nilai_masuk = []
lulus = []
remedial = []

print("Masukkan nilai ujian mahasiswa (ketik 'selesai' untuk berhenti):")

while True:
    data = input("Nilai: ")
    if data.lower() == "selesai":
        if len(nilai_masuk) < 5:
            print("Minimal harus ada 5 nilai! Silakan lanjutkan input.")
            continue
        if len(lulus) == 0 or len(remedial) == 0:
            print("Harus ada nilai Lulus dan Remedi! Silakan lanjutkan input.")
            continue
        break
    try:
        nilai = int(data)
        if nilai < 0 or nilai > batas_nilai[1]:
            print("Nilai harus antara 0 - 100.")
            continue
        nilai_masuk.append(nilai)

        if nilai >= batas_nilai[0]:
            lulus.append(nilai)
        else:
            remedial.append(nilai)
    except ValueError:
        print("Input tidak valid. Masukkan angka atau 'selesai'.")

print("\napakah anda ingin dihapus? (ketik 'ya' untuk menghapus, 'tidak' untuk melanjutkan):")
konfirmasi_hapus = input()
if konfirmasi_hapus.lower() == "ya":
    hapus = input("nilai yang ingin dihapus:")
    try:
        hapus = int(hapus)
        if hapus in nilai_masuk:
            nilai_masuk.remove(hapus)
            if hapus >= batas_nilai[0]:
                lulus.remove(hapus)
            else:
                remedial.remove(hapus)
            print(f"Nilai {hapus} telah dihapus.")
        else:
            print(f"Nilai {hapus} tidak ditemukan dalam daftar.")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

print("\n^~^ Hasil Akhir Pengelompokan Nilai Ujian Mahasiswa ^~^")
print("nilai yang masuk:", nilai_masuk)
print("nilai lulus:", lulus)
print("nilai remedial:", remedial)
print("nilai hapus:", hapus)
