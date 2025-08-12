def hitung_kata_unik(teks):
    teks = teks.lower()
    teks_bersih = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in teks)
    kata_list = teks_bersih.split()
    kata_unik = set(kata_list)
    return len(kata_unik)

# Definisikan kalimat di luar fungsi
kalimat = "Hallo, dunia! Selamat datang di dunia Python. Python itu menyenangkan."

# Panggil fungsi
print(hitung_kata_unik(kalimat))
