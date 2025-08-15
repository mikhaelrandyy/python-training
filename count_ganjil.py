def count_angka_ganjil(angka_list):
    count = 0
    for angka in angka_list:
        if angka % 2 != 0:
            count += 1
    
    return count

angka_list = [1, 2, 3, 4, 5]

print(count_angka_ganjil(angka_list))