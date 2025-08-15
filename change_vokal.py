def ganti_vokal(teks):
    pengganti = "*"
    vokal = "aeiou"
    hasil = []

    for x in teks:
        if x.lower() in vokal:  # cek lowercase agar kapital juga terdeteksi
            hasil.append(pengganti)
        else:
            hasil.append(x)

    result = "".join(hasil)  
    return result  

# Contoh penggunaan
input_teks = input("Masukkan teks: ")
print(ganti_vokal(input_teks))
