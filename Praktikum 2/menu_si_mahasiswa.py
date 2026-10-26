IPK_MIN_AKTIF = 3.0
IPK_MIN_PERINGATAN = 2.5
SKS_MIN = 18

DISKON_ANAK_KARYAWAN = 25
DISKON_PRESTASI_TINGGI = 20
DISKON_PRESTASI_BAIK = 15
DISKON_MEMUASKAN = 10
DISKON_TEPAT_WAKTU = 5

BATAS_AMAN = 20
BATAS_RENDAH = 10

inventaris = [
    {"kode": "B001", "nama": "Buku Python",    "stok": 45, "harga": 85000},
    {"kode": "B002", "nama": "Buku Database",  "stok": 12, "harga": 95000},
    {"kode": "B003", "nama": "Flashdisk 16GB", "stok": 5,  "harga": 50000},
    {"kode": "B004", "nama": "Headset kabel",  "stok": 0,  "harga": 25000},
    {"kode": "B005", "nama": "Mouse Wireless", "stok": 18, "harga": 120000},
]


# ---------------- Fungsi bantu input ----------------
def baca_float(prompt, minimum, maksimum):
    while True:
        try:
            nilai = float(input(prompt))
        except ValueError:
            print("  Error: masukkan angka yang valid.")
            continue
        if minimum <= nilai <= maksimum:
            return nilai
        print(f"  Error: nilai harus antara {minimum} dan {maksimum}.")


def baca_int(prompt, minimum, maksimum):
    while True:
        try:
            nilai = int(input(prompt))
        except ValueError:
            print("  Error: masukkan bilangan bulat yang valid.")
            continue
        if minimum <= nilai <= maksimum:
            return nilai
        print(f"  Error: nilai harus antara {minimum:,} dan {maksimum:,}.")


def baca_ya_tidak(prompt):
    while True:
        jawab = input(prompt).strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  Error: jawab dengan 'y' atau 'n'.")


def baca_pilihan(prompt, pilihan_valid):
    while True:
        pilihan = input(prompt).strip()
        if pilihan in pilihan_valid:
            return pilihan
        print(f"  Error: pilih salah satu dari {pilihan_valid}.")


# ---------------- Logika bisnis ----------------
def tentukan_status(ipk, sks, is_cuti):
    if is_cuti:
        return "Cuti", "Lakukan administrasi cuti"
    if ipk >= IPK_MIN_AKTIF and sks >= SKS_MIN:
        return "Aktif", "Lanjut semester depan"
    elif ipk >= IPK_MIN_AKTIF:
        return "Peringatan", "SKS kurang dari 18"
    elif ipk >= IPK_MIN_PERINGATAN:
        return "Peringatan", "Konsultasi dosen PA"
    return "Tidak Aktif", "Risiko drop out"


def hitung_diskon(ipk, is_anak_karyawan, is_tepat_waktu):
    if is_anak_karyawan:
        kategori, utama = "Anak Karyawan", DISKON_ANAK_KARYAWAN
    elif ipk >= 3.8:
        kategori, utama = "Prestasi Tinggi", DISKON_PRESTASI_TINGGI
    elif ipk >= 3.5:
        kategori, utama = "Prestasi Baik", DISKON_PRESTASI_BAIK
    elif ipk >= 3.0:
        kategori, utama = "IPK Memuaskan", DISKON_MEMUASKAN
    else:
        kategori, utama = "Tidak ada diskon utama", 0
    tambahan = DISKON_TEPAT_WAKTU if is_tepat_waktu else 0
    return kategori, utama, tambahan


def cek_status_stok(stok):
    if stok == 0:
        return "HABIS", "CRITICAL", "Restock segera"
    elif stok <= BATAS_RENDAH:
        return "RENDAH", "HIGH", "Restock 1-3 hari"
    elif stok <= BATAS_AMAN:
        return "PERINGATAN", "MEDIUM", "Restock 1-2 minggu"
    return "AMAN", "LOW", "Mencukupi"


