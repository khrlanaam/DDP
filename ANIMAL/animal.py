class animal:
    def __init__(self, nama, makanan, hidup, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak

    def info_animal(self):
        print(f"Nama Hewan\t\t\t: {self.nama}")
        print(f"Makanan Hewan\t\t\t: {self.makanan}")
        print(f"Hidup di\t\t\t: {self.hidup}")
        print(f"Berkembang biak\t\t\t: {self.berkembangbiak}")    
    