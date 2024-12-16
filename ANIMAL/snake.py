from animal import animal 

class Snake(animal):  # Gunakan huruf kapital di nama kelas
    def __init__(self, nama, makanan, hidup, berkembangbiak, berbisa, jenis):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.berbisa = berbisa
        self.jenis = jenis

    def info_snake(self):
        super().info_animal() 
        print(f"Berbisa\t\t\t\t: {self.berbisa}")
        print(f"Jenis\t\t\t\t: {self.jenis}")

python = Snake("Ular Python", "Daging", "Hutan", "Bertelur", "Tidak", "Python")

print("## Info Snake ##")
python.info_snake()
