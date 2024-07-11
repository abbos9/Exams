# 20. Odamdan input orqali text so'rang va uni ichida nechta so'z borlini topib beradigan kod yozing.
list = []
for num in range(1, 100 + 1):
    if num % 5 == 0 and num % 7 == 0:
        list.append(num)
print(list)