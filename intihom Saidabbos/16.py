# 16. Odamdan 0 dan katta son bo'lgan son kiritishini so'rang. Va 0 dan boshlab usha songacha bo'lgan sonlarni
#    yig'indisini topadigan kod yozing.
user = int(input("0 dan kotta raqam kiriting: "))
count = 0
for count in range(0, user):
    if user == 0:
        print("siz 0 yozdis. 0 dan kotta son yozing")
    elif user > 0:
        count += 1


print(count)