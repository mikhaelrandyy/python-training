# angka = [1, 2, 3]
# angka.append(4)
# angka.remove(2)
# print(angka)

# mhs = {"nama": "Randy", "umur": 20}
# mhs["alamat"] = "Jakarta"
# print(mhs)

# genap = [x for x in range(15) if x % 5 == 0]
# print(genap)

from collections import Counter

text = "taiwan mobile 2025"
text = text.replace(" ", "")  # hapus spasi
freq = Counter(text)

for char, count in freq.items():
    print(f"{char}: {count}")