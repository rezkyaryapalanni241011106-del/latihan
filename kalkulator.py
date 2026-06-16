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
    
k = Kalkulator (10,6)
print(k.tambah())
print(k.kurang())
print(k.bagi())
print(k.kali())
