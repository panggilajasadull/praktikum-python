class PerpustakaanError(Exception):
    """Exception dasar untuk sistem perpustakaan."""


class BukuNotFoundError(PerpustakaanError):
    """Exception ketika buku tidak ditemukan."""


class BukuTidakTersediaError(PerpustakaanError):
    """Exception ketika buku sedang dipinjam."""


class AnggotaNotFoundError(PerpustakaanError):
    """Exception ketika anggota tidak ditemukan."""


daftar_buku = {
    "B001": {"judul": "Belajar Python", "tersedia": True},
    "B002": {"judul": "Dasar Pemrograman", "tersedia": False},
}

daftar_anggota = ["A001", "A002"]


def pinjam_buku(kode_buku, id_anggota):
    if kode_buku not in daftar_buku:
        raise BukuNotFoundError("Buku tidak ditemukan.")

    if id_anggota not in daftar_anggota:
        raise AnggotaNotFoundError("Anggota tidak ditemukan.")

    if not daftar_buku[kode_buku]["tersedia"]:
        raise BukuTidakTersediaError("Buku sedang dipinjam.")

    daftar_buku[kode_buku]["tersedia"] = False
    return "Peminjaman buku berhasil."


if __name__ == "__main__":
    try:
        print(pinjam_buku("B001", "A001"))
    except PerpustakaanError as error:
        print("Terjadi kesalahan:", error)

    try:
        print(pinjam_buku("B999", "A001"))
    except PerpustakaanError as error:
        print("Terjadi kesalahan:", error)

    try:
        print(pinjam_buku("B002", "A001"))
    except PerpustakaanError as error:
        print("Terjadi kesalahan:", error)

    try:
        print(pinjam_buku("B001", "A999"))
    except PerpustakaanError as error:
        print("Terjadi kesalahan:", error)
