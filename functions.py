'''FUNCTIONS
(1)DEFINE va CALL
(2)Parametr vs Argument
(3)Keyword & Default arguments
(4)Scope

'''

print("=====DEFINE va CALL=====")
# build in fuctionlar >print ()type()
# Function -Reusable block of code! Malumot bir mantiqni ishga tushrip beradigan cod block
# Instead of block {} in JAVA,Python uses indentation!

# DEFINE indentation!


def greet(a):
    # void  bos bolmawi kerek pass boliw kerek esh bolmaganda
    print(f"How do you do ,{a}")


def greeting(b):  # return
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute
result1 = greet('DANNY')
print("result1:", result1)

result2 = greeting("Martin")
print("result2:", result2)


# Parametr vs Argument
# Keyword & Default arguments
print("=====Keyword & Default arguments=====")
# DEFINE # Keyword


def give_greet(name, age):
    print("give_greet is executed")
    return f"Hello {name},you are {age} years old"


# CALL # Keyword

result3 = give_greet(name="Danny", age=29)
print("result3:", result3)
# DEFINE # Default arguments


def how_are(name, age=30):
    print("next test done")
    return f"My name is {name},and I'm {age}"


result4 = how_are(name="Islam")
print("result4:", result4)


print("=====Scope=====")
# Scope
b = 300  # 3

# DEFINE


def calculate(a):  # 2
    c = a*b  # 1
    print(f"the c value: {c}")


# CALL
calculate(10)
