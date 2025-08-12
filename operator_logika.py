def check_angka(params):
    if params > 10 and params % 2 == 0:
        return "Angka Valid ✅"
    else:
        return "Angka Tidak Valid ❌"

input_angka = int(input("Masukkan angka: "))

# Cetak hasil dari fungsi
print(check_angka(input_angka))
