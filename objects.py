'''
    OBJECTS — OBYEKTLAR
        (1) What is object — Obyekt nima?
        (2) Iterable objects & RANGE — Takrorlanadigan obyektlar va RANGE
        (3) DICTIONARY
        (4) Error handling system — Xatolarni boshqarish tizimi
'''

import array  # package/module — paket/modul
import math  # package — paket
from math import ceil  # math modulidan ceil funksiyasini olib kelish

print("===== What is object =====")
# An object has state and method properties. — Obyektning state va metod xususiyatlari mavjud.
# Everything is object in Python! — Python'da hamma narsa obyekt!

print(type('Hello World!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP


# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritance | Polymorphism


result1 = math.ceil(97.7)
print("result1:", result1)

result2 = ceil(98.7)
print("result2:", result2)

print(type(ceil))  # ceil funksiyasining turini tekshirish


print("===== Error handling system =====")
# Error handling system — xatolarni boshqarish tizimi
# try, except, else, finally — xatolar bilan ishlash uchun ishlatiladi
'''
try      → kodni sinab ko‘r
except   → xato bo‘lsa ushla
else     → xato bo‘lmasa bajar
finally  → har qanday holatda bajar
'''

car_dict = dict(name="Tayota", year=2026, electric=True)
# car_dict nomli dictionary yaratildi
# name, year, electric — keylar
# Tayota, 2026, True — value'lar


try:
    # try — xato chiqishi mumkin bo‘lgan kod shu yerga yoziladi

    print("passed here")
    # "passed here" — kod shu qismgacha muvaffaqiyatli kelganini ko‘rsatadi

    a = car_dict.speed
    # car_dict ichidan speed propertysini olishga harakat qilmoqda
    # Lekin dictionaryda speed mavjud emas

    result = car_dict["origin"]
    # car_dict ichidan "origin" keyini olishga harakat qilmoqda
    # "origin" keyi mavjud emas

    print("result:", result)
    # result qiymatini ekranga chiqaradi


except KeyError as err:
    # KeyError — dictionaryda mavjud bo‘lmagan key chaqirilganda yuz beradi

    print("No origin state property found:", err)
    # "origin" keyi topilmasa shu xabar chiqadi

# except (KeyError, AttributeError) as err:
#     print("ERROR:", err) //a = car_dict.speed shuni oshirip tur✅
# except Exception as err:
#     print("General ERROR:", err)   #HAMME TURDEGI ERRORDI SHIGARADI✅

except AttributeError as err:
    # AttributeError — mavjud bo‘lmagan attribute/property chaqirilganda yuz beradi

    print("No speed found:", err)
    # speed propertysi topilmasa shu xabar chiqadi


else:
    # else — try ichidagi kod xatosiz ishlasa bajariladi

    print("Executed successfully without errors")
    # Kod hech qanday xatosiz muvaffaqiyatli bajarilganini bildiradi


finally:
    # finally — xato bo‘lishi yoki bo‘lmasligidan qat’i nazar bajariladi

    print("Final closing logic")
    # Yakuniy kod shu yerda bajariladi
