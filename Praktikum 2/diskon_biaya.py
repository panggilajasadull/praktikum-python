DISKON_ANAK_KARYAWAN = 25   # persen
DISKON_PRESTASI_TINGGI = 20  # IPK >= 3.8
DISKON_PRESTASI_BAIK = 15    # IPK >= 3.5
DISKON_MEMUASKAN = 10        # IPK >= 3.0
DISKON_TEPAT_WAKTU = 5


def baca_int(prompt, minimum, maksimum):
    while True:
        try:
            nilai = int(input(prompt))
        except ValueError:
            print("  Error: masukkan bilangan bulat tanpa titik/koma "
                "(contoh: 5000000).")
            continue
        if minimum <= nilai <= maksimum:
            return nilai
        print(f"  Error: nilai harus antara {minimum:,} dan {maksimum:,}.")


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


def baca_ya_tidak(prompt):
    while True:
        jawab = input(prompt).strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  Error: jawab dengan 'y' atau 'n'.")


def hitung_diskon(ipk, is_anak_karyawan, is_tepat_waktu):
    """Kembalikan (kategori, diskon_utama, diskon_tambahan) dalam persen."""
    if is_anak_karyawan:
        kategori, utama = "Anak Karyawan", DISKON_ANAK_KARYAWAN
    elif ipk >= 3.8:
        kategori, utama = "Prestasi Tinggi (IPK >= 3.8)", DISKON_PRESTASI_TINGGI
    elif ipk >= 3.5:
        kategori, utama = "Prestasi Baik (IPK >= 3.5)", DISKON_PRESTASI_BAIK
    elif ipk >= 3.0:
        kategori, utama = "IPK Memuaskan (IPK >= 3.0)", DISKON_MEMUASKAN
    else:
        kategori, utama = "Tidak ada diskon utama", 0
    tambahan = DISKON_TEPAT_WAKTU if is_tepat_waktu else 0
    return kategori, utama, tambahan


def hitung_potongan(biaya, persen):
    """Potongan dalam rupiah, dibulatkan ke rupiah terdekat (half-up)."""
    return (biaya * persen + 50) // 100


def main():
    print("=== Kalkulator Diskon Biaya Kuliah ===")
    biaya_spp = baca_int("Biaya SPP (Rp)            : ", 1, 1_000_000_000)
    is_ak = baca_ya_tidak("Anak karyawan? (y/n)      : ")
    ipk = baca_float("IPK (0.0-4.0)             : ", 0.0, 4.0)
    is_tw = baca_ya_tidak("Bayar tepat waktu? (y/n)  : ")

    kategori, utama, tambahan = hitung_diskon(ipk, is_ak, is_tw)
    total = utama + tambahan
    potongan = hitung_potongan(biaya_spp, total)
    biaya_final = biaya_spp - potongan

    print("\n=== Rincian Diskon ===")
    print(f"Kategori diskon utama : {kategori}")
    print(f"Diskon utama          : {utama}%")
    print(f"Diskon tepat waktu    : {tambahan}%")
    print(f"Total diskon berlaku  : {total}%")
    print("-" * 36)
    print(f"Biaya SPP             : Rp{biaya_spp:,}")
    print(f"Potongan biaya        : Rp{potongan:,}")
    print(f"Biaya final dibayar   : Rp{biaya_final:,}")


if __name__ == "__main__":
    main()
