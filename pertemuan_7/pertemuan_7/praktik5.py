"""
Praktik 5: Identifikasi Code Smell dan Refactoring

Contoh refactoring program pengelolaan nilai mahasiswa.
"""

# Konstanta agar tidak menggunakan magic number
BATAS_LULUS = 60


def hitung_rata_rata(nilai: list[float]) -> float:
    """Menghitung rata-rata nilai mahasiswa."""
    if not nilai:
        return 0.0

    return sum(nilai) / len(nilai)


def tentukan_status(rata_rata: float) -> str:
    """Menentukan status kelulusan mahasiswa."""
    if rata_rata >= BATAS_LULUS:
        return "LULUS"

    return "TIDAK LULUS"


def tampilkan_hasil(nama: str, nilai: list[float]) -> None:
    """Menampilkan hasil pengolahan nilai mahasiswa."""
    rata_rata = hitung_rata_rata(nilai)
    status = tentukan_status(rata_rata)

    print("\n=== HASIL NILAI MAHASISWA ===")
    print("Nama:", nama)
    print("Nilai:", nilai)
    print("Rata-rata:", round(rata_rata, 2))
    print("Status:", status)


def main() -> None:
    """Menjalankan program pengolahan nilai mahasiswa."""
    data_mahasiswa = [
        {"nama": "Andi", "nilai": [80, 85, 90]},
        {"nama": "Budi", "nilai": [50, 55, 60]},
        {"nama": "Citra", "nilai": [90, 95, 85]},
    ]

    for mahasiswa in data_mahasiswa:
        tampilkan_hasil(mahasiswa["nama"], mahasiswa["nilai"])


if __name__ == "__main__":
    main()
