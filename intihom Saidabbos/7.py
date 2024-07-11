# 7. Barcha bilgan string metodlaringizga tarif bering.
name = "mening ismim Saidabbos"
name = name.lower()  # string ichidagi hamma harfni kichkina qiladi
name = name.upper()  # string ichidagi hamma harfni kotta qiladi
name = name.capitalize()  # str ichidagi textning boshidagi brininchi  harifni kotta qiladi
name = name.title()  # str ichidagi hamma texlani boshidiy harifni kotta qiladi
name = name.index('MEN')  # ichiga yozilgan sozlani indexsini topib beradi

name = name.count('S')  # ichiga yozilgan sozni harifni qancha ligini yozadi
name = name.replace('o', 'Ayubxon')  # index boyicha qidiradi textbni
# agar topsa ikkinchi yozilagan textga almashtiradi
name = name.strip()  # oldindiy va orqadiy bosh joyini olip tashlidi
name = name.rstrip()  # ong tomondiy bosh joyini yoq qiladi
name = name.lstrip()  # chap tomondiy bosh joyini yoq qiladi
# yozishga vaqt qomadi
name = name.split()  # o'ziga berilgan so'z bo'yicha string kesadi va uni list holatda qaytaradi,
# agar hech nima berilmasa bo'sh joy bo'yicha kesadi
name = name.isalpha()  # string faqat harflardan tashkil topganmi yo'qmi tekshiradi
name = name.isdigit()  # string faqat sonlardan tashkil topganmi yo'qmi tekshiradi
name = name.isalnum()  # string faqat raqam va harflardan tashkil topganmi yo'qmi tekhiradi
name = name.islower()  # stringni hamma harflari kichkinami yoki yo'qmi tekshiradi
name = name.isupper()  # stringni hamma harflari kattami yoki yo'qmi tekshiradi
name = name.find('elon')  # o'ziga berilgan so'zni indexini topadi agar topa olmasa -1 qaytaradi
