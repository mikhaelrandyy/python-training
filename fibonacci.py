def fibonacci(n):
    # Kalau n <= 0, kembalikan list kosong
    if n <= 0:
        return []
    # Kalau n == 1, kembalikan hanya [0]
    elif n == 1:
        return [0]
    # Kalau n == 2, kembalikan [0, 1]
    elif n == 2:
        return [0, 1]
    
    # Mulai dari dua angka pertama
    deret = [0, 1]
    
    # Tambah angka berikutnya sampai panjang deret = n
    for i in range(2, n):
        angka_berikut = deret[i-1] + deret[i-2]
        deret.append(angka_berikut)
    
    return deret

# Contoh penggunaan
print(fibonacci(7))  # Output: [0, 1, 1, 2, 3, 5, 8]
