# 19. Ushbu list ichidan 3 va 7 ga qoldiqsiz bo'linadigan sonlarning yig'indisni toping.
numbers = [12, 22, 21, 4, 66, 43, 42, 122, 43, 67, 84, 64, 22, 222, 11]
count = 0
for num in numbers:
    if num % 3 == 0 and num % 7 == 0:
        count += num
print(count)
