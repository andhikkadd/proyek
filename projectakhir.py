data_pemasukkan = []
data_pengeluaran = []
saldo = 0 

def tambahkan_data(saldo):
    jenis = input("Tambahkan data [Pengeluaran/Pemasukan]: ").lower()
    
    if jenis == "pemasukan":
        nominal = int(input("Masukkan nominal: "))
        tanggal = input('masukkan tanggal dan bulan (dd-mm-yy): ')
        judul = input("Masukkan judul: ")
        data_pemasukkan.append({'judul': judul, 'nominal': nominal, 'tanggal': tanggal})
        saldo += nominal  
        print("Data Pemasukan Berhasil Ditambahkan")
        
    elif jenis == "pengeluaran":
        nominal = int(input("Masukkan nominal: "))
        if nominal > 100000:
            print('pengeluaran anda sudah mencapai batas!')
        else:
            pass
        tanggal = input('masukkan tanggal dan bulan (dd-mm-yy): ')
        judul = input("Masukkan judul: ")
        kategori = input("Masukkan kategori yang sesuai: ")
        data_pengeluaran.append({'judul': judul, 'nominal': nominal, 'kategori': kategori, 'tanggal': tanggal})
        saldo -= nominal  
        print("Data Pengeluaran Berhasil Ditambahkan")
        
    else:
        print("Pilihan jenis tidak sesuai!")
    
    return saldo

def fitur_menu():
    print("Menu:")
    print("1. Tambah Data")    
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("0. Keluar")

def tampilan():
    totalNominalPemasukkan = 0
    totalNominalPengeluaran = 0
    KetemuData=False
    
    masukkan_bulan = input('masukkan bulan untuk menampilkan data: ')
    
    for data in data_pemasukkan:
        if masukkan_bulan in data['tanggal']:
            KetemuData=True
            totalNominalPemasukkan += data['nominal']
            print(f"Judul: {data['judul']}, Nominal: {data['nominal']}, Tanggal: {data['tanggal']}")
        
    
    for data in data_pengeluaran:
        if masukkan_bulan in data['tanggal']:
            KetemuData=True
            totalNominalPengeluaran += data['nominal']
            print(f"Judul: {data['judul']}, Nominal: {data['nominal']}, Kategori: {data['kategori']}, Tanggal: {data['tanggal']}")
    if not KetemuData:
        print('Data tidak ditemukan')
    else:
    
        print(f"Rekap Data bulan {masukkan_bulan}")     
        print("Total Pemasukkan: ", totalNominalPemasukkan)
        print("Total Pengeluaran: ", totalNominalPengeluaran)
        print("Sisa Saldo: ", saldo)
        
def update_data():
    pass

def hapus(data_pemasukkan, data_pengeluaran):
    print("Hapus Data:")
    print("1. Hapus Pemasukan")
    print("2. Hapus Pengeluaran")
    jenis_hapus = input("Masukkan pilihan: ")
    
    if jenis_hapus == "1":
        judul_hapus = input("Masukkan judul pemasukan yang ingin dihapus: ")
        for data in data_pemasukkan:
            if data['judul'] == judul_hapus:
                data_pemasukkan.remove(data)
                print("Pemasukan berhasil dihapus.")
                break
        else:
            print("Judul pemasukan tidak ditemukan.")
        
    elif jenis_hapus == "2":
        judul_hapus = input("Masukkan judul pengeluaran yang ingin dihapus: ")
        for data in data_pengeluaran:
            if data['judul'] == judul_hapus:
                data_pengeluaran.remove(data)
                print("Pengeluaran berhasil dihapus.")
                break
        else:
            print("Judul pengeluaran tidak ditemukan.")
        
    else:
        print("Pilihan tidak valid.")
        
while True:
    fitur_menu()
    pilihan = input("Masukkan pilihan anda: ")
    
    if pilihan == "1":
        tambahkan_data(saldo)
        
    elif pilihan == "2":
        tampilan()

    elif pilihan == "3":
        pass  
    
    elif pilihan == "4":
        hapus(data_pemasukkan, data_pengeluaran)

    elif pilihan == "0":
        print("Terima kasih telah menggunakan program ini.")
        break
    
    else:
        print("Input tidak sesuai, silahkan masukkan ulang..")