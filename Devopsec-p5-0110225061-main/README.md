# Devopsec-p5-0110225061
# Secure Student Task Manager

## 1. Deskripsi Aplikasi

Secure Student Task Manager adalah aplikasi sederhana berbasis Python yang digunakan untuk membantu mahasiswa mengelola daftar tugas. Pengguna dapat menambahkan tugas baru, melihat daftar tugas, dan menandai tugas yang telah selesai.

Aplikasi ini dibuat sebagai proyek pembelajaran untuk menerapkan konsep DevSecOps dalam proses pengembangan perangkat lunak.

## 2. Bahasa Pemrograman dan Tools

Proyek ini menggunakan beberapa teknologi berikut:

- **Python 3.12** sebagai bahasa pemrograman.
- **unittest** untuk menjalankan pengujian otomatis.
- **GitHub Actions** untuk mengotomatisasi proses build dan pengujian.
- **Bandit** sebagai tools Static Application Security Testing (SAST) untuk mendeteksi pola kode Python yang berpotensi tidak aman.

## 3. Cara Menjalankan Aplikasi

Pastikan Python telah terpasang pada komputer. Buka terminal di folder proyek, kemudian jalankan perintah berikut:

```bash
python main.py
```

Setelah aplikasi berjalan, pengguna dapat memilih menu untuk menambahkan tugas, melihat daftar tugas, menandai tugas selesai, atau keluar dari aplikasi.

Data tugas disimpan sementara di memori dan akan hilang ketika aplikasi ditutup.

## 4. Cara Menjalankan Pengujian

Pengujian otomatis dapat dijalankan melalui terminal dengan perintah:

```bash
python -m unittest discover -s test -v
```

Untuk memasang Bandit dan menjalankan pemindaian keamanan secara lokal, gunakan:

```bash
python -m pip install -r requirement.txt
bandit -r app main.py
```

## 5. Implementasi Pipeline DevSecOps

Pipeline DevSecOps diimplementasikan menggunakan GitHub Actions dan disimpan pada file `.github/workflows/devsecops.yml`.

Workflow dijalankan secara otomatis ketika terdapat perubahan kode melalui `push` ke branch `main` atau ketika terdapat `pull_request` yang menargetkan branch `main`.

Pipeline terdiri dari dua job utama:

1. **Build** — memasang dependensi yang diperlukan dan menjalankan unit test untuk memeriksa fungsi aplikasi.
2. **SAST Scan** — menjalankan Bandit untuk memindai kode sumber Python dan menerapkan Quality Gate berdasarkan tingkat keparahan serta confidence temuan keamanan.

Job SAST Scan bergantung pada job Build. Dengan demikian, pemindaian keamanan baru dijalankan setelah job Build berhasil.

## 6. Quality Gate

Quality Gate digunakan untuk menentukan apakah hasil pemindaian keamanan memenuhi kriteria yang telah ditetapkan. Pada proyek ini, pipeline akan gagal apabila Bandit menemukan masalah dengan tingkat keparahan tinggi (*HIGH severity*) dan tingkat keyakinan sedang atau tinggi (*MEDIUM atau HIGH confidence*).

Hasil pemindaian juga disimpan sebagai laporan JSON yang dapat diperiksa melalui artifact pada GitHub Actions.

Penerapan pipeline ini diharapkan dapat membantu menemukan potensi masalah keamanan lebih awal dan meningkatkan kualitas kode selama proses pengembangan aplikasi.
