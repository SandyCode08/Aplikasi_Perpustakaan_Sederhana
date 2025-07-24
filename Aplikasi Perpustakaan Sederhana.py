
#Membuat Fungsi Untuk Bikin Tabel
from tabulate import tabulate

###ini Dictionarynya
perpustakaanMelati = {
    'id' : [0,1,2,3],
    'buku' : ['laskar pelangi', 'perahu kertas', 'supernova', 'negeri 5 menara'],
    'genre' : ['drama','romance','sastra','drama'],
    'penulis' : ['andrea hirata', 'dee lestari', 'dee lestari', 'ahmad fuadi'],
    'stok' : [5,3,1,6]
}

### fungsi untuk membuat tabel
def tabelPerpus(perpustakaanMelati): 
  headers = ['id','buku','genre','penulis','stok']

  tampung = []
  for i in range(len(perpustakaanMelati['id'])):
    row = [
      perpustakaanMelati['id'][i],
      perpustakaanMelati['buku'][i],
      perpustakaanMelati['genre'][i],
      perpustakaanMelati['penulis'][i],
      perpustakaanMelati['stok'][i]  
    ]

    tampung.append(row)

  print(tabulate(tampung, headers=headers,tablefmt='grid'))

### tabel pinjam buku
def tabelPinjamBuku(keranjangBuku):
  headers = ['Buku','Jumlah Peminjaman','Nama Peminjam']
  wadah = []
  for i in range(len(keranjangBuku)):
    baris = [
      keranjangBuku[i],
      keranjangPinjam[i],
      namaPeminjam[i]
    ]
    wadah.append(baris)
  print(tabulate(wadah, headers=headers, tablefmt='grid'))


### Fungsi 1 List Menu
def listMenu(perpustakaanMelati):
  while True:
    try: # input menu
      print('\n'+'--LIST BUKU PERPUSTAKAAN MELATI--')
      print('\n'+'='*40)
      print('1.Tampilkan List Buku')
      print('2.Filter List Buku')
      print('3.Kembali Ke Menu Utama')
      print('='*40 + '\n' )
      menuList = int(input('Silahkan Pilih Opsi Menu Yang Tersedia:'))
     

      if menuList == 1: # tampilkan List Buku
        if tabelPerpus(perpustakaanMelati):
          print('\nBerikut Merupakan List Buku Perpustakaan Melati yang Tersedia:')
          tabelPerpus(perpustakaanMelati)
        else:
          print('\nJika Ada Judul Buku yang Mau dicari silahkan masukan "judul bukunya"')
          print('Jika Tidak Ada yang Mau dicari cukup masukan "tidak"\n')
          while True:
            tanyaBuku = str(input('Silahkan Masukan (Judul Buku/tidak):')).lower().strip()
            if tanyaBuku in perpustakaanMelati['buku']:
              indexBuku = perpustakaanMelati['buku'].index(tanyaBuku)
              print(f'\nSilahkan Buku "{tanyaBuku}" Tersedia dan Ada di Id "{indexBuku}"')
              break
            elif tanyaBuku == 'tidak':
              break
            elif tanyaBuku.isdigit():
              print('\nSilahkan Masukan Huruf Bukan Angka')
              continue
            else:
              print(f'\nMohon Maaf Saat Ini Buku "{tanyaBuku}" Belum Tersedia di Perpustakaan Kami')
              print('Silahkan Pilih Menu 1.Tampilkan List Buku Untuk Menampilkan Buku yang Tersedia')
              break
 
 
      elif menuList == 2: #### filter BUKU
        tabelPerpus(perpustakaanMelati)
        while True:
          print("\nSilahkan Masukan Filter Buku Berdasarkan 'Genre' dan 'Penulis' yang Ada Pada List Buku,")
          print('atau Bisa Mengisi Salah Satunya dengan Menginput Kosong Salah Satunya\n')
          
          indexGenreKosong = []
          indexPenulisKosong = []

          masukanGenre = str(input('Masukan Genre Buku Yang Mau Di Cari: ')).strip().lower()
          
          if masukanGenre == '':
            break
          elif masukanGenre in perpustakaanMelati['genre']:
            for i in range(len(perpustakaanMelati['genre'])):
              if perpustakaanMelati['genre'][i] == masukanGenre:
                indexGenreKosong.append(i)
            break
          elif masukanGenre.isdigit():
            print('Silahkan Masukan Huruf Bukan Angka')
            continue
          else:
            print(f'Mohon Maaf Untuk Genre "{masukanGenre}" Belum Tersedia Saat Ini')
            break

        if not indexGenreKosong and masukanGenre != '':
          continue

        while True:
          masukanPenulis = str(input('Masukan Penulis Buku Yang Mau Di Cari: ')).strip().lower()
          
          if masukanPenulis == '':
            break
          elif masukanPenulis in perpustakaanMelati['penulis']:
            for i in range(len(perpustakaanMelati['penulis'])):
              if perpustakaanMelati['penulis'][i] == masukanPenulis:
                indexPenulisKosong.append(i)
            break
          elif masukanPenulis.isdigit():
            print('Silahkan Masukan Huruf Bukan Angka')
            continue
          else:
            print(f'Mohon Maaf Untuk Penulis "{masukanPenulis}" Tidak Ditemukan Dalam List')
            break

        if not indexPenulisKosong and masukanPenulis != '':
          continue

        set_genre = set(indexGenreKosong)
        set_penulis = set(indexPenulisKosong)

        if masukanGenre != '' and masukanPenulis != '':
          hasil_set = set_genre & set_penulis
        elif masukanGenre != '':
          hasil_set = set_genre
        elif masukanPenulis != '':
          hasil_set = set_penulis
        else:
          hasil_set = set(range(len(perpustakaanMelati['id'])))

        if hasil_set:
          headersBuku = ['id','buku','genre','penulis','stok']
          listBuku = []
          for i in hasil_set:
            rowBuku = [
              perpustakaanMelati['id'][i],
              perpustakaanMelati['buku'][i],
              perpustakaanMelati['genre'][i],
              perpustakaanMelati['penulis'][i],
              perpustakaanMelati['stok'][i]
            ]
            
            listBuku.append(rowBuku)
  
          print('\nBerikut Merupakan Hasil Filter Buku:')
          print(tabulate(listBuku, headers=headersBuku,tablefmt='grid'))
          
        else:
          print('Mohon Maaf Tidak Ada Hasil yang Sesuai dengan Filter yang di Input')

      elif menuList == 3:
          return
      else:
        print('Silahkan Masukan Input "1" sampai "3"')
        continue
    except ValueError:
      print('\nSilahkan Masukan "Angka" Bukan Huruf')
      continue


