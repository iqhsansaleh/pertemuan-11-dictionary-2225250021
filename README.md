# Pertemuan 11 - Dictionary/Map

Nama: Iqhsan Saleh 

NIM: 2225250021

Kelas: 3A

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data

- **Key utama:** NIM mahasiswa bertipe string, misalnya `"A001"` dan `"A002"`, yang berfungsi sebagai pengenal unik.
- **Value:** Nested dictionary yang berisi:
	- `"nama"` (string): nama mahasiswa.
	- `"kelas"` (string): kelas mahasiswa.
	- `"nilai"` (integer): nilai hasil belajar mahasiswa.

## Cara Menjalankan

```bash
python3 praktik/data_mahasiswa.py
```

## Test Case

| No. | Input / Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
| --- | --- | --- | --- | --- |
| 1 | Cari NIM `A003` | Data Citra ditampilkan | `{'nama': 'Citra', 'kelas': 'B', 'nilai': 92}` | Lulus |
| 2 | Cari NIM `A999` yang tidak terdaftar | Pesan `Data tidak ditemukan` | `Data tidak ditemukan` | Lulus |
| 3 | Perbarui nilai `A002` menjadi `82` | Nilai A002 berubah menjadi 82 | `{'nama': 'Budi', 'kelas': 'A', 'nilai': 82}` | Lulus |
| 4 | Tambahkan data `A006` | Data A006 tersimpan | `{'nama': 'Fajar', 'kelas': 'B', 'nilai': 90}` | Lulus |
| 5 | Rekap data menggunakan `items()` | Seluruh data mahasiswa ditampilkan | Enam data mahasiswa tampil dengan NIM, nama, kelas, dan nilai | Lulus |

## Refleksi

Kesalahan akses key yang dapat terjadi adalah mengambil key yang tidak terdaftar dengan tanda kurung siku, misalnya `data["A999"]`. Cara ini memicu `KeyError`. Untuk pencarian yang aman, gunakan `.get()`, misalnya `data.get("A999", "Data tidak ditemukan")`, agar nilai pengganti ditampilkan tanpa menghentikan program.
