def jumlah_digit(angka):
    convert_angka = str(angka) 
    total = 0 

    for x in convert_angka:  
        total = total + int(x)  
    return total

angka = 12345
print(jumlah_digit(angka)) 



# def jumlah_data(data):
#     obj_new = data[0]  
#     obj_split = obj_new.split()  
#     for x in obj_split:
#         obj = x
#         return obj

# data = ["Python sangat indah"]
# print(jumlah_data(data))  
