def hitung_kata_unik(kalimat):

     for tanda in [",", "/", "!", ".", "?"]:
        kalimat = kalimat.replace(tanda, " ")

        kata_list = kalimat.lower().split()
        kata_unik = set(kata_list)  
        return len(kata_unik)  

kalimat = "Python itu mudah / Python itu powerful, Python sangat keren"
print(hitung_kata_unik(kalimat))