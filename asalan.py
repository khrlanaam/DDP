hitung_luas = int(input("""Pilih salah satu:
                        1. Hitung luas persegi
                        2. Hitung luas lingkaran
                        3. Hitung luas segitiga                      
"""))
pi = 3.14

match hitung_luas:
    case 1:  
        sisi = float(input("Masukkan sisi persegi: "))
        luas_persegi = sisi ** 2
        print(f"Luas persegi: {luas_persegi}")
        
    case 2: 
        radius = float(input("Masukkan jari-jari lingkaran: "))
        luas_lingkaran = pi * radius ** 2  
        print(f"Luas lingkaran: {luas_lingkaran}")
        
    case 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas_segitiga = 0.5 * alas * tinggi
        print(f"Luas segitiga: {luas_segitiga}")
        
    case _: 
        print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")
