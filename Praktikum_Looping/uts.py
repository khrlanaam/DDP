nilai = int(input("masukkan(o-100):"))
if 90 <= nilai <= 100:
    ket="A"
elif 80 <= nilai <=89:
    ket-"B"
elif 60 <= nilai <=79:
    ket-"C"
elif 0 <= nilai <=59:
    ket="D"
else:
    ket="Tidak valid"
print("Nilai: ", nilai, "Ket: ", ket)