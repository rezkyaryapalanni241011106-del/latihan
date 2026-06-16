class Kalkulator:
    def __init__(self,angka_1,angka_2):
        self.angka_1 = angka_1
        self.angka_2 = angka_2

    def tambah (self):
        return self.angka_1 + self.angka_2
    def kurang (self):
        return self.angka_1 - self.angka_2
    def bagi (self):
        return self.angka_1 / self.angka_2
    def kali (self):
        return self.angka_1 * self.angka_2

angka_1 = float(input("Masukkan angka pertama: "))
angka_2 = float(input("Masukkan angka kedua: "))
k = Kalkulator (angka_1,angka_2)
print(k.tambah())
print(k.kurang())
print(k.bagi())
print(k.kali())
