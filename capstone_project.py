# =================================================================================================
# Data Utama

dict_data   = {
        '1':{'Nama'         : 'Brownies',
           'Rasa'         : 'Almond',
           'Kategori'     : 'Cakes',
           'Stok'         : 20,  
           'Harga'        : 75000
           },
        '2':{'Nama'         : 'Brownies',
           'Rasa'         : 'Keju',
           'Kategori'     : 'Cakes',
           'Stok'         : 15,  
           'Harga'        : 80000
           },
        '3':{'Nama'         : 'Chiffon Cake',
           'Rasa'         : 'Pandan',
           'Kategori'     : 'Chiffon & Roll Cakes',
           'Stok'         : 5,  
           'Harga'        : 65000
           },
        '4':{'Nama'         : 'Chiffon Cake',
           'Rasa'         : 'Coklat',
           'Kategori'     : 'Chiffon & Roll Cakes',
           'Stok'         : 9,  
           'Harga'        : 65000
           }   
}

# =================================================================================================
# List Kategori & Rasa

list_rasa = [ 'Original',
                'Coklat',
                'Keju',
                'Almond',
                'Pandan']

def create_rasa():
    rasa = input_rasa(2).title()
    list_rasa.append(rasa)
    print_list(1)

def update_rasa():
    upd_item = input_rasa(3)

    for index, item in enumerate(list_rasa):
        
        if upd_item == str(index+1):
            print(f'''{upd_item}. {item}''')
            
            while True:
                mengubahData = input('Apakah ingin mengubah Data tersebut? (Ya/Tidak)').lower()
                
                if mengubahData == 'ya':
                    # mengubah data pada list rasa
                    rasa = input_rasa(2).title()
                    list_rasa[int(upd_item)-1] = rasa
                    print(f'''
        ============= Data Terupdate =============
        ''')
                    print_list(1)
                    break
                
                elif mengubahData == 'tidak':
                    update_rasa()
                    
                else:
                    print_salah_perintah()
                    update_rasa()

def delete_rasa():
    del_item = input_rasa(3)
    
    for index, item in enumerate(list_rasa):

        if del_item == str(index+1):
            print(f'''{del_item}. {item}''')
            
            while True:
                menghapusData = input('Apakah ingin menghapus Data tersebut? (Ya/Tidak)').lower()
                
                if menghapusData == 'ya':
                    # menghapus data pada list rasa
                    del list_rasa[int(del_item)-1]
                    print(f'''
        ============= Data Terhapus =============
        ''')
                    print_list(1)
                    break
                
                elif menghapusData == 'tidak':
                    delete_rasa()
                    
                else:
                    print_salah_perintah()
                    delete_rasa()

list_kategori = ['Bread',
                 'Cakes',
                 'Chiffon & Roll Cakes',
                 'Donut',
                 'Pastry & Danish',
                 'Tradiotional Snack',
                 'Pudding',
                 'Cookies',
                 'Lapis',
                 'Drink']

def create_kategori():
    kategori = input_kategori(2).title()
    list_kategori.append(kategori)
    print_list(2)

def update_kategori():
    upd_item = input_kategori(3)

    for index, item in enumerate(list_kategori):
        
        if upd_item == str(index+1):
            print(f'''{upd_item}. {item}''')
            
            while True:
                mengubahData = input('Apakah ingin mengubah Data tersebut? (Ya/Tidak)').lower()
                
                if mengubahData == 'ya':
                    # mengubah data pada list kategori
                    kategori = input_kategori(2).title()
                    list_kategori[int(upd_item)-1] = kategori
                    print(f'''
        ============= Data Terupdate =============
        ''')
                    print_list(2)
                    break
                
                elif mengubahData == 'tidak':
                    update_kategori()
                    
                else:
                    print_salah_perintah()
                    update_kategori()

