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