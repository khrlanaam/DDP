harga_perliter = {
    "pertalite" : 10000,
    "pertamax" : 14000,
    "pertamax turbo" : 17000
}
jarak_perliter = {
    "pertalite" : 12,
    "pertamax" : 13,
    "pertamax turbo" : 13.5
}
kota = {
    "jakarta" : 20,
    "bekasi" : 35.7,
    "depok" : 5,
    "tanggerang" : 99,
    "bogor" : 120.6
}
nama_kendaraan = int(input("masukkan nama kendaraan? (motor,mobil): ")).lower()
jenis_bensin = int(input("masukkan jenis bensin? (pertalite,pertamax,pertamax turbo): ")) .lower()
kota_dituju = int(input("masukkan kota yang dituju? (jakarta,bekasi,depok,tanggerang,bogor): ")) .lower()

jenis_bensin in harga_perliter and kota_dituju in kota;
harga = harga_perliter[jenis_bensin]
jarak_tempuh = jarak_perliter[jenis_bensin]

jarak = kota[kota_dituju]

pemakaian_bensin =jarak / jarak_tempuh
total_harga = pemakaian_bensin * harga

print("\n---hasil perhitungan ---")
print("nama kendaraan"),nama_kendaraan
print("jenis bensin"),jenis_bensin
print("kota yang dituju"),kota_dituju
print("pemakaian bensin"),pemakaian_bensin
print("total harga dari bensin: Rp",sum(total_harga,2))

