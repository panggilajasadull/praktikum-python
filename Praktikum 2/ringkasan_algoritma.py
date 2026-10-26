IPK_MIN_AKTIF, IPK_MIN_PERINGATAN, SKS_MIN = 3.0, 2.5, 18
BATAS_RENDAH, BATAS_AMAN = 10, 20

# ---------- Data simulasi ----------
daftar_mhs = [
    {"nama": "Pajar",  "ipk": 3.52, "sks": 20},
    {"nama": "Fauzan",  "ipk": 1.75, "sks": 15},
    {"nama": "Fajar",  "ipk": 1.30, "sks": 12},
    {"nama": "Naufal",   "ipk": 3.00, "sks": 18},
    {"nama": "Sona", "ipk": 2.00, "sks": 18},
    {"nama": "Ajis",  "ipk": 3.45, "sks": 16},
]

SPP = 5_000_000
# (nama, ipk, anak_karyawan, tepat_waktu)
daftar_bayar = [
    ("Pajar",  3.50, True,  False),
    ("Naufal",  2.80, False, True),
    ("Ajis",  3.20, False, False),
    ("Sona", 2.00, False, False),
]

inventaris = [
    {"kode": "B001", "stok": 45}, {"kode": "B002", "stok": 12},
    {"kode": "B003", "stok": 5},  {"kode": "B004", "stok": 0},
    {"kode": "B005", "stok": 18}, {"kode": "B006", "stok": 30},
    {"kode": "B007", "stok": 10}, {"kode": "B008", "stok": 0},
    {"kode": "B009", "stok": 21}, {"kode": "B010", "stok": 3},
]


# ---------- Fungsi aturan bisnis ----------
def tentukan_status(ipk, sks):
    if ipk >= IPK_MIN_AKTIF and sks >= SKS_MIN:
        return "Aktif"
    elif ipk >= IPK_MIN_PERINGATAN:
        return "Peringatan"   # termasuk IPK >= 2.0 tetapi SKS < 18
    return "Tidak Aktif"


def hitung_total_diskon(ipk, is_ak, is_tw):
    if is_ak:
        utama = 25
    elif ipk >= 3.8:
        utama = 20
    elif ipk >= 3.5:
        utama = 15
    elif ipk >= 3.0:
        utama = 10
    else:
        utama = 0
    return utama + (5 if is_tw else 0)


def butuh_restock(stok):
    """Perlu restock segera: stok HABIS (0) atau RENDAH (1-10)."""
    return stok <= BATAS_RENDAH


def garis(panjang=52):
    print("-" * panjang)


def main():
    # (a) status mahasiswa
    hitung = {"Aktif": 0, "Peringatan": 0, "Tidak Aktif": 0}
    for m in daftar_mhs:
        hitung[tentukan_status(m["ipk"], m["sks"])] += 1
    total_mhs = len(daftar_mhs)
    aktif = hitung["Aktif"]
    bukan_aktif = total_mhs - aktif

    print("=" * 52)
    print("RINGKASAN ALGORITMA")
    print("=" * 52)
    print("\n(a) STATUS MAHASISWA")
    garis()
    print(f"{'Status':<20} {'Jumlah':>8} {'Persentase':>12}")
    garis()
    for status, jml in hitung.items():
        print(f"{status:<20} {jml:>8} {jml / total_mhs * 100:>11.1f}%")
    garis()
    print(f"{'Aktif':<20} {aktif:>8} {aktif / total_mhs * 100:>11.1f}%")
    print(f"{'Bukan Aktif':<20} {bukan_aktif:>8} "
          f"{bukan_aktif / total_mhs * 100:>11.1f}%")
    garis()

    # (b) rata-rata diskon
    total_persen = 0
    total_potongan = 0
    print("\n(b) DISKON BIAYA KULIAH (SPP Rp5,000,000)")
    garis()
    print(f"{'Mahasiswa':<12} {'Diskon':>8} {'Potongan (Rp)':>16}")
    garis()
    for nama, ipk, is_ak, is_tw in daftar_bayar:
        persen = hitung_total_diskon(ipk, is_ak, is_tw)
        potongan = SPP * persen // 100
        total_persen += persen
        total_potongan += potongan
        print(f"{nama:<12} {persen:>7}% {potongan:>16,}")
    n = len(daftar_bayar)
    garis()
    rata_persen = total_persen / n
    rata_potongan = total_potongan / n
    print(f"{'Rata-rata':<12} {rata_persen:>7.2f}% {rata_potongan:>16,.0f}")
    garis()

    # (c) restock
    perlu = sum(1 for item in inventaris if butuh_restock(item["stok"]))
    rencana = sum(1 for item in inventaris
                if BATAS_RENDAH < item["stok"] <= BATAS_AMAN)
    total_item = len(inventaris)
    print("\n(c) INVENTARIS")
    garis()
    print(f"{'Kategori':<30} {'Jumlah':>6} {'Persentase':>10}")
    garis()
    print(f"{'Perlu restock (stok <= 10)':<30} {perlu:>6} "
          f"{perlu / total_item * 100:>9.1f}%")
    print(f"{'Perlu direncanakan (11-20)':<30} {rencana:>6} "
          f"{rencana / total_item * 100:>9.1f}%")
    print(f"{'Total item':<30} {total_item:>6} {'100.0%':>10}")
    garis()


if __name__ == "__main__":
    main()