### Fungsi Untuk meminjam Buku
def pinjamBuku(perpustakaanMelati): 
   keranjangBuku = []
   keranjangPinjam = []
   namaPeminjam = []

   while True: 
    # Input Nama
      while True:

        masukanNama = str(input('Silahkan Masukan Nama Peminjam:')).strip().capitalize()
        
        if masukanNama.isdigit(): #Kalau Nama dimasukan Angka
          print('Silahkan Masukan "Nama Anda" bukan "Angka"\n')
          continue

        elif masukanNama == '': #Kalau Nama Diisi Kosong
          print ('Nama Harus Diisi Tidak Boleh Kosong\n')
          continue

        #Memastikan Nama Sudah Benar
        while True:
          tanyaNama = str(input(f'\nApakah Nama {masukanNama} Sudah Sesuai (sudah/belum)?\n')).strip().lower()
          
          if tanyaNama.isdigit(): #Jika Menjawab Angka Bukan Belum atau Sudah
            print ('Silahkan Masukan "Huruf" Bukan Angka\n')
            continue

          elif tanyaNama == 'belum': #Kalau Belum Sesuai
            break

          elif tanyaNama == 'sudah': #jika nama yang dimasukan sudah sessuai
            print(f'\nNama "{masukanNama}" Sudah Tercatat Sebagai Nama Peminjam')
            keranjangSementara = []
            break

          else: #selain sudah atau belum
            print('Silahkan Pilih "Sudah" dan "Belum" Saja\n')
            continue

        if tanyaNama == 'belum': #biar ngeloop lagi ke awal
          continue
    
        # input Pinjam Buku
        while True: 

          pinjamBuku = str(input('\nSilahkan Masukan Judul Buku yang Mau Dipinjam:')).strip().lower()
          
          if pinjamBuku.isdigit(): #kalau input pinjam buku angka
            print('Silahkan Masukan Huruf Bukan Angka')
            continue
          
          if pinjamBuku == '': #kalau input isi buku kosong
            print('Silahkan Isi Buku yang Dipinjam')
            continue
          
          if pinjamBuku in perpustakaanMelati['buku']: #kalau buku yang kita inpu ada di pepustkaan melati
            posisiBuku = perpustakaanMelati['buku'].index(pinjamBuku) #untuk mengatahuin index buku yang kita tulis

            if perpustakaanMelati['stok'][posisiBuku] == 0: #ini kalau misal bukunya dah ada di perustkaan melati tapi stoknya 0
              print(f'\nMohon Maaf Buku {pinjamBuku}, Saat Ini Stoknya Habis')
              print('Silahkan Pilih Buku yang Masih Tersedia')
              continue
            
          else: #kalau buku yang kita pinjam ga ada di perpustakaan melati
            print(f'\nMohon Maaf Buku "{pinjamBuku}" Tidak Tersedia')
            return keranjangBuku, keranjangPinjam, namaPeminjam
          

          #mengecek apakah buku yang kita pinjem sudah ada di keranjang sementara
          totalSementara = 0
          for item in keranjangSementara: 
            if item['judul'] == pinjamBuku:
              totalSementara += item['jumlah'] #kalau sudah ada bukan buat list baru tapi namabhain jumlahnya
            
          stokTersedia = perpustakaanMelati['stok'][posisiBuku] - totalSementara
          


            ### pinjem jumlah buku
          while True:
              jumlahPinjam = 0
                
              try:
                pinjamBerapa = int(input('Mau Berapa Banyak Buku yang Dipinjam:'))
                jumlahPinjam += pinjamBerapa

                if pinjamBerapa < 0:
                  print('Silahkan Masukan Jumlah Buku yang Mau Dipinjam, Tidak Boleh Minus')
                  continue

                elif pinjamBerapa == 0:
                  print(f'\nKarena Anda Meminjam "{pinjamBuku}" dengan Jumlah "{pinjamBerapa}" buah')
                  print('Maka Anda Dianggap Tidak Jadi Meminjam Buku\n')
                  return keranjangBuku, keranjangPinjam, namaPeminjam
                
                elif pinjamBerapa > stokTersedia:
                  print('\nAnda Meminjam Melebihi Stok Yang Ada')
                  print(f'Saat Ini Anda Meminjam {totalSementara} Untuk Buku Ini')
                  print(f'Yang bisa Dipinjam Tinggal "{stokTersedia}" Buah Saja\n')
                  continue
                else:
                  print(f'Meminjam {pinjamBerapa} Buah Buku')
                  break
              except ValueError:
                print('Silahkan Masukan Angka Bukan Huruf')
                continue    
          
          #cek buku yang sudah di input hasil pinjam
          sudahAda = False
          for item in keranjangSementara:
              if item['judul'] == pinjamBuku:
                  item['jumlah'] += jumlahPinjam
                  sudahAda = True
                  break
          if not sudahAda:
            keranjangSementara.append({'judul':pinjamBuku,'jumlah':pinjamBerapa,'nama': masukanNama })
          
          print(f'\nBuku "{pinjamBuku}" Dipinjam Sebanyak "{pinjamBerapa}" buah\n')


          while True:
            tambahan = str(input('Apakah Ada Buku yang Mau dipinjam Lagi (ya/tidak)?   '+'\n')).strip().lower()
            if tambahan == 'ya':
              break
            elif tambahan == 'tidak':
                for item in keranjangSementara:
                  judul = item['judul']
                  jumlah = item['jumlah']
                  nama = item['nama']
                  posisiBuku = perpustakaanMelati['buku'].index(judul)

                  perpustakaanMelati['stok'][posisiBuku] -= jumlah 

                  sudahAda = False
                  for i in range(len(keranjangBuku)):
                    if keranjangBuku[i] == judul and namaPeminjam[i] == nama:
                      keranjangPinjam[i] += jumlah
                      sudahAda = True
                      break

                  if not sudahAda:
                      keranjangBuku.append(judul)
                      keranjangPinjam.append(jumlah)
                      namaPeminjam.append(nama)
                print(f'\nTerimakasih "{masukanNama}" Atas Peminjamannya')
                return keranjangBuku, keranjangPinjam, namaPeminjam
            else:  
              print('Silahkan Masukan "ya" atau "tidak"') 
              continue


