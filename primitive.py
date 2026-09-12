print("=====Number=====")
# in JAVA ,variable is a name of storge location!
# in PYTHON ,variable  is named reference! malumat manziliga bogliq  reference nomlanishi

count = 100
count_type = type(count)
# print("count:", count, count_type)
print(f"the count:{count}and type {count_type}")


result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("=====String======")
# METHODS: upper) lower) title() find() replace()
course = "AI Python FullStack"  # COURSE dep har turli stringlardi alsa boladi
result = type(course)
print(f"the result (1): {result}")

result = course.title()
print(f"the result (2): {result}")

result = course. upper()
print(f"the result (3): {result}")

# usi result di course tenlesen pastegi bas qiymatqa tasir otkeredi ⬇️
result = course. replace("FullStack", "MasterClass")
print(f"the result (4): {result}")
print(course)  # Baslangish qiymatti ozgertirmeydi!!!⬆️

print("===== boolean =====")
# functions > type() input() bool() int() str()
y = input("Give your value for y: ")
print("y:", y)

result = y.isnumeric()  # son kiritildimi?
print(f"the input value is numeric: {result}")

# TRUTHY vs FALSY value
# TRUTHY: True 100 -100 "MIT"
# FALSY: False 0 "" None

test_falsy = "" or False or None or 0
print("test_falsy:", bool(test_falsy))

test_truthy = "MIT"
print("test_truthy:", bool(test_truthy))
