TAHUN_MIN, TAHUN_MAKS = 2000, 2037
IPK_MIN, IPK_MAKS = 0.0, 4.0
SKS_MIN, SKS_MAKS = 0, 24
SEMESTER_MIN, SEMESTER_MAKS = 1, 14


def validasi_nim(nim):
    """10 digit angka, 4 digit pertama = tahun masuk 2000-2037."""
    nim = nim.strip()
    if nim == "":
        return ["NIM tidak boleh kosong"]
    # isascii() ikut dicek: karakter seperti '²' lolos isdigit() tetapi
    # bukan angka 0-9 dan membuat int() gagal.
    if not (nim.isascii() and nim.isdigit()):
        return ["NIM harus berisi angka 0-9 saja"]
    if len(nim) != 11:
        return [f"NIM harus tepat 11 digit (terdeteksi {len(nim)} digit)"]
    tahun = int(nim[:4])
    if not TAHUN_MIN <= tahun <= TAHUN_MAKS:
        return [f"Tahun masuk pada NIM ({tahun}) harus {TAHUN_MIN}-{TAHUN_MAKS}"]
    return []


def validasi_ipk(ipk_teks):
    """IPK harus angka dalam rentang 0.0 - 4.0."""
    try:
        ipk = float(ipk_teks)
    except ValueError:
        return ["IPK harus berupa angka (contoh: 3.25)"]
    # Ditulis sebagai "not (a <= x <= b)" supaya NaN pun ditolak.
    if not IPK_MIN <= ipk <= IPK_MAKS:
        return [f"IPK harus antara {IPK_MIN} dan {IPK_MAKS}"]
    return []


def validasi_sks(sks_teks):
    """SKS harus bilangan bulat 0 - 24."""
    try:
        sks = int(sks_teks)
    except ValueError:
        return ["SKS harus berupa bilangan bulat"]
    if not SKS_MIN <= sks <= SKS_MAKS:
        return [f"SKS harus antara {SKS_MIN} dan {SKS_MAKS}"]
    return []


def validasi_semester(semester_teks):
    """Semester harus bilangan bulat 1 - 14."""
    try:
        semester = int(semester_teks)
    except ValueError:
        return ["Semester harus berupa bilangan bulat"]
    if not SEMESTER_MIN <= semester <= SEMESTER_MAKS:
        return [f"Semester harus antara {SEMESTER_MIN} dan {SEMESTER_MAKS}"]
    return []


def validasi_data_mahasiswa(nim, ipk, sks, semester):
    """Gabungkan semua validasi; kembalikan list error (kosong = valid)."""
    error_list = []
    for label, hasil in (
        ("NIM", validasi_nim(nim)),
        ("IPK", validasi_ipk(ipk)),
        ("SKS", validasi_sks(sks)),
        ("Semester", validasi_semester(semester)),
    ):
        for pesan in hasil:
            error_list.append(f"[{label}] {pesan}")
    return error_list


def main():
    print("=== Validasi Data Mahasiswa ===")
    while True:
        nim = input("\nNIM      : ")
        ipk = input("IPK      : ")
        sks = input("SKS      : ")
        semester = input("Semester : ")

        errors = validasi_data_mahasiswa(nim, ipk, sks, semester)
        print("\nHasil validasi:")
        if not errors:
            print("  DATA VALID - semua isian memenuhi aturan.")
        else:
            print(f"  DATA TIDAK VALID - {len(errors)} kesalahan ditemukan:")
            for no, pesan in enumerate(errors, start=1):
                print(f"  {no}. {pesan}")

        lagi = input("\nValidasi data lain? (y/n): ").strip().lower()
        if lagi != "y":
            print("Selesai.")
            break


if __name__ == "__main__":
    main()
