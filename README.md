# pertemuan-03-seleksi-2225250002

## Identitas
* **Nama**: Nasywaa Zaafarani Kurniawan
* **NIM**: 2225250002
* **Kelas**: 3A

---

## Tujuan Repositori
Repositori ini dibuat untuk memenuhi tugas praktikum Pertemuan 3 mata kuliah Algoritma dan Pemrograman. Repositori ini berisi latihan penggunaan struktur kontrol keputusan (seleksi) pada Python, seperti cabang `if`, `if-else`, kondisi majemuk (`if-elif-else`), dan `nested if` untuk menyelesaikan berbagai kasus evaluasi bilangan, perbandingan, nilai batas kelulusan, penentuan jenis segitiga, serta perhitungan matematis berbasis diskriminan.

---

## Daftar dan Fungsi Berkas

### Folder `latihan/`
* **`01_genap_ganjil.py`**: Memeriksa apakah suatu bilangan bulat merupakan bilangan genap atau ganjil menggunakan operator modulus (`%`).
* **`02_bandingkan_dua_bilangan.py`**: Membandingkan dua nilai masukan untuk menentukan bilangan mana yang lebih besar, lebih kecil, atau apakah keduanya bernilai sama.
* **`03_kelulusan_bersyarat.py`**: Menilai status kelulusan berdasarkan input nilai dengan pengujian nilai batas (*boundary test*) menggunakan operator perbandingan `>=`.
* **`04_jenis_segitiga.py`**: Mengidentifikasi jenis segitiga (sama sisi, sama kaki, atau sembarang) berdasarkan panjang ketiga sisinya menggunakan pengujian kondisi majemuk.

### Folder `tugas/`
* **`analisis_persamaan_kuadrat.py`**: Program utama untuk menerima koefisien a, b, dan c dari persamaan ax² + bx + c = 0, mengecek keabsahan persamaan kuadrat (a ≠ 0), menghitung diskriminan (D = b² - 4ac), serta menentukan jenis dan nilai akar real (x1, x2) menggunakan `nested if`.

---

## Hasil Pengujian Tugas Utama (`analisis_persamaan_kuadrat.py`)

| a | b | c | D | Hasil yang Diharapkan | Status |
| :-: | :-: | :-: | :-: | :--- | :-: |
| 1 | -5 | 6 | 1 | Dua akar real: 3 dan 2 | Sesuai |
| 1 | 2 | 1 | 0 | Akar kembar: -1 | Sesuai |
| 1 | 0 | 1 | -4 | Tidak ada akar real | Sesuai |
| 0 | 2 | 3 | - | Bukan persamaan kuadrat | Sesuai |
---

## Cara Menjalankan

Buka terminal di direktori utama repositori ini, lalu jalankan program menggunakan perintah berikut:

```bash
python tugas/analisis_persamaan_kuadrat.py
python latihan/01_genap_ganjil.py
python latihan/02_bandingkan_dua_bilangan.py
python latihan/03_kelulusan_bersyarat.py
python latihan/04_jenis_segitiga.py
```

### Refleksi
Dalam praktikum Pertemuan 3 ini, saya mempelajari penggunaan operator perbandingan (==, !=, >, >=, <, <=), operator aritmatika modulus, serta pentingnya ketelitian dalam penulisan operator pada struktur keputusan.

Hal yang paling mudah saya pahami adalah perbedaan penggunaan tanda penugasan = (untuk menyimpan nilai ke variabel) dan tanda perbandingan == (untuk menguji kesamaan). Selain itu, saya juga memahami pentingnya pengujian nilai batas (boundary testing). Misalnya, pada penentuan kelulusan bersyarat, operator yang tepat untuk syarat "minimal 60" adalah >= (bukan >), yang perlu diuji menggunakan sampel tepat di bawah batas, tepat pada batas, dan di atas batas.

Kendala yang sempat saya hadapi adalah lupa menambahkan tanda kurung pada pembagi saat menghitung rumus akar (-b ± √D) / (2a), yang menyebabkan kesalahan logika matematis karena 2a tidak terbagi secara utuh. Masalah ini berhasil diselesaikan setelah menambahkan kurung (2 * a). Ketika menemukan kendala, saya dibantu oleh AI Gemini untuk mengonfirmasi logika dan penulisan sintaksnya.

### Sumber yang Digunakan
1. Modul Praktikum Algoritma dan Pemrograman Pertemuan 03.
2. Channel YouTube Himadiktika Uninus.
3. Bantuan Asisten AI Gemini (untuk penjelasan konsep, solusi kendala kode, dan bantuan penulisan dokumen).
