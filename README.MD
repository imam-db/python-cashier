### Project Python Pacmann


#### Latar belakang masalah




#### Requirements / objectives



#### Flowchart


!['Flowchart app'](./images/python_cashier_project.drawio.png)

Program kasir self-service ini dimulai dari tampilnya menu, dengan total ada 7 menu seperti gambar di bawah ini:

!['Menu Awal'](./images/1.PNG)

Untuk menambahkan item belanja, customer bisa memilih menu nomer 1.  
Sebelum memilih menu dalam pilihan angka yang benar, terlebih dahulu masukkan pilihan diluar menu. Sebagai contoh memasukkan nomor 8 atau non angka. Hasilnya muncul error dengan keterangan "Invalid selection. Try again later." seperti dua gambar di bawah ini.

!['Salah Pilih Menu'](./images/2.PNG)  
!['Salah Pilih Menu'](./images/3.PNG)

Percobaan berikutnya memilih menu sesuai dengan pilihan menu.  
Untuk setiap transaksi, bisa menambahkan item-item ke dalamnya dengan memilih menu 1. Setelah itu customer dapat memasukkan data produk, yaitu nama produk, total quantity dan harga tiap pcs-nya. Setelah memasukkan ketiga data tersebut, data produk berhasil disimpan. Kemudian muncul pilihan kembali apakah akan menambahkan item yang lain?jika iya masukkan "y" atau "n" jika ingin mengakhiri inputan item.

!['Menu 1'](./images/4.PNG)

Setelah memilih "y" / menambahkan item yang lain, customer menginputkan kembali data-data produk seperti langkah-langkah sebelumnya.

!['Menu 1-Tambah Items Lain'](./images/5.PNG)

Lanjut ke menu ke 2 (View items). Customer bisa melihat item-item yang sudah ditambahkan sebelumnya, dengan detail yang ditampilkan yaitu nama produk, quantity dan total harga per produk.

!['Menu 2'](./images/6.PNG)

Menu berikutnya, loncat dulu ke menu 4 (Update Items). Menu ini akan berguna bagi customer ketika ingin mengubah item yang sebelumnya sudah dimasukkan ke program. Seperti terlihat pada gambar, setelah memilih menu 4, langsung dihadapkan pilihan kembali berupa produk-produk yang sebelumnya sudah diinput. Customer tinggal mengisi angka sesuai produk yang ingin diubah. 

!['Menu 4 - List Produk'](./images/7.PNG)

Sebagai contoh, customer ingin mengubah item no. 3 (Semangka). Customer tinggal mengetik angka 3. Dan setelahnya muncul pilihan lagi apakah akan mengubah (1) nama produk, (2) quantity atau (3) harga per itemnya. Dan juga ada pilihan untuk (4) cancel jika dirasa salah memilih produk yang akan diubah, sehingga otomatis akan kembali ke menu sebelumnya.

!['Menu 4 - Produk terpilih - Action Update'](./images/8.PNG)

Pilih menu 1 untuk mengubah nama produk. Sebagai contoh, customer ternyata salah menginput nama produk `semangka` dan mengubahnya menjadi `Semangka Merah`.

!['Menu 4 - Produk terpilih - Update Nama'](./images/9.PNG)

Pilihan menu 2 untuk mengubah quantity dari produk. Sebagai contoh, customer mengubah quantity dari `2` menjadi `12`.

!['Menu 4 - Produk terpilih - Update Quantity'](./images/10.PNG)

Pilihan menu 3 untuk mengubah harga per item dari produk. Sebagai contoh, customer mengubahnya dari `50000` menjadi `55000`.

!['Menu 4 - Produk terpilih - Update Quantity'](./images/11.PNG)

