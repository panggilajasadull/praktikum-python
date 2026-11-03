import unittest


def hitung_ipk(total_nilai, total_sks):
    if total_sks <= 0:
        raise ValueError("Total SKS harus lebih dari 0.")

    return total_nilai / total_sks


def validasi_nim(nim):
    return nim.isdigit() and len(nim) == 10


def konversi_nilai_huruf(nilai):
    if nilai < 0 or nilai > 100:
        raise ValueError("Nilai harus antara 0 sampai 100.")

    if nilai >= 85:
        return "A"
    elif nilai >= 80:
        return "B+"
    elif nilai >= 70:
        return "B"
    elif nilai >= 65:
        return "C+"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"


class TestFungsiAkademik(unittest.TestCase):

    def test_hitung_ipk(self):
        self.assertEqual(hitung_ipk(350, 100), 3.5)

    def test_hitung_ipk_sks_nol(self):
        with self.assertRaises(ValueError):
            hitung_ipk(350, 0)

    def test_validasi_nim_valid(self):
        self.assertTrue(validasi_nim("1234567890"))

    def test_validasi_nim_tidak_valid(self):
        self.assertFalse(validasi_nim("12345"))

    def test_validasi_nim_huruf(self):
        self.assertFalse(validasi_nim("12345ABCDE"))

    def test_nilai_a(self):
        self.assertEqual(konversi_nilai_huruf(90), "A")

    def test_nilai_b_plus(self):
        self.assertEqual(konversi_nilai_huruf(82), "B+")

    def test_nilai_b(self):
        self.assertEqual(konversi_nilai_huruf(75), "B")

    def test_nilai_c_plus(self):
        self.assertEqual(konversi_nilai_huruf(67), "C+")

    def test_nilai_c(self):
        self.assertEqual(konversi_nilai_huruf(62), "C")

    def test_nilai_d(self):
        self.assertEqual(konversi_nilai_huruf(55), "D")

    def test_nilai_e(self):
        self.assertEqual(konversi_nilai_huruf(40), "E")

    def test_nilai_di_luar_batas(self):
        with self.assertRaises(ValueError):
            konversi_nilai_huruf(110)


if __name__ == "__main__":
    unittest.main()
