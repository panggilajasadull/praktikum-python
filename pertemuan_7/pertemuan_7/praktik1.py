import csv

file = None

try:
    # Membuka file CSV
    file = open("data_mahasiswa.csv", mode="r", newline="", encoding="utf-8")

    # Membaca isi file CSV
    reader = csv.DictReader(file)
    data_mahasiswa = list(reader)

    # Memeriksa dan memvalidasi data
    for mahasiswa in data_mahasiswa:
        if (
            not mahasiswa.get("nim")
            or not mahasiswa.get("nama")
            or not mahasiswa.get("nilai")
        ):
            raise ValueError("Terdapat data mahasiswa yang kosong.")

        # Memastikan nilai dapat dikonversi menjadi angka
        mahasiswa["nilai"] = int(mahasiswa["nilai"])

except FileNotFoundError:
    print("Error: File data_mahasiswa.csv tidak ditemukan.")

except csv.Error as e:
    print("Error saat membaca file CSV:", e)

except ValueError as e:
    print("Error pada data mahasiswa:", e)

else:
    # Dijalankan jika proses membaca dan validasi berhasil
    print("Data mahasiswa berhasil dibaca!")
    print("Jumlah mahasiswa:", len(data_mahasiswa))

    print("\nDaftar Mahasiswa:")
    for mahasiswa in data_mahasiswa:
        print(
            "NIM:",
            mahasiswa["nim"],
            "| Nama:",
            mahasiswa["nama"],
            "| Nilai:",
            mahasiswa["nilai"],
        )

finally:
    # Memastikan file ditutup
    if file is not None:
        file.close()
        print("\nFile berhasil ditutup.")

    print("Program selesai dijalankan.")
