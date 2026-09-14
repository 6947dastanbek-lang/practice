'''
    CLASS — KLASS
        (1) What is class — Class nima?
        (2) ordinary vs static properties — Oddiy va static xususiyatlar
        (3) special/magic methods — Maxsus metodlar
'''

print("===== What is class =====")
# class — blueprint for object creation!⬇️
# class — obyekt yaratish uchun blueprint (qolip/reja)
# Ya'ni class orqali keyinchalik obyektlar yaratamiz.

# structure > state > constructor > method ⬇️
# structure — obyektning tuzilishi
# state — obyektning ma'lumotlari/holati
# constructor — obyekt yaratilganda avtomatik ishlaydigan maxsus metod
# method — obyekt nima qila olishini bildiradigan funksiya


class Person:
    # Person — class nomi
    # Bu class orqali odam (Person) obyektlarini yaratamiz.

    # state
    message = "class state property"
    # message — class property
    # Bu Person class'iga tegishli umumiy property.

    # constructor

    def __init__(self, name, age):
        # __init__ — constructor
        # Person obyekti yaratilganda avtomatik ishlaydi.
        self.name = name
        self.age = age

    # method

    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explain(cls):
        # @classmethod — bu class method ekanligini bildiradi.
        # Bu method obyektga emas, classning o‘ziga tegishli.
        # cls — classning o‘zini bildiradi.

        print("static method property executed!")


# Person classidan obyektlar yaratamiz.
person1 = Person("Justin", 25)
# person1 — Person classidan yaratilgan obyekt
person2 = Person("Martin", 35)
person3 = Person("John", 22)
person4 = Person("Danny", 29)

# ordinary state — oddiy state/property
print("person1.name:", person1.name)
# person1 obyektining name propertysini olamiz.
# Natija: person1.name: Justin


# ordinary method — oddiy method
person1.introduce()
# person1 obyektining introduce() metodini chaqiramiz.
# Natija: Justin says: How do you do!
person2.say_age()
# person2 obyektining say_age() metodini chaqiramiz.
# Natija: Martin says I am 35!
person4.say_age()


print("===== ordinary vs static properties =====")
# static state
new_message = Person.message
print("new_message is:", new_message)


# static method
Person.explain()
# explain() class methodini Person classining o‘zidan chaqiryapmiz.
# Buning uchun person1.explain() qilish shart emas.


print("===== special/magic methods =====")

# Ularning nomi odatda ikkita __ bilan boshlanib, ikkita __ bilan tugaydi.

# Python's most common special methods are below:
# Python'dagi eng ko‘p ishlatiladigan maxsus metodlar:
# __init__  — obyekt yaratilganda ishlaydi
# __new__   — yangi obyekt yaratish jarayonida ishlaydi ✅
# __str__   — obyektni string ko‘rinishida chiqarishda ishlaydi
# __call__  — obyektni funksiya kabi chaqirish imkonini beradi
# __getitem__ — [] orqali element olishda ishlaydi
# __eq__    — == taqqoslashda ishlaydi
# __len__   — len() ishlatilganda ishlaydi


class Car():

    # state
    description = "This class makes cars"
    # description — class property.
    # Car classi nima uchun ekanligini saqlab turibdi.

    # constructor
    def __new__(cls, *args):
        print("__new__")
        return super().__new__(cls)

    def __init__(self, name, year):
        # __init__ — special/magic method.
        # Car obyekti yaratilganda avtomatik ishlaydi.
        self.name = name
        self.year = year

    # method

    def start_engine(self):
        print(f"the {self.name} started engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")

    def __str__(self):
        return f"{self.name} was produced in {self.year} year!"
     # Obyektni string qilib beradi

    def __call__(self):
        print("object called as function!")
        return True
    # Obyektni funksiya kabi chaqiradi

# Car classidan yangi obyekt yaratamiz.


my_car = Car("Ferrari", 2025)

# Bu qatorda __init__ avtomatik ishga tushadi:
# self.name = "Ferrari"
# self.year = 2025


my_car.start_engine()
# my_car obyektining start_engine() methodini chaqiryapmiz.
# the Ferrari started engine!


my_car.stop_engine()
# my_car obyektining stop_engine() methodini chaqiryapmiz.
# the Ferrari stopped engine!
print("-----")
your_car = Car("BMW", 2026)
print(your_car)
your_car()  # CALL
response = your_car()
print("response:", response)