#### fungsi pengembalian buku baru new
def pengembalianBuku2(namaPeminjam):
  while True:
            if not keranjangBuku:
              print('\nTidak Ada Buku yang Sedang Dipinjam\n')
              break

            inputNamaPeminjam = str(input('Silahkan Masukan Nama Anda:')).strip().capitalize()

            if inputNamaPeminjam not in namaPeminjam:
              print(f'\nMohon Maaf Nama "{inputNamaPeminjam}" Tidak Ada Dalam Daftar Peminjam\n')
              break
    
            headers = ['No','Buku','Jumlah Peminjaman','Nama Peminjam']
            wadah = []

            for i in range(len(namaPeminjam)):
              if namaPeminjam[i] == inputNamaPeminjam:
               baris = [len(wadah)+1,
                  keranjangBuku[i],
                  keranjangPinjam[i],
                  namaPeminjam[i]
                ]
               wadah.append(baris)
                      
            print('\nBerikut Buku yang Anda Pinjam:')
            print(tabulate(wadah, headers=headers, tablefmt='grid'))

            while True: 
              konfirmasi = str(input('\nApakah Anda Ingin Mengembalikan Semua Buku Yang Dipinjam "(ya/tidak)"?')).strip().lower()
              
              if konfirmasi == 'ya':

                i=0
                
                while i < len(namaPeminjam):
                  if namaPeminjam[i] == inputNamaPeminjam:
                    judul = keranjangBuku[i]
                    jumlah = keranjangPinjam[i]
                    posisi = perpustakaanMelati['buku'].index(judul)
                    perpustakaanMelati['stok'][posisi] += jumlah

                    del keranjangBuku[i]
                    del keranjangPinjam[i]
                    del namaPeminjam[i]

                  else:
                    i += 1
                print(f'\nTerimakasih "{inputNamaPeminjam}" Telah Mengembalikan Semua Buku Yang Dipinjam')
                return
              
              elif konfirmasi == 'tidak':

                  judulKembali = str(input('\nSilahkan Tuliskan Nama Buku yang Mau Dikembalikan:')).strip().lower()
                  
                  if judulKembali.isdigit():
                    print('Silahkan Masukan Huruf Bukan Angka')
                    continue

                  ditemukan = False
                  for i in range(len(namaPeminjam)):
                    if namaPeminjam[i] == inputNamaPeminjam and keranjangBuku[i] == judulKembali:
                      ditemukan = True
                    
                      try:
                        jumlahKembali = int(input(f'\nBerapa Jumlah Buku yang Mau Dikembalikan:'))
                        
                        if jumlahKembali < keranjangPinjam[i]:
                          posisiBuku = perpustakaanMelati['buku'].index(judulKembali)
                          perpustakaanMelati['stok'][posisiBuku] += jumlahKembali
                          keranjangPinjam[i] -= jumlahKembali
                        
                          print(f'\nTerimakasih Buku "{judulKembali}" Telah Dikembalikan Sebanyak "{jumlahKembali}" Buah')
                          print(f'Buku "{judulKembali}" yang Belum Dikembalikan Sebanyak "{keranjangPinjam[i]}" Buah')
                          return

                        elif jumlahKembali == keranjangPinjam[i]:
                          posisiBuku = perpustakaanMelati['buku'].index(judulKembali)
                          perpustakaanMelati['stok'][posisiBuku] += jumlahKembali

                          del keranjangBuku[i]
                          del keranjangPinjam[i]
                          del namaPeminjam[i]
                          
                          print(f'Terima Kasih "{inputNamaPeminjam}" Telah Mengembalikan Buku yang Dipinjam')
                          return

                        else:
                          print('Jumlah yang Anda Masukan Lebih Dari Apa yang Anda Pinjam')
                          continue
                      except ValueError:
                         print('Silahkan Masukan Angka Bukan Huruf')
                         continue
                  if not ditemukan:
                    print('\nMohon Maaf Buku Tidak Ditemukan Dalam Daftar Pinjam Anda')
                    return 
              else:
                print('Silahkan Pilih "ya" atau "tidak" Saja')
                continue            


