class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            dampak = "dampak gempa tidak berasa"
        elif 2 <= self.skala < 4:
            dampak = "dampak gempa bangunan retak-retak"
        elif 4 <= self.skala < 6:
            dampak = "dampak gempa bangunan roboh"
        else:
            dampak = "dampak gempa bangunan roboh dan berpotensi tsunami"

    
        print(f"Lokasi: {self.lokasi}")
        print(f"Skala: {self.skala}")
        print(f"Dampak: {dampak}\n")