def delete_kategori():
    del_item = input_kategori(3)

    for index, item in enumerate(list_kategori):
        
        if del_item == str(index+1):
            print(f'''{del_item}. {item}''')
            
            while True:
                menghapusData = input('Apakah ingin menghapus Data tersebut? (Ya/Tidak)').lower()
                
                if menghapusData == 'ya':
                    # menghapus data pada list kategori
                    del list_kategori[int(del_item)-1]
                    print(f'''
        ============= Data Terhapus =============
        ''')
                    print_list(2)
                    break
                
                elif menghapusData == 'tidak':
                    delete_kategori()
                    
                else:
                    print_salah_perintah()
                    delete_kategori()

# =================================================================================================
# Function Input

def input_kodeItem ():
    kodeItem   = input('Masukkan Kode Item: ')

    # Cek input berupa numeric
    input_list = list(kodeItem)
    check = [char.isnumeric() for char in input_list]
    
    if False in check:
        print_salah_input()
        input_kodeItem()
    
    else:
        # Cek input apakah sudah ada didalam data
        if kodeItem in dict_data.keys():
            print(f'''Data yang dimasukkan sudah tersedia!
        Tolong Masukkan Kode Item yang lain.''')
            input_kodeItem()
        
        # else dilakukan untuk mendeklarasikan recrusive function sebagai variabel pada if condition 
        # tujuannya agar input pada function tersebut bisa dijadikan 
        else:
            global inputkodeItem
            inputkodeItem = kodeItem

    return inputkodeItem

def input_nama ():
    nama     = input('Masukkan Nama Item: ')

    # cek input berupa alphabet dan spasi
    input_list = list(nama)
    check = [char.isalpha() or char.isspace() for char in input_list]
    
    if False in check:
        print_salah_input()
        input_nama()
    
    # else dilakukan untuk mendeklarasikan recrusive function sebagai variabel pada if condition 
    # tujuannya agar input pada function tersebut bisa dijadikan 
    else:
        global inputname
        inputname = nama.title()

    return inputname

def input_rasa (x):
    print_list(1)

    if x == 1:
        rasa = input('Masukkan nomor rasa: ')
        # Cek input berupa numeric
        input_list = list(rasa)
        check = [char.isnumeric() for char in input_list]
    
        if False in check:
            print_salah_input()
            input_rasa(1)
        else:
            rasa = int(rasa)
            if rasa <= len(list_rasa):
                rasa = str(rasa)
                for index, item in enumerate(list_rasa):
                    if rasa == str(index+1):
                        return item
            else:
                print_salah_input()
                input_rasa(1)

    elif x == 2:
        rasa   = input('Masukkan Rasa Item: ')

        # cek input berupa alphabet dan spasi
        input_list = list(rasa)
        check = [char.isalpha() or char.isspace() for char in input_list]
        
        if False in check:
            print_salah_input()
            input_rasa()
        
        # else dilakukan untuk mendeklarasikan recrusive function sebagai variabel pada if condition 
        # tujuannya agar input pada function tersebut bisa dijadikan 
        else:
            if rasa in list_rasa:
                print(f'Data yang dimasukkan telah tersedia. Tolong masukkan Rasa yang lain')
                input_rasa(2)

            else:
                global inputrasa
                inputrasa = rasa

        return inputrasa

    elif x == 3:
        rasa = input('Masukkan nomor rasa: ')
        # Cek input berupa numeric
        input_list = list(rasa)
        check = [char.isnumeric() for char in input_list]
    
        if False in check:
            print_salah_input()
            input_rasa(3)
        else:
            rasa = int(rasa)
            if rasa <= len(list_rasa):
                rasa = str(rasa)
                for index, item in enumerate(list_rasa):
                    if rasa == str(index+1):
                        return rasa
            else:
                print_salah_input()
                input_rasa(3)

