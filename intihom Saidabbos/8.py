# 8. Barcha bilgan list metodlaringizga tarif bering.

numbers = [-1, 12, -4, 12, 22, 44, -89, -65, 12, 22, 444, -876, 21]

numbers.append(1212)  # listga  yangi element qo'shadi oxiriga!
numbers.insert(0, 1212)  # index bo'yicha yangi elementni qo'shadi
numbers.index(-1)  # qidiradi topsa indexini qaytaradi o'ziga berilgan elementni!
numbers.remove(-1)  # o'ziga berilgan elementni  o'chiradi nomi bo'yicha!
numbers.pop(0)  # o'ziga berilgan elementni indexsi  boyicha ochiradi, agar hech nima bermasa oxiridan o'chiradi
numbers.count(-1)  # list ichida nechta ekanligini sanab qaytaradio'ziga berilgan elementni

numbers.extend(numbers)  # ikkita listni qoshadi
numbers.clear()  # listni bohs qildai

