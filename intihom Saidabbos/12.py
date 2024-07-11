# 12. Odamdan ismini input orqali so'rang. Va uning ichida nechta unli harf borligini topib beradigan kod yozing.
user = input("ismingizni kiriting: ")
un_word = 0
for name in user:
    if name == 'a' or name == 'u' or name == 'i' or name == 'e' or name == 'O':
        un_word += 1
print(un_word)
