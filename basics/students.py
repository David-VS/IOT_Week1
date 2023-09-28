import random

students = ["John", "Karl", "Olaf", "Zacharia", "Elke", "Jean-luc", "Jean-jean", "Kevin", "Sidney"]

print("aantal groepen " + str(len(students) // 4))
print("resterende studenten " + str(len(students) % 4))
print(students[4:8])

print(students[random.randint(0, len(students)-1)])
print(random.sample(students, 1))
print(random.choice(students))
