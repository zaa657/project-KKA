daftar_tugas = []


def tampilkan_header():
    print("=" * 40)
    print("      APLIKASI TO DO LIST SISWA")
    print("=" * 40)


def tampilkan_menu():
    print("\nMenu Utama")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")


def tambah_tugas():
    nama_tugas = input("Masukkan nama tugas: ")

    if nama_tugas.strip() == "":
        print("Nama tugas tidak boleh kosong.")
        return

    tugas_baru = {
        "nama": nama_tugas,
        "status": "Belum selesai"
    }

    daftar_tugas.append(tugas_baru)
    print("Tugas berhasil ditambahkan.")


def lihat_tugas():
    if len(daftar_tugas) == 0:
        print("Belum ada tugas.")
        return

    print("\nDaftar Tugas")
    print("-" * 40)

    for nomor, tugas in enumerate(daftar_tugas, start=1):
        print(f"{nomor}. {tugas['nama']} - {tugas['status']}")


def tandai_selesai():
    lihat_tugas()

    if len(daftar_tugas) == 0:
        return

    try:
        nomor_tugas = int(input("Pilih nomor tugas yang selesai: "))

        if nomor_tugas >= 1 and nomor_tugas <= len(daftar_tugas):
            daftar_tugas[nomor_tugas - 1]["status"] = "Selesai"
            print("Tugas berhasil ditandai selesai.")
        else:
            print("Nomor tugas tidak ditemukan.")

    except ValueError:
        print("Input harus berupa angka.")


def hapus_tugas():
    lihat_tugas()

    if len(daftar_tugas) == 0:
        return

    try:
        nomor_tugas = int(input("Pilih nomor tugas yang ingin dihapus: "))

        if nomor_tugas >= 1 and nomor_tugas <= len(daftar_tugas):
            tugas_dihapus = daftar_tugas.pop(nomor_tugas - 1)
            print(f"Tugas '{tugas_dihapus['nama']}' berhasil dihapus.")
        else:
            print("Nomor tugas tidak ditemukan.")

    except ValueError:
        print("Input harus berupa angka.")


def jalankan_program():
    while True:
        tampilkan_header()
        tampilkan_menu()

        pilihan = input("Pilih menu 1-5: ")

        if pilihan == "1":
            tambah_tugas()
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            tandai_selesai()
        elif pilihan == "4":
            hapus_tugas()
        elif pilihan == "5":
            print("Terima kasih sudah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")

        input("\nTekan Enter untuk lanjut...")


jalankan_program()