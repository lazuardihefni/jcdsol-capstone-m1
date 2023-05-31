def tampilkan_stok(stok_gudang, nama_barang=None):
    print("Stok Barang:")
    if not stok_gudang:
        print("Gudang kosong.")
    else:
        barang_ditemukan = False
        for barang, stok in stok_gudang.items():
            if nama_barang is None or nama_barang.lower() == barang.lower():
                print(f"{barang}: {stok}")
                barang_ditemukan = True
        if not barang_ditemukan:
            print("Barang tidak ditemukan di dalam stok gudang.")


def tampilkan_stok_mengandung_nama(stok_gudang, nama_kata_kunci):
    print(f"Stok Barang yang Mengandung Nama '{nama_kata_kunci}':")
    if not stok_gudang:
        print("Gudang kosong.")
    else:
        barang_ditemukan = False
        for barang, stok in stok_gudang.items():
            if stok >= 0 and nama_kata_kunci.lower() in barang.lower():
                print(f"{barang}: {stok}")
                barang_ditemukan = True
        if not barang_ditemukan:
            print("Barang tidak ditemukan di dalam stok gudang.")


def tampilkan_stok_jumlah_tertentu(stok_gudang, jumlah_stok):
    while True:
        try:
            jumlah_stok = int(jumlah_stok)
            if jumlah_stok < 0:
                raise ValueError
            break
        except ValueError:
            print("Input Salah. Hanya bisa input angka >= 0.")
            jumlah_stok = input("Masukkan jumlah stok: ")

    print(f"Stok Barang dengan Jumlah Stok {jumlah_stok}:")
    if not stok_gudang:
        print("Gudang kosong.")
    else:
        barang_ditemukan = False
        for barang, stok in stok_gudang.items():
            if stok == jumlah_stok:
                print(f"{barang}: {stok}")
                barang_ditemukan = True
        if not barang_ditemukan:
            print("Stok barang tidak ada di gudang.")


def tambah_barang(stok_gudang):
    barang = input("Masukkan nama barang: ").lower()
    if barang in stok_gudang:
        while True:
            stok = input("Masukkan jumlah stok: ")
            try:
                stok = int(stok)
                if stok > 0:
                    stok_gudang[barang] += stok
                    print(f"Stok barang '{barang}' berhasil ditambahkan sebanyak {stok}.")
                    break
                else:
                    print("Jumlah stok harus > 0.")
            except ValueError:
                print("Input Salah. Hanya bisa input angka > 0.")
    else:
        while True:
            stok = input("Masukkan jumlah stok: ")
            try:
                stok = int(stok)
                if stok > 0:
                    stok_gudang[barang] = stok
                    print(f"Barang '{barang}' dengan stok {stok} berhasil ditambahkan.")
                    break
                else:
                    print("Jumlah stok harus > 0.")
            except ValueError:
                print("Input Salah. Hanya bisa input angka > 0.")


def kurangi_stok(stok_gudang):
    if not stok_gudang:
        print("Gudang kosong.")
        return

    while True:
        barang = input("Masukkan nama barang yang akan dikurangi stoknya: ").lower()
        if barang in stok_gudang:
            break
        else:
            print("Barang tidak ditemukan di dalam stok gudang. Silakan masukkan nama barang yang valid.")
    
    if stok_gudang[barang] == 0:
        print(f"Barang '{barang}' mempunyai stok 0 dan tidak bisa dikurangi.")
        return
    
    while True:
        jumlah = input(f"Masukkan jumlah stok yang akan dikurangi untuk barang '{barang}': ")
        try:
            jumlah = int(jumlah)
            if jumlah > 0:
                if jumlah <= stok_gudang[barang]:
                    stok_gudang[barang] -= jumlah
                    print(f"Stok barang '{barang}' berhasil dikurangi sebanyak {jumlah}.")
                    break
                else:
                    print(f"Stok barang '{barang}' tidak mencukupi untuk dikurangi sebanyak {jumlah}.")
            else:
                print("Jumlah stok harus > 0.")
        except ValueError:
            print("Input Salah. Hanya bisa input angka > 0.")


def hapus_barang(stok_gudang):
    if not stok_gudang:
        print("Gudang kosong.")
        return

    nama_barang = input("Masukkan nama barang yang akan dihapus (atau ketik 'semua' untuk menghapus semua barang): ")

    if nama_barang.lower() == 'semua':
        stok_gudang.clear()
        print("Semua barang berhasil dihapus dari gudang.")
    else:
        if nama_barang in stok_gudang:
            del stok_gudang[nama_barang]
            print(f"Barang '{nama_barang}' berhasil dihapus dari gudang.")
        else:
            print("Barang tidak ditemukan di dalam stok gudang.")


def main():
    stok_gudang = {
        'susu': 5,
        'daging ayam': 15,
        'daging sapi': 5,
        'daging kambing': 10,
        'apel': 10,
        'semangka': 15,
        'kangkung': 15,
        'bayam': 5
    }
    while True:
        print("\n=== APLIKASI STOK GUDANG ===")
        print("1. Tampilkan Stok Barang")
        print("2. Tampilkan Stok Barang Berdasarkan Nama Spesifik")
        print("3. Tampilkan Stok Barang yang Mengandung Nama")
        print("4. Tampilkan Stok Barang dengan Jumlah Stok Tertentu")
        print("5. Tambah Barang")
        print("6. Kurangi Stok")
        print("7. Hapus Barang")
        print("8. Keluar Program")
        pilihan = input("Masukkan pilihan [1/2/3/4/5/6/7/8]: ")

        if pilihan == "1":
            tampilkan_stok(stok_gudang)
        elif pilihan == "2":
            nama_barang = input("Masukkan nama barang: ")
            tampilkan_stok(stok_gudang, nama_barang)
        elif pilihan == "3":
            nama_kata_kunci = input("Masukkan kata kunci nama barang: ")
            tampilkan_stok_mengandung_nama(stok_gudang, nama_kata_kunci)
        elif pilihan == "4":
            jumlah_stok = input("Masukkan jumlah stok: ")
            tampilkan_stok_jumlah_tertentu(stok_gudang, jumlah_stok)
        elif pilihan == "5":
            tambah_barang(stok_gudang)
        elif pilihan == "6":
            kurangi_stok(stok_gudang)
        elif pilihan == "7":
            hapus_barang(stok_gudang)
        elif pilihan == "8":
            print("Terima kasih telah menggunakan aplikasi Stok Gudang.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang valid.")


if __name__ == '__main__':
    main()