#### fungsi Update Buku
def updateBuku(perpustakaanMelati):
  while True:
    try:
      while True:
        tanyaTabel = str(input('Apakah Ingin Melihat List Tabel Buku Terlebih Dahulu "(ya/tidak)"?'))
        if tanyaTabel == 'ya':
          print('\nBerikut Merupakan List Buku Perpustakaan Melati:')
          tabelPerpus(perpustakaanMelati)
          break
        elif tanyaTabel == 'tidak':
          break
        else:
          print('Silahkan Pilih "ya" dan "tidak" saja')
          continue

      while True:
        index_input = int(input('\nSilahkan Masukan "id" List yang Mau di Update:'))
        if index_input in perpustakaanMelati['id']:
          posisi = perpustakaanMelati['id'].index(index_input)
          print(f'Update Index "{index_input}" Pada List Perpustakaan Melati')
          break
        else:
          print(f'Index {index_input} Tidak Ditemukan Pada List')
          return

      while True:
        print('\nApa yang Ingin Anda Update:\n')
        print('='*40)
        print('1. Judul Buku')
        print('2. Genre Buku')
        print('3. Penulis Buku')
        print('4. Stok Buku')
        print('='*40)
        try:
           pilihan = int(input('\nMasukan Pilihan (1-4): '))

           if pilihan == 1:
              while True:
                updateBuku = str(input('Masukan Judul Buku Baru:')).strip().lower()
                if updateBuku and not updateBuku.isdigit():
                    print(f'''Memperbarui Judul Buku dari "{perpustakaanMelati['buku'][posisi]}" Menjadi "{updateBuku}"''')
                    inputYesNo1 = str(input('Simpan Pembaruan (iya/tidak)??')).strip().lower()
                    if inputYesNo1 == 'iya':
                      perpustakaanMelati['buku'][posisi] = updateBuku
                      print(f'Nama Buku Berhasil Diperbarui Menjadi {updateBuku}')
                      return
                    elif inputYesNo1 == 'tidak':
                      return
                    else:
                      print('Silahkan Pilih "iya" atau "tidak" saja')
                      continue  
                else:
                  print('Silahkan Isi Huruf dan Bukan Angka, Isian Tidak Boleh Kosong')
                  continue

                    

                
           elif pilihan == 2:
              while True:
                updateGenre = str(input('Masukan Genre Baru:')).strip().lower()
                if updateGenre and not updateGenre.isdigit():
                   perpustakaanMelati['genre'][posisi] = updateGenre
                   print(f'Genre Buku Berhasil Diperbarui Menjadi {updateGenre}')
                   inputYesNo2 = str(input('Simpan Pembaruan (iya/tidak)??')).strip().lower()
                   if inputYesNo2 == 'iya':
                      perpustakaanMelati['genre'][posisi] = updateGenre
                      print(f'Genre Buku Berhasil Diperbarui Menjadi {updateGenre}')
                      return
                   elif inputYesNo2== 'tidak':
                      return
                   else:
                      print('Silahkan Pilih "iya" atau "tidak" saja')
                      continue  
                else:
                   print('Silahkan Isi Huruf dan Bukan Angka, Isian Tidak Boleh Kosong')
                   continue

                 
           elif pilihan == 3:
              while True:  
                updatePenulis = str(input('Masukan Penulis Baru:')).strip().lower()
                if updatePenulis and not updatePenulis.isdigit():
                   perpustakaanMelati['penulis'][posisi] = updatePenulis
                   print(f'Penulis Buku Berhasil Diperbarui Menjadi {updatePenulis}')
                   inputYesNo3 = str(input('Simpan Pembaruan (iya/tidak)??')).strip().lower()
                   if inputYesNo3 == 'iya':
                      perpustakaanMelati['penulis'][posisi] = updatePenulis
                      print(f'Nama Buku Berhasil Diperbarui Menjadi {updatePenulis}')
                      return
                   elif inputYesNo3 == 'tidak':
                      return
                   else:
                      print('Silahkan Pilih "iya" atau "tidak" saja')
                      continue  
                else:
                   print('Silahkan Isi Huruf dan Bukan Angka, Isian Tidak Boleh Kosong')
                   continue

                
           elif pilihan == 4:
              while True:
                updateStok = int(input('Masukan Stok Buku Baru:'))
                if updateStok >= 0:
                   perpustakaanMelati['stok'][posisi] = updateStok
                   print(f'Stok Buku Berhasil Diperbarui Menjadi {updateStok}')
                   inputYesNo4 = str(input('Simpan Pembaruan (iya/tidak)??')).strip().lower()
                   if inputYesNo4 == 'iya':
                      perpustakaanMelati['stok'][posisi] = updateStok
                      print(f'Nama Buku Berhasil Diperbarui Menjadi {updateStok}')
                      return
                   elif inputYesNo4 == 'tidak':
                      return
                   else:
                      print('Silahkan Pilih "iya" atau "tidak" saja')
                      continue  
                else:
                   print('Stok Tidak Bisa Negatif')
                   continue                  
           else:
             print('Hanya Bisa Input 1-4 Saja')
             continue

        except ValueError:
          print('Silahkan Masukan Angka dan Bukan Huruf')
          continue
    except ValueError:
      print('Silahkan Masukan Angka Bukan Huruf')
      continue 


