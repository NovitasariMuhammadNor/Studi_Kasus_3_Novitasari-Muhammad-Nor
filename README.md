# Studi_Kasus_3_Novitasari-Muhammad-Nor
Nama : Novitasari Muhammad Nor  
Nim : 2609116082

Berikut Penjelasannya

- batas_nilai menentukan batas lulus (65) dan nilai maksimum (100).  
- nilai_masuk menyimpan semua nilai yang diinput.  
- lulus menyimpan nilai ≥ 65.  
- remedial menyimpan nilai < 65.

<img width="313" height="59" alt="image" src="https://github.com/user-attachments/assets/44c312c5-9d03-4091-ab3b-6db42919ac1d" />

- Program terus meminta input nilai sampai kamu mengetik "selesai".
- Setiap nilai yang dimasukkan akan dicek apakah valid (antara 65–100).

<img width="563" height="120" alt="image" src="https://github.com/user-attachments/assets/c1e554d6-07eb-4ade-8635-42f77db33939" />

- Program mencoba (try) mengubah input jadi angka (int(data)), supaya bisa dibandingkan.  
- Kalau nilainya di luar 65–100, muncul pesan “Nilai harus antara 65–100” dan program lanjut ke input berikutnya tanpa menyimpan nilai itu.  
- Nilai yang valid langsung dimasukkan ke daftar nilai_masuk.  
- Kemudian dicek: kalau nilainya ≥ 65, masuk ke daftar lulus; kalau di bawah 65, masuk ke daftar remedial.  
- Kalau input bukan angka (misalnya huruf atau kosong), bagian except ValueError akan menangkap error dan menampilkan pesan “Input tidak valid. Masukkan angka atau 'selesai'.”

<img width="448" height="131" alt="image" src="https://github.com/user-attachments/assets/e599e7b0-be57-4c45-bef4-27ce6ed84352" />

- setelah semua nilai dimasukkan dan dikelompokkan (lulus atau remedial), program memberi kesempatan untuk menghapus satu nilai. Kalau kamu jawab “ya”, lalu ketik angka yang ingin dihapus, program akan mencari angka itu di daftar. Kalau ketemu, nilai tersebut dihapus dari semua kategori (nilai masuk, lulus, remedial) dan muncul pesan konfirmasi. Kalau tidak ketemu, muncul pesan bahwa nilai tidak ada. Kalau salah ketik (misalnya huruf), program akan menampilkan pesan input tidak valid.

<img width="613" height="173" alt="image" src="https://github.com/user-attachments/assets/22ac0a93-5dc1-4763-9930-f71918831f1c" />

- Baris pertama mencetak judul hasil akhir supaya tampilannya lebih jelas dan menarik.  
- Baris kedua menampilkan semua nilai yang masuk (semua nilai yang kamu input sebelum dihapus).  
- Baris ketiga menampilkan nilai lulus, yaitu nilai ≥ 65.  
- Baris keempat menampilkan nilai remedial, yaitu nilai < 65.  
- Baris terakhir menampilkan nilai yang dihapus, kalau kamu sempat menghapus satu nilai sebelumnya.

<img width="503" height="58" alt="image" src="https://github.com/user-attachments/assets/5ef91c4a-2365-4d09-80df-9529324ceaf0" />


- Di awal, program meminta kamu memasukkan nilai ujian mahasiswa satu per satu (80, 55, 90, 60, 70).  
- Setelah kamu mengetik selesai, program lanjut ke bagian penghapusan nilai. Kamu jawab ya, lalu masukkan nilai 55.  
- Program menemukan nilai itu di daftar dan menghapusnya dari semua kategori (nilai_masuk, lulus, remedial).  
- Setelah itu, muncul hasil akhir: Nilai yang masuk: [80, 90, 60, 70] → semua nilai setelah penghapusan.  
- Nilai lulus: [80, 90, 70] → nilai ≥ 65.  
- Nilai remedial: [60] → nilai < 65.  
- Nilai hapus: 55 → nilai yang kamu pilih untuk dihapus.

<img width="742" height="183" alt="image" src="https://github.com/user-attachments/assets/8b3e1081-a862-4905-b070-8e0af5e960d5" />


- ini gambar keseluruhan kode
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/3799bbea-bc63-4667-b7c7-7e48c76f41c9" />
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/e9e2ca80-29c1-4195-a827-c51498d3e759" />

