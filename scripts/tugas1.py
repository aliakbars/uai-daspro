from numpy.testing import assert_approx_equal
import math

def luas_segitiga(alas, tinggi):
    pass

def luas_persegi(sisi):
    pass

def luas_persegi_panjang(panjang, lebar):
    pass

def luas_lingkaran(jari_jari):
    # Gunakan math.pi sebagai pengganti nilai pi atau 3.14
    pass

def luas_segi_enam(sisi):
    # Gunakan math.sin(math.pi/3)
    pass

def masukan_pengguna():
    pass

def looping_masukan_pengguna():
    pass

def main():
    looping_masukan_pengguna()

def test():
    assert luas_segitiga(3, 4) == 6
    assert luas_segitiga(10, 2) == 10
    assert luas_persegi(9) == 81
    assert luas_persegi_panjang(7, 3) == 21
    assert luas_persegi_panjang(15, 10) == 150
    assert_approx_equal(luas_lingkaran(7), 153.938, 4)
    assert_approx_equal(luas_lingkaran(14), 615.752, 4)
    assert_approx_equal(luas_segi_enam(2), 10.39, 4)
    assert_approx_equal(luas_segi_enam(9), 210.44, 4)

if __name__ == '__main__':
    test()
    main()