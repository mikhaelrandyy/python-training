def membalik_string(kalimat):
    kalimat = kalimat.lower()
    kalimat = kalimat[::-1]  
    return kalimat
    
input_kalimat = input("Masukkan kalimat: ")
print(membalik_string(input_kalimat))