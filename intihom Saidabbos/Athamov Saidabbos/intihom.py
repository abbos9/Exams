# Imtihon:

# 1. 1 dan 100 gacha bo'lgan sonlar orasida juft sonlarini print qiling. for va range orqali

# for num in range(1, 100 + 1):
#     if num % 2 == 0:
#         print(num)

# 2. Ichida 5 ism saqlaydigan o'zgaruvchi oching. Odamdan qaysi ismni olib tashlash kerakligini
#    sorang va uni chopib tashlang. Funksiya orqali.

# def name_deleter(names: list, use):
#     name = names.remove(use)
#     print(names)
#     return name
#
#
# ismlar = ['saidabbos', 'abbos', 'egamberdi', 'ismoil', 'ibrohim']
# print(ismlar)
# user = input('entyer your name: ')
# res = name_deleter(names=ismlar, use=user)


# 3. Odamdan ikkita son so'rang va ularni bir biriga kopaytirib qaytarib beradigan
#    funksiya yozing.

# def kopayturuvchi(num: int, num2: int):
#     result = num * num2
#     return result
#
#
# user1 = int(input('enter your number1: '))
# user2 = int(input('enter your number2: '))
# res = kopayturuvchi(user1, user2)
# print(res)
# 4. Odamdan ismini input qilib oling va uni ichida nechta unli harf bor bolsa barchasini
#    ismini ichidan olib tashla qaytarib beradigan funksiya yozing.
#    Masalan: name = "Sanjarbek" => "Snjrbk" => barcha unli harflar yoqoldi


# def unllilar(user):
#     a = ''
#     for harf in user:
#         if not harf.lower() in 'aouie':
#             a += harf
#     return a
#
#
# user1 = input("enter your name: ")
#
# res = unllilar(user1)
# print(res)
# 5. Odamdan 1 dan 10 gacha bo'lgan son kiritishini sorang. Va usha sonni 2-darajaga oshirib
#    qaytarib beradigan funksiya yozing.

# def asker(num:int):
#     number = num ** 2
#     return number
#
#
# user = int(input('enter your num 1> 10: '))
#
# res = asker(user)
# print(res)

# 6. Ichida 5 ta shahar nomi bo'lga list yarating. Va jami shaharlarni nomlarini ichida
#    nechta unli harf borligini topib beradigan funksiya yozing.

# countries = ["amerika", "fransiya", "dubai", "russiy", "turkiya"]


# def unli(country):
#     count = 0
#
#     for name in country:
#         for i in name:
#             if i in "aouie":
#                 count += 1
#     return count
#
#
# res = unli(countries)
# print(res)

# 7. Odamdan yoshini sorang va uni nechinchi yil tugilganini aytib beradigan funksiya yozing.

# def age(age: int):
#     year = 2023 - age
#     return year
#
#
# user = int(input('enter your age: '))
# res = age(user)
# print('you was born in', res)

# 8. 10 random toq son taxmin qiling va ularni listga qoshib qaytarib bering.
# import random
#
# nums = []
#
# while len(nums) < 10:
#     a = random.randint(1, 100)
#     if a % 2 == 1:
#         nums.append(a)
#
#
# print(nums)


# 9. Odamdan nechinchi yil tug'ilganini so'rang va uning raqamlari yigindisini qaytarib
#    beradigan funksiya yozng.
#    Masalan: age = 2002 => 2 + 0 + 0 + 2 = 4 => yani raqamlari yigindisi 4

# def age(year):
#     result = 0
#
#     for num in year:
#         result += int(num)
#
#     return result
#
#
# user = input('enter your age: ')
# print(age(user))

# 10. Ichida 10 raqam bor tuple yarating va uni ichidan toq sonlarni olib tashlang.

# numbers = (2, 3, 5, 67, 7, 687, 79, 8, 23, 45)
# nums = []
# toq = []
# for num in numbers:
#     if num % 2 == 0:
#         nums.append(num)
#     elif num % 2 == 1:
#         toq.append(num)
# print(nums)
# print(toq)
# 1. bizz = 3 | bazz = 5 | 1 dan yuzgacha bo'gan sonlardan list hosil qiling. 3     te ga bolinadiganini orniga fizz 5 ga esa buzz
#   qoyib keting
#
# bizz = 3
# bazz = 5
# # ln = []
# for num in range(1, 100 + 1):
#     if num % 3 == 0:
#         num = bazz
#
#     elif num % 5 == 0:
#         num = bizz
#
#     print(num)
# print(bizz, bazz)

# 2. sonni tub yoki tub emasligini aniqlaydigan kod yozing

# user = int(input('enter your number: '))
# if user % 2 == 0:
#     print('juft')
# else:
#     print('tub')

# 3. odamdan gap qabul qiling va ularni har bir so'zini teskari qilib qaytaring

# user = input('enter your text: ')
# user = user[::-1]
# print(user)
# 4. odamdan har xil katta va kichik harflar aralashgan text so'rang. Kattalarini kichkina kichkinalarini esa katta qilib
#   qaytaring
# user = input('enter words: ')
# for num in user:
#     if num.islower():
#         son = num.upper()
#         print(son)
#     elif num.isupper():
#         son = num.lower()
#         print(son)
# 5. Ichida 10 son bor list yarating max va minni o'rnini almashtiring
l = [2, 45, 65, 67, 3, 23, 5, 6, 243, 65]
oxirgi = l.sort()
ohirgi = l[-1]
birinchi = l[0]
s = l.insert(birinchi,ohirgi)
d = l.insert(0, ohirgi)

print(d)
print(l)
print(s)
🇺🇿 bu bot uyga vazifa sifatida yaratilgan
🇷🇺этот бот был создан в учубных целях
🇺🇸 this bot has created to learning  interesting