data_pemasukkan = []
data_pengeluaran = []
saldo = 0 

def tambahkan_data(saldo):
    jenis = input("Tambahkan data [Pengeluaran/Pemasukan]: ").lower()
    
    if jenis == "pemasukan":
        judul = input("Masukkan judul: ")
        nominal = int(input("Masukkan nominal: "))
        tanggal = input('masukkan tanggal dan bulan (dd-mm-yy): ')
        data_pemasukkan.append({'judul': judul, 'nominal': nominal, 'tanggal': tanggal})
        saldo += nominal  
        print("Data Pemasukan Berhasil Ditambahkan")
        
    elif jenis == "pengeluaran":
        judul = input("Masukkan judul: ")
        nominal = int(input("Masukkan nominal: "))
        kategori = input("Masukkan kategori yang sesuai: ")
        tanggal = input('masukkan tanggal dan bulan (dd-mm-yy): ')
        data_pengeluaran.append({'judul': judul, 'nominal': nominal, 'kategori': kategori, 'tanggal': tanggal})
        saldo -= nominal  
        print("Data Pengeluaran Berhasil Ditambahkan")
        
    else:
        print("Pilihan jenis tidak sesuai!")
    
    return saldo

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
        print("")
        print("")
        print(f"Rekap Data bulan {masukkan_bulan}")     
        print("Total Pemasukkan: ", totalNominalPemasukkan)
        print("Total Pengeluaran: ", totalNominalPengeluaran)
        print("Sisa Saldo: ", saldo)
        
def update_data(data_pemasukkan, data_pengeluaran):
    print("Update Data")
    print("1. Data Pemasukkan")
    print("1. Data Pengeluaran")
    jenisUpdate = input("Masukkan pilihan data yang ingin di update: ")
    
    if jenisUpdate == "1":
        updateJudul = input("Masukkan judul data yang ingin di update: ")
        for data in data_pemasukkan:
            if data['judul'] == updateJudul:
                nominal = input("Masukkan nominal: ")
                tanggal = input("Masukkan tanggal: ")
                data['nominal'] = nominal
                data['tanggal'] = tanggal
                print("Data pemasukkan telah diupdate")
        else:
            print("Data tidak ditemukan")
                
    if jenisUpdate == "2":
        updateJudul = input("Masukkan judul data yang ingin diupdate: ")
        for data in data_pengeluaran:
            if data['judul'] == updateJudul:  
                nominal = input("Masukkan nominal: ")
                tanggal = input("Masukkan tanggal: ")
                kategori = input("Masukkan kategori: ")
                data['nominal'] = nominal
                data['tanggal'] = tanggal
                data['kategori'] = kategori
                print("Data Pengeluaran telah diupdate")
        else:
            print("Data tidak ditemukan")
                      
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
    print("Menu:")
    print("1. Tambah Data")    
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("0. Keluar")
    pilihan = input("Masukkan pilihan anda: ")
    
    if pilihan == "1":
        tambahkan_data(saldo)
        
    elif pilihan == "2":
        tampilan()

    elif pilihan == "3":
        update_data(data_pemasukkan, data_pengeluaran)  
    
    elif pilihan == "4":
        hapus(data_pemasukkan, data_pengeluaran)

    elif pilihan == "0":
        print("Terima kasih telah menggunakan program ini.")
        break
    
    else:
        print("Input tidak sesuai, silahkan masukkan ulang..")