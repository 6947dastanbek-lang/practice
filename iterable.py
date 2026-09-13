print("===== Iterable objects & RANGE =====")

# Iterable obyektlar > string, dict, tuple, list, range, map, filter
# Iterable — ichidagi elementlarni bittadan olish mumkin bo‘lgan obyekt

range_obj = range(3)
# range(3) — 0 dan boshlanib 3 gacha bo‘lgan sonlarni yaratadi
# Natija: 0, 1, 2

print("range_obj:", range_obj)
# range_obj qiymatini ekranga chiqaradi

for letter in "MIT":
    # "MIT" stringidagi har bir belgini bittadan oladi
    print(f"the letter: {letter}")
    # Har bir belgini ekranga chiqaradi

for ele in range_obj:
    # range_obj ichidagi har bir elementni bittadan oladi
    print(f"the element: {ele}")
    # Har bir elementni ekranga chiqaradi


print("===== DICTIONARY =====")
# Dictionary is JSON object!
# Dictionary — JSON obyektiga o‘xshash, key va value ko‘rinishida ma’lumot saqlaydi

person = {"name": "Justin", "age": 25, "single": True}
# person dictionary yaratildi
# name, age, single — key
# "Justin", 25, True — value

person_obj = dict(name="Justin", age=25, single=True)
# dict() orqali dictionary yaratishning boshqa usuli

print(f"the person: {person}")
# person dictionaryni ekranga chiqaradi

print(f"the person_obj: {person_obj}")
# person_obj dictionaryni ekranga chiqaradi


# method: get()
# get() — dictionary ichidan key orqali value olish uchun ishlatiladi

# name = person_obj["name"]
# [] orqali key qiymatini olish mumkin

name = person_obj.get("name")
# get() orqali "name" keyining qiymatini olamiz

hobby = person_obj.get("hobby")
# "hobby" keyi mavjud emas, shuning uchun None qaytaradi

balance = person_obj.get("balance", 0)
# "balance" keyi mavjud emas
# Ikkinchi argument sifatida 0 berilgani uchun 0 qaytaradi

print(f"the name: {name}; hobby: {hobby} and balance: {balance}")
# name, hobby va balance qiymatlarini ekranga chiqaradi


del person_obj["single"]
# "single" key-value juftligini dictionarydan o‘chiradi

for key in person_obj:
    # Dictionary ichidagi keylarni bittadan oladi
    print(f"the key: {key} => value {person_obj.get(key)}")
    # Har bir key va unga tegishli value'ni chiqaradi
