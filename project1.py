
""" Module 'project-1-super-cashier-pacmann' berfungsi untuk membuat input data belanjaan.
Function tambah_barang() berfungsi untuk menambah nama barang, harga barang dan jumlah barang.
Function update_barang() berfungsi untuk update nama barang, harga barang dan jumlah barang.
Function hapus_barang() berfungsi untuk menghapus nama barang.
Function reset_transaksi() berfungsi untuk menghapus semua transaksi atau reset order dari awal.
Function check_order() berfungsi untuk mengecek order dengan total harga.
Function checkout() berfungsi untuk checkout danmengetahui dapat diskon atau tidak.

Data di ID transaksi01 sebagai contoh data awal yang sudah tersimpan dalam database.

"""

# Import library yang akan digunakan 
from tabulate import tabulate

# membuat class transaksi
class Transaksi():
    def __init__(self):
        self.nama_barang = list()
        self.harga_barang = list()
        self.jumlah_barang = list()

# bila customer mau tambah barang
    def tambah_barang(self, nama, harga, jumlah):
        self.nama_barang.append(nama)
        self.harga_barang.append(harga)
        self.jumlah_barang.append(jumlah)

# bila customer mau update barang       
    def update_barang(self, index, nama=None, harga=None, jumlah=None):
        if nama is not None:
            self.nama_barang[index] = nama
        if harga is not None:
            self.harga_barang[index] = harga
        if jumlah is not None:
            self.jumlah_barang[index] = jumlah
        return "Barang berhasil diupdate"

# bila customer mau menghapus barang
    def hapus_barang(self, index):
        try:
            self.nama_barang.pop(index)
            self.harga_barang.pop(index)
            self.jumlah_barang.pop(index)
            print("Barang berhasil dihapus.")
        except IndexError:
            print("Terjadi kesalahan. Barang tidak dapat dihapus.")

#bila customer mau menghapus semua transaksi atau reset order dari awal
    def reset_transaksi(self):
        self.nama_barang.clear()
        self.harga_barang.clear()
        self.jumlah_barang.clear()
        print("Semua barang berhasil dihapus!")

#bila customer mau mengecek order
    def check_order(self):
        data = []
        for i in range(len(self.nama_barang)):
            if self.nama_barang[i] is None or self.jumlah_barang[i] is None or self.harga_barang[i] is None:
                print("Terjadi kesalahan input")
                return
            data.append([i+1, self.nama_barang[i], self.jumlah_barang[i], self.harga_barang[i], self.harga_barang[i]*self.jumlah_barang[i]])
        print(tabulate(data, headers=["No.", "Nama Barang", "Jumlah", "Harga", "Total Harga"], tablefmt="fancy_grid"))
        print("Pemesanan sudah benar")

#bila customer mau checkout dan dapat diskon atau tidak
    def checkout(self):
        total_harga = 0 
        for i in range(len(self.nama_barang)):
            total_harga += self.harga_barang[i]*self.jumlah_barang[i]
        
        if total_harga >= 500_000:
            total_harga *= 0.90
            print('Muantab dapet diskon 10% !')
        elif total_harga >= 300_000:
            total_harga *= 0.92
            print('Asik dapet diskon 8% !')
        elif total_harga >= 200_000:
            total_harga *= 0.95
            print('Hore dapet diskon 5% !')
        else:
            print('Waaa ngga dapet diskon hiks... T_T')
        print('Total Harga =', total_harga)


""" Fungsi di bawah merupakan contoh. 
    transaksi01 adalah contoh ID transaksi
    Klepon, Ote-Ote, Tahu, Playstation adalah contoh saat menggunakan fungsi tambah_barang()
    (2, 'Sushi', 7000, 5) adalah contoh menggunakan fungsi update_barang(), 
    dengan cara membaca index kedua, nama barang, harga barang dan jumlah barang yang di-update
    transaksi01.hapus_barang(2) adalah contoh menghapus barang index ke-2
    transaksi01.reset_transaksi() adalah contoh menghapus semua transaksi dan memulai dari awal
    transaksi01.check_order() adalah contoh mengecek order
    transaksi01.checkout() adalah contoh checkout order beserta diskonnya (bila ada)
    
    """
# buat objek berdasarkan class
#transaksi01 = Transaksi()
#transaksi01.tambah_barang('Klepon', 500000, 1)
#transaksi01.tambah_barang('Ote-Ote', 2500, 2)
#transaksi01.tambah_barang('Tahu', 2000, 6)
#transaksi01.tambah_barang('PlayStation', 1000000, 5)

#transaksi01.tambah_barang("Pensil", 3000, None)

#transaksi01.update_barang(2, 'Sushi', 7000, 5)

#transaksi01.hapus_barang(2)

#transaksi01.reset_transaksi()

#transaksi01.check_order()
#transaksi01.checkout()



