# 1. Definisi Fungsi
def cari_mahasiswa(data, nim):
    # Menggunakan get() agar aman dari KeyError jika NIM tidak ditemukan
    return data.get(nim, "Data tidak ditemukan")

def rata_rata_nilai(data):
    if not data:
        return 0
    total_nilai = 0
    for info in data.values():
        total_nilai += info["nilai"]
    return total_nilai / len(data)

# 2. Inisialisasi Dictionary Data Mahasiswa (Minimal 5 mahasiswa)
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

print("=== UJI PENCARIAN MAHASISWA ===")
# Pencarian tersedia (A003)
print("Cari A003:", cari_mahasiswa(data_mahasiswa, "A003"))
# Pencarian tidak tersedia (A999)
print("Cari A999:", cari_mahasiswa(data_mahasiswa, "A999"))

print("\n=== PENAMBAHAN MAHASISWA BARU ===")
# Menambahkan mahasiswa baru (A006)
data_mahasiswa["A006"] = {"nama": "Fajar", "kelas": "B", "nilai": 90}
print("Berhasil menambahkan A006:", data_mahasiswa["A006"])

print("\n=== PEMBARUAN NILAI MAHASISWA ===")
# Mengubah nilai salah satu mahasiswa (A002 menjadi 82)
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai A002 setelah diperbarui:", data_mahasiswa["A002"])

print("\n=== SELURUH DATA MAHASISWA (REKAP) ===")
# Menampilkan seluruh data menggunakan items()
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Nama: {info['nama']} | Kelas: {info['kelas']} | Nilai: {info['nilai']}")

print("\n=== RATA-RATA NILAI KELAS ===")
# Menghitung dan menampilkan rata-rata nilai seluruh mahasiswa
rata_rata = rata_rata_nilai(data_mahasiswa)
print(f"Rata-rata nilai mahasiswa: {rata_rata:.2f}")