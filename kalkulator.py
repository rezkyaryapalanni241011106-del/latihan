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


aritmatika = input("Pilih Operasi (tambah/kurang/kali/bagi)").lower()
if aritmatika == "tambah":
    print (k.tambah())
elif aritmatika == "kurang":
    print(k.kurang())
    
elif aritmatika == "bagi":
    print(k.bagi())
    
elif aritmatika == "kali":
    print(k.kali())
else:
    print("Pilhan tidak valid")
    
