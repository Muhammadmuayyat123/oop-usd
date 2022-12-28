#Muhammad muayyat sabir
#D0221114
#Informatika H

import math

class BangunRuang:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def luasPermukaan(self):
        pass

    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__(sisi, sisi, sisi)

    def luasPermukaan(self):
        return 6 * self.panjang**2

    def volume(self):
        return self.panjang**3

class Balok(BangunRuang):
    def luasPermukaan(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class LimasSegitiga(BangunRuang):
    def luasPermukaan(self):
        luas_alas = 0.5 * self.panjang * self.lebar
        luas_sisi = self.panjang * self.tinggi / 2
        return luas_alas + 3 * luas_sisi

    def volume(self):
        return (1/3) * self.panjang * self.lebar * self.tinggi

# Contoh penggunaan kelas
while True:
    print("""Pilih Bangun Ruang untuk
menghitung Volume dan Luasnya
1. Kubus
2. Balok
3. Limas segitiga
4. Berhenti""")

    pilihan = input("=> ")

    if pilihan == "1":
        while True:
            print("""1. Menghitung Luas permukaan Kubus
2. Menghitung Volume Kubus
3. Berhenti""")
            pilihanKubus = input("Masukkan pilihan anda : ")
            if pilihanKubus == "1":
                sisi = float(input("Masukkan sisi : "))
                kubus = Kubus(sisi)
                print(f"Luas permukaan kubus : {kubus.luasPermukaan()}\n")
            elif pilihanKubus == "2":
                sisi = float(input("Masukkan sisi : "))
                kubus = Kubus(sisi)
                print(f"Volume Kubus : {kubus.volume()}\n")
            elif pilihanKubus == "3":
                break
            else:
                print("Pilihan anda tidak ada dalam menu!")
    
    elif pilihan == "2":
        while True:
            print("""1. Menghitung Luas Permukaan Balok
2. Menghitung Volume Kubus
3. Berhenti""")
            PilihanBalok = input("Masukkan pilihan anda : ")
            if PilihanBalok == "1":
                print("Masukkan nilai panjang, lebar, dan tinggi untuk balok : ")
                panjang = float(input())
                lebar = float(input())
                tinggi = float(input())
                balok = Balok(panjang, lebar, tinggi)
                print(f"Luas permukaan Balok : {balok.luasPermukaan()}\n")
            elif PilihanBalok == "2":
                print("Masukkan nilai panjang, lebar, dan tinggi untuk balok : ")
                panjang = float(input())
                lebar = float(input())
                tinggi = float(input())
                balok = Balok(panjang, lebar, tinggi)
                print(f"Volume Balok : {balok.volume()}\n")
            elif PilihanBalok == "3":
                break
            else:
                print("Pilihan anda tidak ada dalam menu!")
    
    elif pilihan == "3":
        while True:
            print("""1. Menghitung Luas Permukaan Limas Segitiga
2. menghitung Volume Limas Segitiga
3. Berhenti""")
            PilihanLimas = input("Masukkan pilihan anda : ")
            if PilihanLimas == "1":
                print("Masukkan nilai alas, tinggi, dan tinggi limas untuk Limas Segitiga : ")
                alas = float(input())
                tinggi = float(input())
                tinggi_limas = float(input())
                limas_segitiga = LimasSegitiga(alas, tinggi, tinggi_limas)
                print(f"Luas permukaan Limas Segitiga : {limas_segitiga.luasPermukaan()}\n")
            elif PilihanLimas == "2":
                print("Masukkan nilai alas, tinggi, dan tinggi limas untuk Limas Segitiga : ")
                alas = float(input())
                tinggi = float(input())
                tinggi_limas = float(input())
                limas_segitiga = LimasSegitiga(alas, tinggi, tinggi_limas)
                print(f"Volume Limas Segitiga : {limas_segitiga.volume()}\n")
            elif PilihanLimas == "3":
                break
            else:
                print("Pilihan anda tidak ada dalam menu!")
    elif pilihan == "4":
        break
    else:
        print("Pilihan anda tidak ada dalam menu!")
print("Program telah berhenti. Terima Kasih")