# ---------------- Submenu ----------------
def menu_status_mahasiswa():
    print("\n--- Cek Status Mahasiswa ---")
    nama = input("Nama mahasiswa : ").strip() or "(tanpa nama)"
    ipk = baca_float("IPK (0.0-4.0)   : ", 0.0, 4.0)
    sks = baca_int("SKS (0-24)      : ", 0, 24)
    is_cuti = baca_ya_tidak("Sedang cuti? (y/n): ")
    status, saran = tentukan_status(ipk, sks, is_cuti)
    print(f"\nHasil untuk {nama}")
    print(f"  Status     : {status}")
    print(f"  Rekomendasi: {saran}")


def menu_diskon():
    print("\n--- Hitung Diskon Biaya Kuliah ---")
    biaya = baca_int("Biaya SPP (Rp)           : ", 1, 1_000_000_000)
    is_ak = baca_ya_tidak("Anak karyawan? (y/n)     : ")
    ipk = baca_float("IPK (0.0-4.0)            : ", 0.0, 4.0)
    is_tw = baca_ya_tidak("Bayar tepat waktu? (y/n) : ")
    kategori, utama, tambahan = hitung_diskon(ipk, is_ak, is_tw)
    total = utama + tambahan
    potongan = (biaya * total + 50) // 100  # bulatkan half-up, tanpa float
    print(f"\n  Kategori      : {kategori}")
    print(f"  Diskon utama  : {utama}% + tepat waktu {tambahan}% = {total}%")
    print(f"  Potongan      : Rp{potongan:,}")
    print(f"  Biaya final   : Rp{biaya - potongan:,}")


def tampilkan_laporan_stok():
    print(f"\n{'Kode':<6} {'Nama Barang':<16} {'Stok':>4}  "
        f"{'Status':<11} {'Prioritas':<9}")
    print("-" * 52)
    for item in inventaris:
        status, prioritas, _ = cek_status_stok(item["stok"])
        print(f"{item['kode']:<6} {item['nama']:<16} {item['stok']:>4}  "
            f"{status:<11} {prioritas:<9}")


def menu_stok():
    print("\n--- Cek Peringatan Stok ---")
    print("1. Laporan seluruh inventaris")
    print("2. Cek satu barang (berdasarkan kode)")
    print("3. Cek stok manual (input jumlah stok)")
    pilihan = baca_pilihan("Pilih (1/2/3): ", ["1", "2", "3"])

    if pilihan == "1":
        tampilkan_laporan_stok()
    elif pilihan == "2":
        kode_valid = [item["kode"] for item in inventaris]
        kode = input(f"Kode barang {kode_valid}: ").strip().upper()
        while kode not in kode_valid:
            print("  Error: kode barang tidak ditemukan.")
            kode = input(f"Kode barang {kode_valid}: ").strip().upper()
        for item in inventaris:
            if item["kode"] == kode:
                status, prioritas, saran = cek_status_stok(item["stok"])
                print(f"\n  {item['nama']}: stok {item['stok']} unit")
                print(f"  Status {status} [{prioritas}] -> {saran}")
                break
    else:
        stok = baca_int("Jumlah stok (0-100000): ", 0, 100000)
        status, prioritas, saran = cek_status_stok(stok)
        print(f"\n  Status {status} [{prioritas}] -> {saran}")


# ---------------- Program utama ----------------
def main():
    print("=== Sistem Informasi Mahasiswa ===")
    while True:
        print("\nMenu:")
        print("1. Cek Status Mahasiswa")
        print("2. Hitung Diskon Biaya")
        print("3. Cek Peringatan Stok")
        print("0. Keluar")
        pilihan = baca_pilihan("Pilih menu (1/2/3/0): ", ["1", "2", "3", "0"])

        if pilihan == "1":
            menu_status_mahasiswa()
        elif pilihan == "2":
            menu_diskon()
        elif pilihan == "3":
            menu_stok()
        else:
            print("Terima kasih.")
            break


if __name__ == "__main__":
    main()
