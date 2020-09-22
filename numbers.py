import math as M

pi = M.pi
r = int(input("geef de straal:"))

omtrek = 2 * pi * r
oppervlakte = pi * (r ** 2)

print("oppervlakte " + str(oppervlakte))
print("omtrek " + str(omtrek))