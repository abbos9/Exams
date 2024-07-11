# 17. while orqali 1 dan 1000 gacha bo'lgan toq sonlarni yig'indisini topadigan kod yozing.

count = 0
while count < 1000:
    count += 1
    if count % 2 != 0:
        count += count
print(count)
