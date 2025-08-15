def is_palindrome(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
        return "palindrome"
    else:
        return "bukan palindrome"
    
input_kata = input("Masukkan kata atau kalimat: ")
print(is_palindrome(input_kata))
