# 14. for va range orqali 1 dan 100 gacha sonlar ichidan 5 va 7 ga bolinadiganlarini alohida listga olib chiqing.
list = []
for num in range(1, 100 + 1):
    if num % 5 == 0 and num % 7 == 0:
        list.append(num)
print(list)
