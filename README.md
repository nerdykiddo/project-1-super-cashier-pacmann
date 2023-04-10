# Project Pacmann 1 : Super Cashier
Ini adalah project membuat sistem kasir self-service, di mana customer bisa memasukkan nama, jumlah dan harga barang yang akan dibeli.

# Tujuan Project
1. Agar customer yang berada di kota lain bisa membeli barang dari supermarket tersebut.
2. Membuat fitur-fitur agar proses transaksi di kasir berjalan dengan lancar.
3. Membuat status bila customer salah memasukkan data saat membeli.
4. Membuat proses perhitungan total belanja beserta diskonnya (bila ada).

# Alur Program
1. Masukkan ID Transaksi
2. Masukkan nama barang, jumlah barang dan harga barang.
3. Jalankan tambah_barang bila customer mau tambah barang.
4. Jalankan update_barang bila customer mau update barang.
5. Jalankan hapus_barang bila customer mau menghapus barang.
6. Jalankan reset_transaksi bila customer mau menghapus semua transaksi atau reset order dari awal.
7. Jalankan check_order bila customer sudah selesai dan ingin mengecek order. 
Bila order ada yang salah, akan muncul "Terjadi kesalahan input". 
Bila order benar, akan muncul "Pemesanan sudah benar".
8. Jalankan checkout bila customer mau checkout dan mengetahui dapat diskon atau tidak.
Bila total belanja di atas 200,000 maka mendapat diskon 5%
Bila total belanja di atas 300,000 maka mendapat diskon 8%
Bila total belanja di atas 500,000 maka mendapat diskon 10%

# Hasil Test Case
1. Customer ingin menambahkan 3 barang dengan menggunakan method tambah_barang. 
Barang yang ditambahkan adalah :
    - Nama barang : Klepon, jumlah :1, harga : 5000
    - Nama barang : Ote-Ote, jumlah : 2, harga : 2500
    - Nama barang : Tahu, jumlah : 6, harga : 2000
  - Output :
   ![image](https://user-images.githubusercontent.com/127496480/230802742-61c57b98-de2d-4fa4-af64-b502b172aba8.png)
 
2. Customer ingin tambah barang namun data yang dimasukkan tidak lengkap.
 ![image](https://user-images.githubusercontent.com/127496480/230802916-b9b40e0d-f948-4bef-8a2c-dfba6092ac97.png)
  - Output :
  ![image](https://user-images.githubusercontent.com/127496480/230802931-5fea2b53-f9fe-4bb9-8f7d-940354b687d6.png)

3. Customer ternyata lupa mau beli sushi bukan tahu, maka customer menggunakan method update_barang, mengganti :
    - Nama barang : Tahu, jumlah : 6, harga : 2000, menjadi :
    - Nama barang : Sushi jumlah : 5, harga : 7000
  - Output :
   ![image](https://user-images.githubusercontent.com/127496480/230803298-547bf60c-a899-4593-ba3d-1ae278e3ca2a.png)

4. Customer berubah pikiran dan tidak jadi membeli sushi, maka customer menggunakan method hapus_barang. 
  - Output :
    ![image](https://user-images.githubusercontent.com/127496480/230803485-7fd07df6-9b31-4238-9da1-280b016a73cd.png)

5. Setelah berpikir panjang ternyata customer mau menghapus semua barang dan mengulang order dari awal! Daripada mengetik 
   satu-persatu, customer menggunakan method reset_transaksi untuk menghapus semua barang.
  - Output :
  ![image](https://user-images.githubusercontent.com/127496480/230803720-1fb79d24-32af-41a7-833f-3dbd13d6f0d6.png)

6. Setelah memesan semua barang, customer ingin memastikan total semua belanjaan yang dipesan beserta total harganya.
    Maka customer menggunakan method check_order untuk melihat semua pesanan yang akan dibeli sebelum membayar.
   - Output :
   ![image](https://user-images.githubusercontent.com/127496480/230803846-e1266516-3fa8-40c5-bfc1-9cf6941a4073.png)

7. Setelah sudah yakin dengan pesanannya, maka akhirnya customer ingin membayar. Maka customer menggunakan method 
    checkout() untuk menghitung total belanjaan sekaligus mengetahui apakah customer mendapat diskon atau tidak.
   - Output diskon 10% :
    ![image](https://user-images.githubusercontent.com/127496480/230803947-d15795fb-fd70-49ae-bb1a-db951d1b26af.png)
   
   - Output diskon 8% :
    ![image](https://user-images.githubusercontent.com/127496480/230804130-116d7d4b-9c05-4ff9-9d8c-aca6f45fc930.png)

   - Output diskon 5% :
    ![image](https://user-images.githubusercontent.com/127496480/230804105-b8992341-3012-42e7-9495-57444e6ca0b2.png)
    
   - Output tidak mendapat diskon :
   ![image](https://user-images.githubusercontent.com/127496480/230804163-64266c75-7e20-4d71-be34-6f5bc9f414d8.png)

# Saran Perbaikan
  1. Saat check order dan ada kesalahan input, bisa dijelaskan bagian mana yang salah
  2. di bagian diskon bisa dijelaskan statusnya sudah mencapai angka minimal belanja tertentu sehingga mendapatkan 
      angka diskon tertentu



    
  