def input_kategori (x):
    print_list(2)

    if x == 1:
        kategori = input('Masukkan nomor kategori: ')
        # Cek input berupa numeric
        input_list = list(kategori)
        check = [char.isnumeric() for char in input_list]
    
        if False in check:
            print_salah_input()
            input_kategori(1)
        else:
            kategori = int(kategori)
            if kategori <= len(list_kategori):
                kategori = str(kategori)
                for index, item in enumerate(list_kategori):
                    if kategori == str(index+1):
                        return item
            else:
                print_salah_input()
                input_kategori(1)

    elif x == 2:
        kategori = input('Masukkan Kategori Item: ')

        # cek input adalah alphabet dan spasi
        input_list = list(kategori)
        check = [char.isalpha() or char.isspace() for char in input_list]
        
        if False in check:
            print_salah_input()
            input_kategori(2)
        
        # else dilakukan untuk mendeklarasikan recrusive function sebagai variabel pada if condition 
        # tujuannya agar input pada function tersebut bisa dijadikan 
        else:
            if kategori in list_kategori:
                print(f'Data yang dimasukkan telah tersedia. Tolong masukkan Kategori yang lain')
                input_rasa()

            else:
                global inputkategori
                inputkategori = kategori

        return inputkategori
    
    elif x == 3:
        kategori = input('Masukkan nomor kategori: ')
        # Cek input berupa numeric
        input_list = list(kategori)
        check = [char.isnumeric() for char in input_list]
    
        if False in check:
            print_salah_input()
            input_kategori(3)
        else:
            kategori = int(kategori)
            if kategori <= len(list_kategori):
                kategori = str(kategori)
                for index, item in enumerate(list_kategori):
                    if kategori == str(index+1):
                        return kategori
            else:
                print_salah_input()
                input_kategori(3)

def input_stok ():
    stok = input('Masukkan Stok Item: ')

    # Cek input berupa numeric
    input_list = list(stok)
    check = [char.isnumeric() for char in input_list]
    
    if False in check:
        print_salah_input()
        input_stok()
    
    else:
        # mengubah type data sesuai dengan kebutuhan pada data utama
        stok = int(stok)

        # Cek input harus berada diantara 10 dan 1000
        MM = 10 <= stok <= 1000
        
        if MM == False:
            print_salah_input()
            input_stok()
        
        # else dilakukan untuk mendeklarasikan recrusive function sebagai variabel pada if condition 
        # tujuannya agar input pada function tersebut bisa dijadikan 
        else:
            global inputstok
            inputstok = stok

    return inputstok

def input_harga ():
    harga   = input('Masukkan Harga Item: ')
    input_list = list(harga)

    # Cek input berupa numeric
    check = [char.isnumeric() for char in input_list]
    
    if False in check:
        print_salah_input()
        input_harga()

    else:
        # mengubah type data sesuai dengan kebutuhan pada data utama
        harga = int(harga)

        # Cek input harus berada diantara 10000 dan 250000
        MM = 10000 <= harga <= 250000
        
        if MM == False:
            print_salah_input()
            input_harga()

        # else dilakukan untuk mendeklarasikan recrusive function sebagai variabel pada if condition 
        # tujuannya agar input pada function tersebut bisa dijadikan 
        else:
            global inputharga
            inputharga = harga

    return inputharga

# =================================================================================================
# Function Search Item

def search_item():
    pilihanItem = input('Masukkan Kode Item yang ingin dicari: ')
    # Cek input berupa numeric
    input_list = list(pilihanItem)
    check = [char.isnumeric() for char in input_list]
    
    if False in check:
        print_salah_input()
        search_item()
    
    else:

        if  pilihanItem in dict_data.keys():
            global inputpilihanItem
            inputpilihanItem = pilihanItem
            print_pilihan(pilihanItem, 1)
        
        else:
            print_salah()
            search_item()
    
    return inputpilihanItem

# =================================================================================================
# Function print

def print_data():
    print(f'''
==================================================== Daftar Menu Just Cake It! ====================================================
''')
    print("{: <20} {: <20} {: <20} {: <30} {: <20} {: <20}".format('Kode Item', '| Nama', ' | Rasa', '  | Kategori', '   | Stok', '    | Harga'))
    print(f'-----------------------------------------------------------------------------------------------------------------------------------------')

    for i in dict_data:
        print(f'''{i:<20} | {dict_data[i]['Nama']:<20}| {dict_data[i]['Rasa']:<20}| {dict_data[i]['Kategori']:<30}| {dict_data[i]['Stok']:<20}| {dict_data[i]['Harga']:<20}''')