###Fungsi Untuk Menambah Buku
def tambahBuku(perpustakaanMelati):
  while True:  
    while True: ### masukan judul buku yang mau ditambah
      tambahBuku = str(input('\nSilahkan Masukan Judul Buku Yang mau ditambah:')).strip().lower()
      if not tambahBuku:
        print('Silahkan Isi Buku yang Mau ditambah\n')
        continue
      elif tambahBuku.isdigit():
        print ('Silahkan Masukan Huruf Bukan Angka\n')
        continue
      elif tambahBuku in perpustakaanMelati['buku']:
        print('\n"Mohon Maaf Buku yang Dimasukan Sudah Ada"')
        print('"Silahkan Masukan Judul Buku yang Lain"\n')
        return
      else:
        break

    while True: ### masukan genre
      tambahGenre = str(input('Silahkan Masukan Genre Buku:')).strip().lower()
      if not tambahGenre:
        print('Silahkan Isi Penulis Buku\n')
        continue
      elif tambahGenre.isdigit():
        print ('Silahkan Masukan Huruf Bukan Angka\n')
        continue
      else:
        break
       
    while True: ### masukan penulisnya
      tambahPenulis = str(input('Silahkan Masukan Penulis Buku:')).strip().lower()
      if not tambahPenulis:
        print('Silahkan Isi Penulis Buku\n')
        continue
      elif tambahPenulis.isdigit():
        print ('Silahkan Masukan Huruf Bukan Angka\n')
        continue
      else:
        break
       
    while True: ### masukan stok buku
      try:
        tambahStok = int(input('Silahkan Masukan Stok Buku:'))
        if tambahStok < 0:
          print('Tidak Boleh Memasukan Angka Negatif\n')
          continue
        else:
          break
      except ValueError:
        print('Silahkan Masukan Angka Bukan Huruf\n')
        continue
    
    if perpustakaanMelati['id']:
      newIndex = max(perpustakaanMelati['id']) + 1
    else:
      newIndex = 0

    perpustakaanMelati['id'].append(newIndex)
    perpustakaanMelati['buku'].append(tambahBuku)
    perpustakaanMelati['genre'].append(tambahGenre)
    perpustakaanMelati['penulis'].append(tambahPenulis)
    perpustakaanMelati['stok'].append(tambahStok)

    print('\nBerhasil Menambahkan Buku ' + f'"{tambahBuku}"' + ' Dengan Genre ' + f'"{tambahGenre}"' +' Ditulis oleh ' + f'"{tambahPenulis}"' + ' dengan Jumlah ' + f'"{tambahStok}"' + ' buah\n')
  
    while True:
      tambahLagi = str(input('Mau Menambah Buku lagi (ya/tidak)?')).strip().lower()
      if tambahLagi == 'ya':
        break
      elif tambahLagi == 'tidak':
        return
      else:
        print('Silahkan Hanya Masukan Opsi "ya" atau "tidak"')
        continue


