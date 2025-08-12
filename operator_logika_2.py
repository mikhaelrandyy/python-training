def check_usia(params):
    result = ""
    if params >= 18 and params <= 60:
        result = "Usia Produktif"
        return result
    elif params < 18:
        result = "Masih muda"
        return result
    else:
        result = "Sudah tua"
        return result
    
input_usia = int(input("Masukkan usia: "))

print(check_usia(input_usia))