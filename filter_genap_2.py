def list_angka_genap_terurut(angka_list):
    angka_genap = [x for x in angka_list if x % 2 == 0]
    angka_genap.sort()
    return angka_genap

angka_list = [7, 4, 1, 8, 2]
print(list_angka_genap_terurut(angka_list))