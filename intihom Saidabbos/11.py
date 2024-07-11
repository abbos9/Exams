# 11.Odamdan ikki xonali son sorang va usha sonni ikkala sonini bir birga qo'shib bering. Masalan:
#     odam 12 kiritsa unga 3 qaytarasiz chunki 12 -> 1 + 2 = 3
#     odam 54 kiritsa unga 9 qaytarasiz chunki 54 -> 5 + 4 = 9
num1 =int(input("write number: "))
num2 =int(input("write number: "))
arif = (input("write arifmetik: "))

if arif == "*":
    print(num1 * num2)
elif arif == "/":
    print(num1 / num2)
elif arif == "+":
    print(num1 + num2)
elif arif == "-":
    print(num1 - num2)
elif arif == "//":
    print(num1 // num2)
elif arif == "**":
    print(num1 ** num2)
elif arif == "%":
    print(num1 % num2)
else:print("bunaqa operator yoq")
# apgreade