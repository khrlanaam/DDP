from animal import animal

class Bird(animal): 
    # Konstruktor
    def __init__(self, nama, makanan, hidup, berkembangbiak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.warna = warna
        self.paruh = paruh

    # Method
    def info_bird(self):
        super().info_animal()
        print(f"Warna\t\t\t\t: {self.warna}")
        print(f"Jenis Paruh\t\t\t: {self.paruh}")

# Membuat objek bird
print()
bird = Bird("Elang", "Daging", "Ditebing", "Bertelur", "Coklat", "Bengkok dan Lancip")
print("## Info Bird ##")
bird.info_bird()
