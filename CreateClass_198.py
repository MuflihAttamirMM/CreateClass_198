class PersegiPanjang:
    def __init__(self, panjang, lebar):
        if panjang <= 0 or lebar <= 0:
            raise ValueError("Panjang dan lebar tidak boleh 0 atau negatif")
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

while True:
    input_panjang = int(input("Masukkan panjang (cm): "))
    input_lebar = int(input("Masukkan lebar (cm): "))

    if input_panjang > 0 and input_lebar > 0:
        break
    print("Nilai tidak boleh 0, coba lagi.\n")

pp = PersegiPanjang(input_panjang, input_lebar)

print(pp)
print("Keliling:", pp.hitung_keliling())
print("Luas:", pp.hitung_luas())