### Untuk Hapus Semua isi Dictionary
def HapusSemua(perpustakaanMelati):
    for key in perpustakaanMelati:
        perpustakaanMelati[key].clear()


### Fungsi Untuk Hapus Buku
def hapusBuku(perpustakaanMelati):

  while True:
    konfirmasiHapus = input('Hapus Semua Buku Atau Hanya Satu (semua/satu)?').strip().lower()
    if konfirmasiHapus.isdigit():
      print('Silahkan Masukan "Huruf" bukan "Angka"')
      continue
    elif konfirmasiHapus != 'semua' and  konfirmasiHapus != 'satu':
      print('Silahkan Hanya Pilih "semua" atau "satu"')
      continue
    elif konfirmasiHapus == 'semua':
      HapusSemua(perpustakaanMelati)
      print('\nSemua Buku Berhasil Dihapus')
      return

    elif konfirmasiHapus == 'satu':
      while True:
          try: 
            idHapus = int(input('\nSilahkan Pilih Nomer Id Buku yang Mau Dihapus:'))
            if idHapus in perpustakaanMelati['id']:

              letak = perpustakaanMelati['id'].index(idHapus) ### untuk mengetahui index mana yang dihapus

              bukuDihapus = perpustakaanMelati['buku'][letak]

              for key in perpustakaanMelati:
                perpustakaanMelati[key].pop(letak)
              
              panjangDataList = len(perpustakaanMelati['id'])

              listSementara = []

              for i in range(panjangDataList):
                listSementara.append(i)

              perpustakaanMelati['id'] = listSementara

              print(f'\nBuku ' + f'"{bukuDihapus}"' ' Berhasil Dihapus Dari List')
              print('\nSilahkan Lihat List Buku Untuk Melihat List yang Bukunya Tadi Sudah Dihapus\n')
            else:
              print(f'\nMohon Maaf Nomer Id "{idHapus}" Tidak Ditemukan,')
              print('silahkan Pilih Input "2" Untuk Melihat List Buku yang Tersedia')
              return
          except ValueError:
            print('\nSilahkan Masukan Angka Bukan Huruf')
            continue
    

          while True:
            hapusLagi = str(input('Apakah Ada Lagi Buku yang Mau dihapus (ya/tidak)? ')).strip().lower()
            if hapusLagi == 'ya':
              break
            elif hapusLagi == 'tidak':
              return
            else:
              print('Silahkan Hanya Masukan Opsi "ya" atau "tidak"')
              continue


