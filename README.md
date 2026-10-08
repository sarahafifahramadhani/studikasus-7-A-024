# studikasus-6-A-024

# SISTEM MANAJEMEN INVENTARIS BARANG

## Penjelasan Program

Program ini digunakan untuk user dapat melihat data barang beserta ketersediaan stoknya dan menambahkan data barang baru.

## Kode yang digunakan pada Program

1. ``Library``, saya menggunakan ``import json`` untuk menyimpan data barang dan stok pada file ``.json``. Data pada file ini akan berubah isinya jika user menambahkan data baru di program.

2. ``if-elif-else``, saya menggunakan percabangan agar user dapat memilih 3 opsi pada menu di program.

3. ``function``, saya menggunkan beberapa function untuk memudahkan progam saya saat ingin melihat ataupun menambah data, dengan cara memanggil fungsi ``lihat_data()`` untuk melihat data dan stok, lalu fungsi ``tambah_brg()`` untuk menambahkan data barang yang terbaru, dan terakhir adalah fungsi ``main()`` untuk menjalankan menu utama pada program yang menampilkan 3 pilihan opsi.

4. ``while loop``, saya menggunakan menu perulangan agar program terus berjalan setiap user memilih opsi 1, 2 ataupun opsi yang tidak ada pada menu. Jika user memilih opsi ketiga, perulangan akan berhenti karna ada ``break`` untuk menghentikan program.

5. ``.append``, saya menggunakan ``.append`` untuk menambahkan data baru pada file ``.json``.

## Output pada Program

### Output 1

<img width="318" height="134" alt="Screenshot 2026-10-07 220613" src="https://github.com/user-attachments/assets/9836e0bb-bb12-42e4-8200-6adcee12c75c" />

Ini adalah output dari fungsi ``main()``.

### Output 2

<img width="325" height="264" alt="Screenshot 2026-10-07 220632" src="https://github.com/user-attachments/assets/6394bf67-ea56-4c28-94b4-9d88db22f300" />

Ini adalah output dari fungsi ``lihat_data()``, jika user memilih opsi pertama, maka program akan menampilkan data barang dan stok yang ada.

### Output 3

<img width="328" height="120" alt="Screenshot 2026-10-07 221134" src="https://github.com/user-attachments/assets/00b8d633-7053-4c8a-8096-d140244ea811" />

Ini adalah output dari fungsi ``tambah_brg()``, ketika user memilih opsi kedua, program akan meminta user untuk mengisi data-data yang diperlukan jika ingin menambah data baru.

### Output 4

<img width="321" height="136" alt="Screenshot 2026-10-07 221205" src="https://github.com/user-attachments/assets/46334704-b94d-4fec-8b4b-fbb2163eeec4" />

Ini adalah output percabangan, jika user menginput angka yang tidak ada pada opsi, maka program akan mengembalikan user pada menu opsi (perulangan).

### Output 5

<img width="327" height="144" alt="Screenshot 2026-10-07 221316" src="https://github.com/user-attachments/assets/cb5ea0c2-aea3-4a53-b664-40d2062e5590" />

Ini adalah output jika user memilih opsi ketiga, program akan menghentikan perulangan karena ada ``break``.

### Output 6

<img width="328" height="304" alt="Screenshot 2026-10-07 230956" src="https://github.com/user-attachments/assets/29d54b20-ad8b-4797-8da4-68d462e7b57b" />

Ini adalah output setelah user menambahkan data barang baru.

## Dokumentasi file .json sebelum ada penambahan data

<img width="496" height="382" alt="Screenshot 2026-10-07 220313" src="https://github.com/user-attachments/assets/2946cafe-01c1-40d3-a686-2163b8802a2a" />

## Dokumentasi file .json setelah ada penambahan data

<img width="460" height="434" alt="Screenshot 2026-10-07 221232" src="https://github.com/user-attachments/assets/fbcbb341-edfb-488b-996e-9cdfc019a493" />