def print_data_kosong():
    print(f'-----------------------------------------------------------------------------------------------------------------------------------------')
    print("{: >80}".format('Data Tidak Tersedia'))
    print(f'-----------------------------------------------------------------------------------------------------------------------------------------')

def print_pilihan(pilihan, x, data = dict_data):
    print()
    print("{: <20} {: <20} {: <20} {: <30} {: <20} {: <20}".format('Kode Item', '| Nama', ' | Rasa', '  | Kategori', '   | Stok', '    | Harga'))
    print(f'-----------------------------------------------------------------------------------------------------------------------------------------')
    
    # "x" merupakan kondisi untuk membedakan 
    # print sesuai pilihan dengan data yang tersedia
    # dan print data yang akan diinputkan pada data utama
    if x == 1:
        print(f'''{pilihan:<20} | {data[pilihan]['Nama']:<20}| {data[pilihan]['Rasa']:<20}| {data[pilihan]['Kategori']:<30}| {data[pilihan]['Stok']:<20}| {data[pilihan]['Harga']:<20}''')    

    elif x == 2:
        print(f'''{pilihan:<20} | {data['Nama']:<20}| {data['Rasa']:<20}| {data['Kategori']:<30}| {data['Stok']:<20}| {data['Harga']:<20}''')

def print_list(x):
    if x == 1:
        print(f'''
========================= Pilihan Rasa =========================''')
        for index, item in enumerate(list_rasa):
            print(f'{index+1}. {item}')
    elif x == 2:
        print(f'''
========================= Pilihan Kategori =========================''')
        for index, item in enumerate(list_kategori):
            print(f'{index+1}. {item}')

def print_salah():
    print("{: >50}".format('Data Tidak Tersedia'))
    print(f'''============= Data yang anda masukkan tidak sesuai dengan yang tersedia ============= ''')

def print_salah_input():
    print(f'''
============= Data yang dimasukkan Tidak Sesuai =============
Tolong masukkan Data yang sesuai
''')

def print_salah_menu():
    print(f'''
============= Menu yang anda masukkan tidak sesuai dengan pilihan Menu yang tersedia ============= ''')

def print_salah_perintah():
    print(f'''
============= Perintah yang dimasukkan Tidak Sesuai =============
Tolong masukkan Perintah yang sesuai
''')

# =================================================================================================
# Menu 1 (Read)

def menu1():
    print(f'''
List Menu Menampilkan Daftar Item:
1. Menampilkan Daftar Item
2. Mencari Item
3. Kembali ke Menu Utama
''')
    
    pilihanMenu = input('Masukkan Menu yang ingin dijalankan: ')

    if  (pilihanMenu == '1'):
        
        # memberikan kondisi apabila data keseluruhan tidak ada 
        if len(dict_data) == 0:
            print_data_kosong()
            menu1()
        else:
            print_data()
            menu1()

    elif(pilihanMenu == '2'):
        search_item()
        menu1()
    
    elif(pilihanMenu == '3'):
        menu_utama()
    
    else:
        print_salah_menu()
        menu1()

# =================================================================================================
# Menu 2 (Create)

def submenu1_menu2():
    input_keys  = input_kodeItem()
    nama        = input_nama()
    rasa        = input_rasa(1)
    kategori    = input_kategori(1)
    stok        = input_stok()
    harga       = input_harga()

    # memasukkan data input kedalam sebuah data collection
    dict_add = {'Nama'         : nama,
                'Rasa'         : rasa,
                'Kategori'     : kategori,
                'Stok'         : stok,  
                'Harga'        : harga}

    print_pilihan(input_keys, 2, dict_add)

    while True:
        menyimpanData = input('Apakah ingin menyimpan Data tersebut? (Ya/Tidak)').lower()
        
        if menyimpanData == 'ya':

            # menginput data kedalam data utama
            dict_data[input_keys] = dict_add
            print(f'''
============= Data Tersimpan =============
''')
            print_data()
            break

        elif menyimpanData == 'tidak':
            menu2()

        else:
            print_salah_perintah()