###########################################################################################

#Aplikasi Perpustakaan Sederhana

#Membuat Greetings Awal
firstRun = True

keranjangBuku = []
keranjangPinjam = []
namaPeminjam = []

while True:
  if firstRun:
    print('\n'+'='*40)
    print('Selamat Datang di Perpustakaan Melati'.center(40))
    print('='*40)
    print('\nSilahkan Pilih Layanan:\n')
    print('1.Lihat List Buku')
    print('2.Pinjam Buku')
    print('3.Pengembalian Buku')
    print('4.Update Data Perpustakaan')
    print('5.Tambah Buku Baru')
    print('6.Hapus Buku Dalam List')
    print('7.Keluar Perpustakaan')
    print('='*40 + '\n')
    firstRun = False
  else:
    print('\n'+'='*40)
    print('Silahkan Pilih Layanan:\n')
    print('1.Lihat List Buku')
    print('2.Pinjam Buku')
    print('3.Pengembalian Buku')
    print('4.Update Data Perpustakaan')
    print('5.Tambah Buku Baru')
    print('6.Hapus Buku Dalam List')
    print('7.Keluar Perpustakaan')
    print('='*40 + '\n' )
  

## Input Layanan Yang ada
  while True:
    try:
        inputLayanan = int(input('Pilih Layanan yang Ada (1-7):' ))
        if inputLayanan < 1 or inputLayanan > 7:
          print('Silahkan Pilih Layanan yang Tersedia Pada Tampilan')
          continue
        break
    except ValueError:
      print('Silahkan Masukan Angka Bukan Huruf')
      continue

### Input Layanan 1 Melihat list Buku
  if inputLayanan == 1:
    listMenu(perpustakaanMelati)



## input layanan 2 pinjam buku
  if inputLayanan == 2:

    while True:
      print('\n'+'MENU 2: PINJAM BUKU PERPUS:')
      print('='*40  )
      print('1. Pinjam Buku')
      print('2. Lihat Buku Yang Dipinjam')
      print('3. Kembali Ke Menu Awal')
      print('='*40 + '\n' )
      try:   
            # Input Pinjam Buku
            menuPinjamBuku = int(input('Silahkan Pilih Layanan yang Ada (1-3):'))
            if not menuPinjamBuku: 
                print('Input Tidak Boleh Kosong')
                continue
            
            # 1 Pinjam Buku
            elif menuPinjamBuku == 1:
                print('\n')
                tabelPerpus(perpustakaanMelati)
                print('\n')
                bukuBaru,pinjamBaru,namaPinjem = pinjamBuku(perpustakaanMelati)
                keranjangBuku.extend(bukuBaru)
                keranjangPinjam.extend(pinjamBaru)
                namaPeminjam.extend(namaPinjem)
            
            # 2 Melihat Buku Yang Dipinjam 
            elif menuPinjamBuku == 2:
                if keranjangBuku and keranjangPinjam:    
                  print('\nBerikut Merupakan Buku yang Sedang Di Pinjam:')            
                  tabelPinjamBuku(keranjangBuku)
                else: 
                  print('\nBelum Ada Buku yang Dipinjam Saat Ini')
                  tabelPinjamBuku(keranjangBuku)
            
            # 3 keluar dari menu pinjam   
            elif menuPinjamBuku == 3:
                break
            else:
              print('Silahkan Pilih input antara "1" sampai "3"')
              continue
      except ValueError:
        print('Silahkan Masukan Input Angka Bukan Huruf')
        continue

  

