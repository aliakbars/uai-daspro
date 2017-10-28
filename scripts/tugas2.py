from numpy.testing import assert_approx_equal
import os

def rataan(daftar_nilai):
    """
    Menerima masukan berupa list dan mengembalikan satu nilai rata-rata
    e.g. [90, 73, 82, 100, 36, 44, 60] => 69.285...
    """
    pass

def simpangan_baku(daftar_nilai):
    """
    Menerima masukan berupa list dan mengembalikan nilai simpangan bakunya
    Anda dapat memanfaatkan fungsi rataan() di sini
    e.g. [90, 73, 82, 100, 36, 44, 60] => 21.978...
    """
    pass

def median(daftar_nilai):
    """
    Menerima masukan berupa list dan mengembalikan nilai tengahnya
    e.g. [90, 73, 82, 100, 36, 44, 60] => 73
         [90, 73, 82, 36, 44, 60] => 66.5
    """
    pass

def indeks(nilai):
    """
    Menerima masukan berupa nilai dan mengembalikan indeksnya
    e.g. 70 => A
         45 => D
         27 => F
         60 => B
    """
    pass

def rekap(daftar_indeks):
    """
    Menerima masukan berupa daftar indeks dan mengembalikan dictionary berupa jumlah indeks
    e.g. ['A', 'D', 'F', 'B', 'A', 'C'] => {'A': 2, 'B': 1, 'C': 1, 'D': 1, 'F': 1}
    Perhatikan bahwa tidak ada nilai E dalam dictionary yang dihasilkan
    """
    pass

def tulis_laporan(filename):
    pass

def test():
    daftar_nilai = [90, 73, 82, 100, 36, 44, 60]
    assert_approx_equal(rataan(daftar_nilai), 69.285)
    assert_approx_equal(simpangan_baku(daftar_nilai), 21.978)
    assert_approx_equal(median(daftar_nilai), 73)
    assert_approx_equal(median(daftar_nilai[:-1]), 77.5)
    assert indeks(70) == 'A'
    assert indeks(45) == 'D'
    assert indeks(27) == 'F'
    assert indeks(60) == 'B'

def main():
    files = os.listdir('.')
    # Lengkapi kodenya di sini

if __name__ == '__main__':
    test()
    main()