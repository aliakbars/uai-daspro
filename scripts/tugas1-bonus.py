import tugas1

def volume():
    # Definisikan parameter Anda di atas
    pass

def test():
    assert volume(tugas1.luas_segitiga(3, 4), 3, True) == 6
    assert volume(tugas1.luas_segitiga(10, 2), 5) == 50
    assert volume(tugas1.luas_persegi(9), 3, True) == 81
    assert volume(tugas1.luas_persegi_panjang(7, 3), 3, False) == 63
    assert volume(tugas1.luas_persegi_panjang(15, 10), 1) == 150

if __name__ == '__main__':
    test()