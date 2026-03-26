# 📦 Big Integer ADT (Single File Implementation)

## 📌 Deskripsi

Project ini merupakan implementasi **Big Integer Abstract Data Type (ADT)** menggunakan Python dalam **satu file (`big_integer.py`)**.
Tujuan dari project ini adalah untuk merepresentasikan bilangan integer dengan ukuran sangat besar yang tidak terbatas oleh kapasitas hardware.

Implementasi ini dibuat berdasarkan tugas praktikum, di mana setiap digit bilangan disimpan secara terpisah menggunakan:

* **Singly Linked List**
* **Python List**

---

## ✨ Fitur

✔ Menyimpan bilangan dengan digit tak terbatas
✔ Dua pendekatan implementasi:

* Linked List
* Python List

✔ Operasi yang tersedia:

* Penjumlahan (`+`)
* Perbandingan sederhana
* Operator assignment (`+=`)
* Operasi tambahan:

  * Pengurangan (`-`)
  * Perkalian (`*`)
  * Pembagian (`//`)
  * Modulus (`%`)
  * Pangkat (`**`)

---

## 📂 Struktur Project

```
big_integer.py   # Semua implementasi dalam satu file
README.md        # Dokumentasi project
```

---

## 🧠 Konsep Dasar

Pada implementasi ini:

* Setiap digit angka disimpan secara terpisah
* Urutan penyimpanan dimulai dari digit terkecil ke terbesar (Linked List)
* Tidak bergantung pada tipe data integer bawaan Python

Contoh:

```
12345 → disimpan sebagai:
5 → 4 → 3 → 2 → 1
```

---

## 🚀 Cara Menjalankan

1. Pastikan Python sudah terinstall
2. Jalankan file:

```bash
python big_integer.py
```

---

## 🧪 Contoh Output

```
=== LINKED LIST ===
12345 + 6789 = 19134

=== LIST ===
99999 + 1 = 100000

=== OPERATOR TAMBAHAN ===
Pengurangan: 750
Perkalian: 5535
Pembagian: 20
Modulus: 1
Pangkat: 1024
```

---

## 📖 Penjelasan Singkat

* **BigIntegerLinkedList** → Menyimpan digit menggunakan node
* **BigIntegerList** → Menyimpan digit menggunakan list Python
* Operasi aritmatika dilakukan dengan meniru cara perhitungan manual

---

## 🎯 Tujuan Pembelajaran

* Memahami struktur data Linked List
* Mengimplementasikan ADT (Abstract Data Type)
* Mensimulasikan operasi bilangan besar
* Memahami keterbatasan integer pada level hardware

---

## 👨‍💻 Author

Nama: Farhan Bagas Firmansyah
Kelas: 2025B

---

## 📌 Catatan

Project ini dibuat untuk keperluan pembelajaran dan praktikum struktur data.
