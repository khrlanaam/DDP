def biaya_patungan(total_biaya, jumlah_peserta):
    return total_biaya / jumlah_peserta

total = float(input("Masukkan total biaya: "))
peserta = int(input("Masukkan jumlah peserta: "))
hasil = biaya_patungan(total, peserta)

print(f"Setiap orang harus membayar: Rp{hasil:,.2f}")
