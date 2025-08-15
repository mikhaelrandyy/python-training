def is_palindrome(kalimat):
    kalimat = kalimat.lower()
    kalimat = ''.join(char for char in kalimat if char.isalnum())
    if kalimat == kalimat[::-1]:
        return True
    else:
        return False
    
input_kalimat = input("Masukkan kalimat: ")
print(is_palindrome(input_kalimat))