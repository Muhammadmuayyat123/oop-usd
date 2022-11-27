# Muhammad muayyat sabir
# D0221114
# Informatika H

class Persegi:
    def __init__(self,sisi=0):
        self.sisi = sisi
  
    def luas(self):
        return self.sisi * self.sisi


class Lingkaran:
    def __init__(self,jari=0):
        self.jari = jari

    def luas(self):
        return 3.14 * (self.jari**2)

class Segitiga:
    def __init__(self, alas=0, tinggi=0):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

persegi = Persegi()
lingkaran = Lingkaran()
segitiga = Segitiga()

print('''1. Persegi
2. Lingkaran
3. Segitiga''')

pilihan = int(input("Masukkan luas yang dicari : "))
if pilihan == 1:
    persegi.sisi = float(input("Masukkan Sisi : "))
    luas  = persegi.luas()
elif pilihan == 2:
    lingkaran.jari = float(input("Masukkan Jari - Jari : "))
    luas = lingkaran.luas()
elif pilihan == 3:
    segitiga.alas = float(input("Masukkan Alas : "))
    segitiga.tinggi = float(input("Masukkan Tinggi : "))
    luas = segitiga.luas()
else:
    print("Periksa kembali inputan Anda!")
    
print("Luas = ", luas )

