# 10. while orqali 1 dan 1000 gacha sonlarni ichida 3 va 5 ga bo'linadigan sonlarni print qiling.
num = 1
while 1000 > num:
    num += 1
    if num % 3 == 0 and num % 5 == 0:
        print(num)
