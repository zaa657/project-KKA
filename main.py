data_transaksi = []


def tampilkan_header():
    print("=" * 45)
    print("     APLIKASI CATATAN KEUANGAN HARIAN")
    print("=" * 45)


def tampilkan_menu():
    print("\nMenu Utama")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Lihat Total Saldo")
    print("4. Lihat Riwayat Transaksi")
    print("5. Hapus Transaksi")
    print("6. Reset Semua Data")
    print("7. Keluar")


def input_uang(pesan):
    while True:
        try:
            jumlah_uang = int(input(pesan))

            if jumlah_uang > 0:
                return jumlah_uang
            else:
                print("Jumlah uang harus lebih dari 0.")

        except ValueError:
            print("Input harus berupa angka.")


def input_keterangan():
    while True:
        keterangan = input("Masukkan keterangan: ")

        if keterangan.strip() != "":
            return keterangan
        else:
            print("Keterangan tidak boleh kosong.")


def tambah_pemasukan():
    print("\nTambah Pemasukan")
    keterangan = input_keterangan()
    jumlah_uang = input_uang("Masukkan jumlah pemasukan: Rp")

    transaksi_baru = {
        "jenis": "Pemasukan",
        "keterangan": keterangan,
        "jumlah": jumlah_uang
    }

    data_transaksi.append(transaksi_baru)
    print("Pemasukan berhasil ditambahkan.")


def tambah_pengeluaran():
    print("\nTambah Pengeluaran")
    keterangan = input_keterangan()
    jumlah_uang = input_uang("Masukkan jumlah pengeluaran: Rp")

    transaksi_baru = {
        "jenis": "Pengeluaran",
        "keterangan": keterangan,
        "jumlah": jumlah_uang
    }

    data_transaksi.append(transaksi_baru)
    print("Pengeluaran berhasil ditambahkan.")


def hitung_total(jenis_transaksi):
    total = 0

    for transaksi in data_transaksi:
        if transaksi["jenis"] == jenis_transaksi:
            total += transaksi["jumlah"]

    return total


def lihat_total_saldo():
    total_pemasukan = hitung_total("Pemasukan")
    total_pengeluaran = hitung_total("Pengeluaran")
    saldo_akhir = total_pemasukan - total_pengeluaran

    print("\nRingkasan Keuangan")
    print("-" * 45)
    print(f"Total Pemasukan   : Rp{total_pemasukan}")
    print(f"Total Pengeluaran : Rp{total_pengeluaran}")
    print(f"Sisa Uang         : Rp{saldo_akhir}")

    if saldo_akhir > 0:
        print("Status            : Keuangan masih aman.")
    elif saldo_akhir == 0:
        print("Status            : Uang habis.")
    else:
        print("Status            : Pengeluaran lebih besar dari pemasukan.")


def lihat_riwayat_transaksi():
    if len(data_transaksi) == 0:
        print("\nBelum ada transaksi.")
        return

    print("\nRiwayat Transaksi")
    print("-" * 45)

    for nomor, transaksi in enumerate(data_transaksi, start=1):
        print(f"{nomor}. {transaksi['jenis']}")
        print(f"   Keterangan : {transaksi['keterangan']}")
        print(f"   Jumlah     : Rp{transaksi['jumlah']}")


def hapus_transaksi():
    lihat_riwayat_transaksi()

    if len(data_transaksi) == 0:
        return

    nomor_transaksi = input_uang("\nPilih nomor transaksi yang ingin dihapus: ")

    if nomor_transaksi >= 1 and nomor_transaksi <= len(data_transaksi):
        transaksi_dihapus = data_transaksi.pop(nomor_transaksi - 1)
        print(f"Transaksi '{transaksi_dihapus['keterangan']}' berhasil dihapus.")
    else:
        print("Nomor transaksi tidak ditemukan.")


def reset_semua_data():
    if len(data_transaksi) == 0:
        print("\nData transaksi masih kosong.")
        return

    konfirmasi = input("Yakin ingin menghapus semua data? y/n: ")

    if konfirmasi.lower() == "y" or konfirmasi.lower() == "ya":
        data_transaksi.clear()
        print("Semua data berhasil dihapus.")
    else:
        print("Reset data dibatalkan.")


def jalankan_program():
    while True:
        tampilkan_header()
        tampilkan_menu()

        pilihan = input("Pilih menu 1-7: ")

        if pilihan == "1":
            tambah_pemasukan()
        elif pilihan == "2":
            tambah_pengeluaran()
        elif pilihan == "3":
            lihat_total_saldo()
        elif pilihan == "4":
            lihat_riwayat_transaksi()
        elif pilihan == "5":
            hapus_transaksi()
        elif pilihan == "6":
            reset_semua_data()
        elif pilihan == "7":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")

        input("\nTekan Enter untuk lanjut...")


jalankan_program()