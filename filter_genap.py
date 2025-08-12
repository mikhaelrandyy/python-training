def filter_ganjil(angka_list):
    angka_ganjil = [x for x in angka_list if x % 2 != 0]
    angka_ganjil.sort()
    return angka_ganjil

print(filter_ganjil([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

