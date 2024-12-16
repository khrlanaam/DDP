from animal import animal  

class Fish(animal): 
    def __init__(self, nama, makanan, hidup, berkembangbiak, bernafas, habitat):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.bernafas = bernafas
        self.habitat = habitat

    def info_fish(self):
        super().info_animal() 
        print(f"Bernafas menggunakan\t\t: {self.bernafas}")
        print(f"Habitat di\t\t\t: {self.habitat}")

hiu = Fish("Hiu", "Daging", "Laut", "Melahirkan", "Insang", "Air asin")
print("## Info Fish ##")
hiu.info_fish()