def menu2():
    print(f'''
List Menu Menambah Item:
1. Menambah Daftar Item
2. Kembali ke Menu Utama
''')
    
    pilihanMenu = input('Masukkan Menu yang ingin dijalankan: ')
    
    if  (pilihanMenu == '1'):
        submenu1_menu2()
        menu2()
    
    elif(pilihanMenu == '2'):
        menu_utama()
    
    else:
        print_salah_menu()
        menu2()

# =================================================================================================
# Menu 3 (Update)

def submenu1_menu3():
    edited = search_item()

    while True:
        mengubahData = input('Apakah ingin mengubah Data tersebut? (Ya/Tidak)').lower()

        if mengubahData == 'ya':
            print(f'''
                Pilih Kolom yang ingin diubah

                List Kolom:
                1. Kode Item
                2. Nama
                3. Rasa
                4. Kategori
                5. Stok
                6. Harga
                ''')

            while True:
                pilihanKolom = input('Masukkan Nomor Kolom yang ingin diubah(1-6): ')
                
                if pilihanKolom == '1':
                    kodeItem  = input_kodeItem()

                    while True:
                        menyimpanData = input('Apakah ingin menyimpan Data tersebut? (Ya/Tidak)').lower()

                        if menyimpanData == 'ya':
                            # melakukan update data pada data utama
                            dict_data[kodeItem] = dict_data.pop(edited)
                            print(f'''
                ============= Data Berhasil Terupdate =============
                ''')
                            print_pilihan(kodeItem,1)
                            break
                        
                        elif menyimpanData == 'tidak':
                            submenu1_menu3()
                        
                        else:
                            print_salah_perintah()
                        break
                    break

                elif pilihanKolom == '2':
                    nama     = input_nama()
                    
                    while True:
                        menyimpanData = input('Apakah ingin menyimpan Data tersebut? (Ya/Tidak)').lower()

                        if menyimpanData == 'ya':
                            # melakukan update data pada data utama
                            dict_data[edited]['Nama'] = nama
                            print(f'''
                ============= Data Berhasil Terupdate =============
                ''')
                            print_pilihan(edited,1)
                            break
                        
                        elif menyimpanData == 'tidak':
                            submenu1_menu3()
                        
                        else:
                            print_salah_perintah()
                        break
                    break
                

                elif pilihanKolom == '3':
                    rasa   = input_rasa(1)

                    while True:
                        menyimpanData = input('Apakah ingin menyimpan Data tersebut? (Ya/Tidak)').lower()

                        if menyimpanData == 'ya':
                            # melakukan update data pada data utama
                            dict_data[edited]['Rasa'] = rasa
                            print(f'''
                ============= Data Berhasil Terupdate =============
                ''')
                            print_pilihan(edited,1)
                            break
                        elif menyimpanData == 'tidak':
                            submenu1_menu3()
                        else:
                            print_salah_perintah()
                        break
                    break

                elif pilihanKolom == '4':
                    kategori = input_kategori(1)
                    
                    while True:
                        menyimpanData = input('Apakah ingin menyimpan Data tersebut? (Ya/Tidak)').lower()

                        if menyimpanData == 'ya':
                            # melakukan update data pada data utama
                            dict_data[edited]['Kategori'] = kategori
                            print(f'''
                ============= Data Berhasil Terupdate =============
                ''')
                            print_pilihan(edited,1)
                            break
                        
                        elif menyimpanData == 'tidak':
                            submenu1_menu3()
                        
                        else:
                            print_salah_perintah()
                        break
                    break

                elif pilihanKolom == '5':
                    stok = input_stok()
                    
                    while True:
                        menyimpanData = input('Apakah ingin menyimpan Data tersebut? (Ya/Tidak)').lower()

                        if menyimpanData == 'ya':
                            # melakukan update data pada data utama
                            dict_data[edited]['Stok'] = stok
                            print(f'''
                ============= Data Berhasil Terupdate =============
                ''')
                            print_pilihan(edited,1)
                            break
                        
                        elif menyimpanData == 'tidak':
                            submenu1_menu3()
                        
                        else:
                            print_salah_perintah()
                        break
                    break

                elif pilihanKolom == '6':
                    harga    = input_harga()
                    
                    while True:
                        menyimpanData = input('Apakah ingin menyimpan Data tersebut? (Ya/Tidak)').lower()

                        if menyimpanData == 'ya':
                            # melakukan update data pada data utama
                            dict_data[edited]['Harga'] = harga
                            print(f'''
                ============= Data Berhasil Terupdate =============
                ''')
                            print_pilihan(edited,1)
                            break

                        elif menyimpanData == 'tidak':
                            submenu1_menu3()

                        else:
                            print_salah_perintah()
                        break
                    break

                else:
                    print_salah_input()
            print_data()
            break

        elif mengubahData == 'tidak':
            menu3()

        else:
            print_salah_perintah()

