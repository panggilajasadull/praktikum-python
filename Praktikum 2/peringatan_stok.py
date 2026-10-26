BATAS_AMAN = 20
BATAS_RENDAH = 10

inventaris = [
    {"kode": "B001", "nama": "Buku Python",       "stok": 45, "harga": 85000},
    {"kode": "B002", "nama": "Buku Database",     "stok": 12, "harga": 95000},
    {"kode": "B003", "nama": "Flashdisk 16GB",    "stok": 5,  "harga": 50000},
    {"kode": "B004", "nama": "Kabel USB",         "stok": 0,  "harga": 25000},
    {"kode": "B005", "nama": "Mouse Wireless",    "stok": 18, "harga": 120000},
    {"kode": "B006", "nama": "Keyboard Mekanik",  "stok": 30, "harga": 350000},
    {"kode": "B007", "nama": "Headset kabel",     "stok": 10, "harga": 150000},
    {"kode": "B008", "nama": "Kertas A4 (rim)",   "stok": 0,  "harga": 55000},
    {"kode": "B009", "nama": "Spidol Whiteboard", "stok": 21, "harga": 12000},
    {"kode": "B010", "nama": "Webcam HD",         "stok": 3,  "harga": 275000},
]


def cek_status_stok(stok):
    """Kembalikan (status, prioritas, rekomendasi)."""
    if stok == 0:
        return "HABIS", "CRITICAL", "Restock segera"
    elif stok <= BATAS_RENDAH:
        return "RENDAH", "HIGH", "Restock 1-3 hari"
    elif stok <= BATAS_AMAN:
        return "PERINGATAN", "MEDIUM", "Restock 1-2 minggu"
    else:
        return "AMAN", "LOW", "Mencukupi"


def main():
    jumlah_status = {"HABIS": 0, "RENDAH": 0, "PERINGATAN": 0, "AMAN": 0}
    total_nilai = 0
    total_unit = 0
    perlu_restock = 0  # status HABIS atau RENDAH

    print("=" * 84)
    print("LAPORAN STATUS INVENTARIS")
    print("=" * 84)
    print(f"{'Kode':<6} {'Nama Barang':<18} {'Stok':>4} {'Nilai (Rp)':>11}  "
        f"{'Status':<11} {'Prioritas':<9} Rekomendasi")
    print("-" * 84)

    for item in inventaris:
        status, prioritas, rekomendasi = cek_status_stok(item["stok"])
        nilai = item["stok"] * item["harga"]

        jumlah_status[status] += 1
        total_nilai += nilai
        total_unit += item["stok"]
        if prioritas in ("CRITICAL", "HIGH"):
            perlu_restock += 1

        print(f"{item['kode']:<6} {item['nama']:<18} {item['stok']:>4} "
            f"{nilai:>11,}  {status:<11} {prioritas:<9} {rekomendasi}")

    jumlah_item = len(inventaris)
    item_terendah = min(inventaris, key=lambda x: x["stok"])
    item_termahal = max(inventaris, key=lambda x: x["stok"] * x["harga"])

    print("\n" + "=" * 84)
    print("RINGKASAN STATISTIK")
    print("=" * 84)
    for status, jml in jumlah_status.items():
        persen = jml / jumlah_item * 100
        print(f"Status {status:<11}: {jml:>2} item ({persen:>5.1f}%)")
    print("-" * 84)
    print(f"Total jenis barang           : {jumlah_item}")
    print(f"Total unit di gudang         : {total_unit:,}")
    print(f"Rata-rata stok per item      : {total_unit / jumlah_item:.1f} unit")
    print(f"Total nilai inventaris       : Rp{total_nilai:,}")
    print(f"Item perlu restock segera    : {perlu_restock} dari {jumlah_item} item")
    print(f"Stok paling sedikit          : {item_terendah['nama']} "
        f"({item_terendah['stok']} unit)")
    print(f"Nilai persediaan terbesar    : {item_termahal['nama']} "
          f"(Rp{item_termahal['stok'] * item_termahal['harga']:,})")


if __name__ == "__main__":
    main()
