# text = "katak"
# if text == text[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")


def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

kata = input("Masukkan kata atau kalimat: ")

if is_palindrome(kata):
    print("Palindrome ✅")
else:
    print("Bukan palindrome ❌")
