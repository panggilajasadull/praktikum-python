JUMLAH_MAHASISWA = 5
IPK_MIN_AKTIF = 2.0
IPK_MIN_PERINGATAN = 1.5
SKS_MIN = 18
SKS_MAKS = 24


# ---------- Fungsi bantu input + validasi ----------
def baca_teks(prompt):
    """Minta teks sampai tidak kosong."""
    while True:
        nilai = input(prompt).strip()
        if nilai:
            return nilai
        print("  Error: isian tidak boleh kosong.")


def baca_nim(prompt, nim_terpakai):
    """Minta NIM (hanya angka, tidak boleh duplikat)."""
    while True:
        nim = input(prompt).strip()
        if not (nim.isascii() and nim.isdigit()):
            print("  Error: NIM harus berisi angka saja.")
        elif nim in nim_terpakai:
            print("  Error: NIM sudah pernah dimasukkan.")
        else:
            return nim


def baca_float(prompt, minimum, maksimum):
    """Minta bilangan desimal dalam rentang [minimum, maksimum]."""
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
    """Minta bilangan bulat dalam rentang [minimum, maksimum]."""
    while True:
        try:
            nilai = int(input(prompt))
        except ValueError:
            print("  Error: masukkan bilangan bulat yang valid.")
            continue
        if minimum <= nilai <= maksimum:
            return nilai
        print(f"  Error: nilai harus antara {minimum} dan {maksimum}.")


# ---------- Logika aturan bisnis ----------
def tentukan_status(ipk, sks):
    """Kembalikan (status, keterangan) berdasarkan IPK dan SKS."""
    if ipk >= IPK_MIN_AKTIF and sks >= SKS_MIN:
        return "Aktif", "Lanjut semester depan"
    elif ipk >= IPK_MIN_AKTIF:
        return "Peringatan", "SKS kurang dari 18"
    elif ipk >= IPK_MIN_PERINGATAN:
        return "Peringatan", "Konsultasi dosen PA"
    else:
        return "Tidak Aktif", "Risiko drop out"


def main():
    daftar_mhs = []
    nim_terpakai = set()

    print("=== Input Data Mahasiswa ===")
    for i in range(1, JUMLAH_MAHASISWA + 1):
        print(f"\nMahasiswa ke-{i}")
        nim = baca_nim("NIM  :", nim_terpakai)
        nim_terpakai.add(nim)
        nama = baca_teks("Nama :")
        ipk = baca_float("IPK (0.0-4.0) :", 0.0, 4.0)
        sks = baca_int("SKS (0-24)    :", 0, SKS_MAKS)
        daftar_mhs.append({"nim": nim, "nama": nama, "ipk": ipk, "sks": sks})

    # Laporan
    jumlah = {"Aktif": 0, "Peringatan": 0, "Tidak Aktif": 0}
    print("\n" + "=" * 78)
    print("LAPORAN STATUS MAHASISWA")
    print("=" * 78)
    print(f"{'No':<3} {'NIM':<12} {'Nama':<14} {'IPK':>5} {'SKS':>4}  "
        f"{'Status':<12} Keterangan")
    print("-" * 78)
    for no, mhs in enumerate(daftar_mhs, start=1):
        status, ket = tentukan_status(mhs["ipk"], mhs["sks"])
        jumlah[status] += 1
        print(f"{no:<3} {mhs['nim']:<12} {mhs['nama']:<14} "
            f"{mhs['ipk']:>5.2f} {mhs['sks']:>4}  {status:<12} {ket}")
    print("-" * 78)
    print("Ringkasan: " + " | ".join(f"{k}: {v}" for k, v in jumlah.items()))


if __name__ == "__main__":
    main()
