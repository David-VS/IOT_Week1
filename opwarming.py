import math

a = int(input("getal a:"))
b = int(input("getal b:"))

result = a + b
print(result)

result = a / b
print(math.ceil(result))

result = a % b
print(result)

a += 1
b += 1
result = a + b
print(result)
