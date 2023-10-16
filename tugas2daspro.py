#toko ikan cupang
data_ikan_cupang = ["rosetail" ,"elephant" ,"koi", "butterfly", "twintail", "cupang Penang", "cupang bintik", "kingofgolddragon", "growntail", "plakat fantail"]

#Fungsi untuk menambahkan ikan cupang
def tambah_ikan_cupang():
    nama = input("Masukkan jenis ikan cupang: ")
    jenis_kelamin= input("Masukkan jenis kelamin: ")
    harga = input("Masukkan harga ikan cupang (Rp): ")
    data_ikan_cupang.append({"Nama": nama, "jenis kelamin": jenis_kelamin, "Harga (Rp)": harga})
    print("Ikan cupang berhasil ditambahkan!")

#Fungsi untuk mengubah data ikan 
def ubah_ikan_cupang():
    indeks = int(input("Masukkan nomor ikan cupang yang ingin diubah: ")) - 1
    if 0 <= indeks < len(data_ikan_cupang):
        field = input("Masukkan jenis ikan cupang yang ingin diubah (Nama/Jenis Kelamin/Harga (Rp)): ")
        new_value = input(f"Masukkan jenis baru untuk {field}: ")
        if field.lower() == "nama":
            data_ikan_cupang[indeks]["Nama"] = new_value
        elif field.lower() == "jenis kelamin":
            data_ikan_cupang[indeks]["jenis kelamin"] = new_value
        elif field.lower() == "harga (rp)":
            data_ikan_cupang[indeks]["Harga (Rp)"] = new_value
        else:
            print("Data ikan cupang berhasil diubah!")
    else:
        print("Nomor ikan cupang tidak valid.")

#Fungsi untuk menghapus ikan cupang
def hapus_ikan_cupang():
    indeks = int(input("Masukkan nomor ikan cupang yang ingin dihapus: ")) - 1
    if 0 <= indeks < len(data_ikan_cupang):
        data_ikan_cupang.pop(indeks)
        print("Ikan cupang berhasil dihapus!")
    else:
        print("Nomor ikan cupang tidak valid.")

#Fungsi untuk login sebagai pembeli
def login_pembeli():
    username = input("Masukkan username pembeli: ")
    password = input("Masukkan password pembeli: ")
    return {"username": username, "password": password}

#Main program
while True:
    print("\nMenu Ikan cupang:")
    print("1. Login Admin")
    print("2. login pembeli")
    print("3. Keluar")
    
    pilihan = input("Masukkan nomor menu: ")

    if pilihan == "1":
        username = input("Masukkan username admin: ")
        password = input("Masukkan password admin: ")
        
        #login sebagai admin 
        if username == "fachi" and password == "180903":
            while True:
                print("\nMenu Admin:")
                print("1. Tambah Ikan cupang")
                print("2. Ubah Ikan cupang")
                print("3. Hapus Ikan cupang")
                print("4. Logout Admin")
                
                pilihan_admin = input("Masukkan nomor menu: ")
                
                if pilihan_admin == "1":
                    tambah_ikan_cupang()
                elif pilihan_admin == "2":
                    ubah_ikan_cupang()
                elif pilihan_admin == "3":
                    hapus_ikan_cupang()
                elif pilihan_admin == "4":
                    print("Logout dari admin.")
                    break
                else:
                    print("Menu tidak valid.")
        else:
            print("Login admin gagal. Coba lagi.")
        
    elif pilihan == "2":
        from prettytable import PrettyTable
        table = PrettyTable()
        table.field_names=["no","jenis ikan cupang","harga"]
        table.add_row([1, "rosetail","700.000"])
        table.add_row([2, "elephant ear","300.000"])
        table.add_row([3, "koi","300.000"])
        table.add_row([4, "butterfly","224.000"])
        table.add_row([5, "twin tali","500.000"])
        table.add_row([6, "cupang penang","100.000"])
        table.add_row([7, "cupang bintik","350.000"])
        table.add_row([8, "king of gold dragon","7.000.000"])
        table.add_row([9, "grown tail","7.500.000"])
        table.add_row([10, "plakat fantail","70.000.000"])
        print(table)
        username_pembeli = input("masukkan user pembeli :")
        hari_tanggal = input("masukkan hari dan tanggal :")
        no_handphone = int(input("masukkan nomor handphone :"))
        jenis_ikan_yang_pilih = input("masukkan jenis ikan yang akan di beli :")
        print("pembelian ikan cupang berhasil")
        break
        
    elif pilihan == "3":
        print("Keluar dari program.")
        break