def menu3():
    print(f'''
List Menu Mengubah Item:
1. Mengubah Daftar Item
2. Kembali ke Menu Utama
''')
    
    pilihanMenu = input('Masukkan Menu yang ingin dijalankan: ')
    
    if  (pilihanMenu == '1'):
        submenu1_menu3()
        menu3()
    
    elif(pilihanMenu == '2'):
        menu_utama()
    
    else:
        print_salah_menu()
        menu3()

# =================================================================================================
# Menu 4 (Delete)

def menu4():
    print(f'''
List Menu Menghapus Item:
1. Menghapus Daftar Item
2. Kembali ke Menu Utama
''')
    
    pilihanMenu = input('Masukkan Menu yang ingin dijalankan: ')
    
    if  (pilihanMenu == '1'):
        deleted = search_item()

        while True:
            menghapusData = input('Apakah ingin menghapus Data tersebut? (Ya/Tidak)').lower()
            
            if menghapusData == 'ya':
                # menghapus data pada data utama
                del dict_data[deleted]
                print(f'''
    ============= Data Terhapus =============
    ''')
                print_data()
                break
            
            elif menghapusData == 'tidak':
                menu4()
                
            else:
                print_salah_perintah()
        menu4()

    elif(pilihanMenu == '2'):
        menu_utama()

    else:
        print_salah_menu()
        menu4()

# =================================================================================================
# Menu 5 (Administrator)

def menu5():
    print(f'''
List Menu Administrator:
1. Menambah Rasa Item
2. Mengubah Rasa Item
3. Menghapus Rasa Item
4. Menambah Kategori Item
5. Mengubah Kategori Item
6. Menghapus Kategori Item
7. Kembali ke Menu Utama
''')
    
    pilihanMenu = input('Masukkan Menu yang ingin dijalankan: ')
    
    if  (pilihanMenu == '1'):
        create_rasa()
        menu5()

    elif(pilihanMenu == '2'):
        update_rasa()
        menu5()

    elif(pilihanMenu == '3'):
        delete_rasa()
        menu5()

    elif(pilihanMenu == '4'):
        create_kategori()
        menu5()

    elif(pilihanMenu == '5'):
        update_kategori()
        menu5()

    elif(pilihanMenu == '6'):
        delete_kategori()
        menu5()

    elif(pilihanMenu == '7'):
        menu_utama()

    else:
        print_salah_menu()
        menu5()

# =================================================================================================
# Menu Utama

def menu_utama():
    print(f'''
Selamat Datang di Just Cake It!

List Menu:
1. Menampilkan Daftar Item
2. Menambah Item
3. Mengubah Item
4. Menghapus Item
5. Administrator
6. Exit Program
''')
    
    pilihanMenu = input('Masukkan Menu yang ingin dijalankan: ')
    if  (pilihanMenu == '1'):
        menu1()
    
    elif(pilihanMenu == '2'):
        menu2()
    
    elif(pilihanMenu == '3'):
        menu3()
    
    elif(pilihanMenu == '4'):
        menu4()
    
    elif(pilihanMenu == '5'):
        menu5()

    elif(pilihanMenu == '6'):
        print('Terima Kasih')
        exit()
    
    else:
        print_salah_menu()
        menu_utama()

menu_utama()