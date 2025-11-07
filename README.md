# 🔐 Hill Cipher 2x2 (Python)

Program ini merupakan implementasi **Hill Cipher 2x2** menggunakan bahasa Python.  
Hill Cipher adalah salah satu algoritma **kriptografi klasik berbasis matriks**, yang melakukan enkripsi dan dekripsi menggunakan operasi aljabar linear (mod 26).

---

## 📘 Fitur

- Enkripsi teks menggunakan **matriks kunci 2x2**
- Dekripsi ciphertext menggunakan **invers matriks modulo 26**
- Validasi determinan agar memiliki **invers modulo**
- Mendukung **padding otomatis** (huruf `X` bila panjang teks ganjil)
- Input kunci dan teks langsung dari user

---

## 🧮 Cara Kerja Singkat

1. Setiap huruf (A–Z) dikonversi menjadi angka (A=0, ..., Z=25).
2. Plaintext dibagi menjadi blok berukuran 2 huruf.
3. Setiap blok dikalikan dengan matriks kunci `K`, hasilnya diambil modulo 26 → menghasilkan ciphertext.
4. Untuk dekripsi, digunakan **invers dari matriks kunci (mod 26)**.

---

## ⚙️ Cara Menjalankan

Pastikan Python dan NumPy sudah terpasang.

### 1️⃣ Install NumPy

```bash
pip install numpy
```

### 2️⃣ Jalankan Program

```bash
python kriptografi.py
```

Kemudian masukkan:
- Plaintext (hanya huruf A–Z)
- Nilai matriks kunci 2x2 (angka 0–25)

---

## 🧩 Contoh Penggunaan

```
=== Program Hill Cipher 2x2 ===
Masukkan plaintext (A-Z): HELLO

Masukkan matriks kunci 2x2 (hanya angka 0-25):
K[0,0]: 3
K[0,1]: 3
K[1,0]: 2
K[1,1]: 5

=== HASIL ===
Plaintext : HELLO
Ciphertext: HIOZHN
Invers matriks K (mod 26):
 [[15. 17.]
  [20.  9.]]
Dekripsi  : HELLOX
===============
```

---

## 🧠 Catatan Penting

- Determinan matriks kunci harus memiliki invers modulo 26 agar dekripsi bisa dilakukan. Jika tidak, program akan menampilkan pesan error.
- Huruf kecil dan spasi otomatis diabaikan/dikonversi ke huruf besar.

---

## 📂 Struktur File

```
kriptografi.py
README.md
```

---


## 🧾 Lisensi

Proyek ini bersifat open-source dan bebas digunakan untuk keperluan edukasi.

---