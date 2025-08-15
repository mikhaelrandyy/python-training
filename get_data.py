nama = ["Randy", "Budi", "Rere", "Mikhael"]

find_steven = None
for x in nama:
    if x == "Steven":
        print("Kamu mendapatkan nama steven")
        find_steven = x
        break

if find_steven is None:
    print("tidak ada nama steven")