### input layanan 3 Pengembalian Buku
  if inputLayanan == 3:
    while True:
      try:
        print('\n'+'MENU 3: PENGEMBALIAN BUKU PERPUSTAKAAN MELATI:')
        print('='*40  )
        print('1. Lihat Buku Yang Dipinjam')
        print('2. Pengembalian Buku')
        print('3. Kembali Ke Menu Awal')
        print('='*40 + '\n' )
      
        
        pengembalianInput = int(input('Pilih Layanan Pengambalian (1-3):\n'))
      
        if pengembalianInput == 1:
            if keranjangBuku and keranjangPinjam:
              print('\nBerikut Merupakan List Buku yang Dipinjem:')
              tabelPinjamBuku(keranjangBuku)
              continue
            else:
              print('\nBelum Ada Buku yang Dipinjam Saat Ini')
              tabelPinjamBuku(keranjangBuku)
              continue

        elif pengembalianInput == 2:
          pengembalianBuku2(namaPeminjam)
                  

        elif pengembalianInput == 3:
          break

        else:
          print('Silahkan Masukan Input "1-3" Saja')
        
    
      except ValueError:
        print('Silahkan Masukan Angka Bukan Huruf')

     
    
##### input layanan 4 Update Buku
  if inputLayanan == 4:
    while True:
      print('\n'+'MENU 4: Update Data Perpustakaan:')
      print('='*40  )
      print('1. Update Data Perpustakaan')
      print('2. Kembali Ke Menu Awal')
      print('='*40 + '\n' )
      try:
            menuUpdateBuku = int(input('Silahkan Pilih Layanan yang Ada (1-2):'))
            if not menuUpdateBuku: 
              print('Input Tidak Boleh Kosong')
              continue
            elif menuUpdateBuku == 1:
              updateBuku(perpustakaanMelati)
              continue
            elif menuUpdateBuku == 2:
                break
            else:
              print('Silahkan Pilih input antara "1" sampai "3"')
              continue
      except ValueError:
        print('Silahkan Masukan Input Angka Bukan Huruf')
        continue
   


## input Layanan 5 Tambah
  if inputLayanan == 5:
    while True:
      print('\n'+'MENU 5: MENAMBAH BUKU BARU:')
      print('='*40  )
      print('1. Menambah Buku Baru')
      print('2. Lihat List Buku')
      print('3. Kembali Ke Menu Awal')
      print('='*40 + '\n' )
      try:
            menuTambahBuku = int(input('Silahkan Pilih Layanan yang Ada (1-3):'))
            if not menuTambahBuku: 
                print('Input Tidak Boleh Kosong')
                continue
            elif menuTambahBuku == 1:
                tambahBuku(perpustakaanMelati) 
            elif menuTambahBuku == 2:
                tabelPerpus(perpustakaanMelati)     
            elif menuTambahBuku == 3:
                break
            else:
              print('Silahkan Pilih input antara "1" sampai "3"')
              continue
      except ValueError:
        print('Silahkan Masukan Input Angka Bukan Huruf')
        continue


## input Layanan 6 Hapus Buku
  if inputLayanan == 6:
    while True:
        try:
           print('\n'+'Hapus Buku Dalam Daftar:')
           print('='*40  )
           print('1. Hapus Buku')
           print('2. Lihat List Buku')
           print('3. Kembali Ke Menu Awal')
           print('='*40 + '\n' )
           menuHapusBuku = int(input('Silahkan Pilih Layanan yang Ada (1-3):'))
           if not menuHapusBuku: 
            print('Input Tidak Boleh Kosong')
            continue
           elif menuHapusBuku == 1:
            hapusBuku(perpustakaanMelati)
           elif menuHapusBuku == 2:
            tabelPerpus(perpustakaanMelati)
            continue
           elif menuHapusBuku == 3:
            break
           else:
            print('Silahkan Pilih input antara "1" sampai "3"')
            continue
        except ValueError:
          print('Silahkan Masukan Input Angka Bukan Huruf')
          continue
  

###### input 7 keluar perpustakaan  
  keluarPerpus = False

  if inputLayanan == 7:
    while True:
      keluarMenu = str(input('\nApakah Anda Ingin Keluar Perpustakaan (ya/tidak)?\n')).strip().lower()
      if keluarMenu == 'ya':  
        print("\n---Terimakasih Sudah Berkungjung Ke Perpustakaan Melati---\n".center(40).upper())
        keluarPerpus = True
        break
      if keluarMenu == 'tidak':
        break
      else:
        print('Silahkan Pilih "ya" atau "tidak" saja')
        continue
  if keluarPerpus:
    break
  
        
      

        
        
      

      

  






    

   
