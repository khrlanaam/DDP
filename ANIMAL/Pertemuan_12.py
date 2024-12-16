class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender  

    def berjalan(self):
        print(f"{self.name} sedang berjalan.")

    def berbicara(self):
        if self.gender == "Laki-laki":
            print(f"{self.name} tidak bercerita karena dia {self.gender}.")
        else:
            print(f"{self.name} berbicara karena dia {self.gender}.")


class Mahasiswa(Person):
    def __init__(self, name, age, gender, nim):
        super().__init__(name, age, gender)
        self.nim = nim

andi = Mahasiswa('andi', 20, 'laki-laki','123')
andi.berbicara()